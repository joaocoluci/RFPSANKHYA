# -*- coding: utf-8 -*-
"""Extracao e preenchimento de RFP (xlsx/docx) com o minimo de contexto no modelo.

scan    <arq>                      detecta layout, rotulos e volume
extract <arq> [--map M] [--all]    imprime SO os requisitos sem resposta no cache
apply   <arq> <respostas.tsv>      gera copia preenchida (original intacto)
cache   <respostas.tsv> <arq>      incorpora as respostas ao cache reutilizavel

Mapa (serializado): "aba|indice!linha_cabecalho:id,req,prio,atend,just"
Colunas xlsx em letra (B,C,D,E,F*), docx em indice (0,1,2,3,4*). "*" = criar.
"""
import argparse
import os
import re
import shutil
import sys
import unicodedata
import warnings
import zipfile

warnings.filterwarnings("ignore")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "cache", "respostas.tsv")
CLASSES = {"T": "Total", "P": "Parcial", "N": "Não Atende"}
SUFIXO = " - RESPOSTA SANKHYA"

RE_ID = re.compile(r"^(id|c[oó]d|item|n[uú]m|ref)", re.I)
RE_REQ = re.compile(r"(capacidade|requisito|descri|funcionalidade|necessidade|especifica)", re.I)
RE_PRIO = re.compile(r"(prioridade|criticidade|peso|obrigat)", re.I)
RE_ATEND = re.compile(r"(atendimento|atende|aderenc|aderênc|resposta|situa|status|conformidade)", re.I)
RE_JUST = re.compile(r"(solu[cç]|justificativ|observa|coment|motivo|customiza|evid)", re.I)
STOP = set("""a o e de da do das dos para por com sem em no na nos nas um uma os as ao aos que
ser sao são ter tem the of and com base atraves através partir possibilitando permitindo""".split())


# ---------------------------------------------------------------- utilidades
def norm(texto):
    texto = unicodedata.normalize("NFKD", (texto or "").lower())
    texto = "".join(c for c in texto if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9 ]+", " ", texto)


def tokens(texto):
    return {p for p in norm(texto).split() if len(p) > 2 and p not in STOP}


def similar(a, b):
    if not a or not b:
        return 0.0
    return len(a & b) / float(len(a | b))


def letra(indice):
    s = ""
    indice += 1
    while indice:
        indice, resto = divmod(indice - 1, 26)
        s = chr(65 + resto) + s
    return s


def indice(letras):
    n = 0
    for c in letras.upper():
        n = n * 26 + (ord(c) - 64)
    return n - 1


def prio_curta(valor):
    v = norm(valor)
    if v.startswith("obrig"):
        return "O"
    if v.startswith("desej"):
        return "D"
    if v.startswith("opc"):
        return "Op"
    return (valor or "")[:3]


# ---------------------------------------------------------------- cache
def ler_cache():
    if not os.path.exists(CACHE):
        return []
    itens = []
    with open(CACHE, encoding="utf-8") as fp:
        for linha in fp:
            partes = linha.rstrip("\n").split("\t")
            if len(partes) >= 3:
                itens.append((tokens(partes[1]), partes[0], partes[2]))
    return itens


def buscar_cache(itens, requisito, corte=0.85):
    alvo = tokens(requisito)
    melhor, escore = None, 0.0
    for chaves, classe, just in itens:
        s = similar(alvo, chaves)
        if s > escore:
            melhor, escore = (classe, just), s
    return (melhor, escore) if escore >= corte else (None, escore)


# ---------------------------------------------------------------- leitura
class Tabela(object):
    """Bloco de requisitos localizado num arquivo."""

    def __init__(self, ref, cabecalho, colunas, linhas, rotulos):
        self.ref = ref                # nome da aba (xlsx) ou indice da tabela (docx)
        self.cabecalho = cabecalho    # linha do cabecalho (1-based xlsx, 0-based docx)
        self.colunas = colunas        # dict papel -> indice de coluna (0-based)
        self.linhas = linhas          # [(linha, id, requisito, prioridade)]
        self.rotulos = rotulos

    def mapa(self):
        fmt = letra if self.ref_xlsx else str
        ordem = ["id", "req", "prio", "atend", "just"]
        cols = ",".join(
            (fmt(self.colunas[p]) + ("*" if p == "just" and self.criar_just else ""))
            if p in self.colunas else "-"
            for p in ordem
        )
        return "%s!%d:%s" % (self.ref, self.cabecalho, cols)


def detectar_colunas(celulas):
    """celulas: lista de textos do cabecalho. Retorna papel -> indice."""
    achado = {}
    for i, txt in enumerate(celulas):
        if not txt:
            continue
        for papel, rx in (("just", RE_JUST), ("atend", RE_ATEND), ("prio", RE_PRIO),
                          ("req", RE_REQ), ("id", RE_ID)):
            if papel not in achado and rx.search(txt):
                achado[papel] = i
                break
    return achado


def rotulos_xlsx(caminho, aba, col_atend):
    """Le a lista de valores permitidos na coluna de atendimento."""
    try:
        with zipfile.ZipFile(caminho) as z:
            nomes = [n for n in z.namelist() if n.startswith("xl/worksheets/sheet")]
            xml = "".join(z.read(n).decode("utf-8", "ignore") for n in nomes)
        alvo = letra(col_atend)
        for f1, sqref in re.findall(r"<(?:x14:)?formula1>(?:<xm:f>)?([^<]+).*?sqref>?([^<]*)<", xml, re.S):
            if re.search(r"\b%s\d" % alvo, sqref) and "!" in f1:
                import openpyxl
                wb = openpyxl.load_workbook(caminho, data_only=True)
                nome, faixa = f1.replace("$", "").split("!")
                vals = [c.value for linha in wb[nome][faixa] for c in linha if c.value]
                if vals:
                    return [str(v).strip() for v in vals]
    except Exception:
        pass
    return []


def ler_xlsx(caminho, mapa=None):
    import openpyxl
    wb = openpyxl.load_workbook(caminho, data_only=True)
    tabelas = []
    for ws in wb.worksheets:
        grade = [[("" if c.value is None else str(c.value).strip()) for c in linha]
                 for linha in ws.iter_rows(max_row=min(ws.max_row, 60))]
        cab, cols = None, {}
        for i, linha in enumerate(grade):
            achado = detectar_colunas(linha)
            if "req" in achado and len(achado) >= 2:
                cab, cols = i + 1, achado
                break
        if cab is None:
            continue
        criar = "just" not in cols
        if criar:
            cols["just"] = max(cols.values()) + 1
        linhas = []
        for linha in ws.iter_rows(min_row=cab + 1, max_row=ws.max_row):
            val = lambda p: ("" if p not in cols or cols[p] >= len(linha) or linha[cols[p]].value is None
                             else str(linha[cols[p]].value).strip())
            req = val("req")
            ident = val("id") or "L%d" % linha[0].row
            if req and (("id" not in cols) or val("id")):
                linhas.append((linha[0].row, ident, " ".join(req.split()), val("prio")))
        if linhas:
            t = Tabela(ws.title, cab, cols, linhas, rotulos_xlsx(caminho, ws.title, cols.get("atend", 0)))
            t.ref_xlsx, t.criar_just = True, criar
            tabelas.append(t)
    return tabelas


def ler_docx(caminho, mapa=None):
    import docx
    doc = docx.Document(caminho)
    tabelas = []
    for n, tb in enumerate(doc.tables):
        if len(tb.rows) < 2:
            continue
        cab, cols = None, {}
        for i, linha in enumerate(tb.rows[:5]):
            achado = detectar_colunas([c.text.strip() for c in linha.cells])
            if "req" in achado and len(achado) >= 2:
                cab, cols = i, achado
                break
        if cab is None:
            continue
        criar = "just" not in cols
        if criar:
            livres = [j for j in range(len(tb.columns)) if j not in cols.values()]
            cols["just"] = livres[-1] if livres else len(tb.columns)
            criar = not livres
        linhas = []
        for i in range(cab + 1, len(tb.rows)):
            cel = tb.rows[i].cells
            val = lambda p: cel[cols[p]].text.strip() if p in cols and cols[p] < len(cel) else ""
            req = val("req")
            if req and (("id" not in cols) or val("id")):
                linhas.append((i, val("id") or "L%d" % i, " ".join(req.split()), val("prio")))
        if linhas:
            t = Tabela(str(n), cab, cols, linhas, [])
            t.ref_xlsx, t.criar_just = False, criar
            tabelas.append(t)
    return tabelas


def ler(caminho, mapa=None):
    return ler_xlsx(caminho, mapa) if caminho.lower().endswith((".xlsx", ".xlsm")) else ler_docx(caminho, mapa)


# ---------------------------------------------------------------- escrita xlsx
def celula_xml(ref, estilo, texto):
    est = ' s="%s"' % estilo if estilo else ""
    if texto is None:
        return "<c r=\"%s\"%s/>" % (ref, est)
    esc = texto.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return "<c r=\"%s\"%s t=\"inlineStr\"><is><t xml:space=\"preserve\">%s</t></is></c>" % (ref, est, esc)


def estilo_de(linha_xml, col):
    m = re.search(r'<c r="%s\d+"[^>]*?\ss="(\d+)"' % letra(col), linha_xml)
    return m.group(1) if m else None


def gravar_celula(linha_xml, num, col, texto, estilo):
    ref = "%s%d" % (letra(col), num)
    nova = celula_xml(ref, estilo, texto)
    padrao = r'<c r="%s"[^>]*/>|<c r="%s"[^>]*>.*?</c>' % (ref, ref)
    if re.search(padrao, linha_xml, re.S):
        return re.sub(padrao, nova, linha_xml, flags=re.S)
    if linha_xml.endswith("/>"):
        return linha_xml[:-2] + ">" + nova + "</row>"
    return linha_xml.replace("</row>", nova + "</row>")


def ajustar_cols(xml, col, largura=110):
    novo = '<col min="%d" max="%d" width="%d" customWidth="1"/>' % (col + 1, col + 1, largura)
    m = re.search(r"<cols>(.*?)</cols>", xml, re.S)
    if not m:
        return xml.replace("<sheetData>", "<cols>%s</cols><sheetData>" % novo)
    saida, alvo = [], col + 1
    for c in re.findall(r"<col [^>]*/>", m.group(1)):
        lo = int(re.search(r'min="(\d+)"', c).group(1))
        hi = int(re.search(r'max="(\d+)"', c).group(1))
        if lo <= alvo <= hi:
            if lo < alvo:
                saida.append(re.sub(r'max="\d+"', 'max="%d"' % (alvo - 1), c))
            if hi > alvo:
                saida.append(re.sub(r'min="\d+"', 'min="%d"' % (alvo + 1), c))
        else:
            saida.append(c)
    saida.append(novo)
    return xml[:m.start()] + "<cols>" + "".join(saida) + "</cols>" + xml[m.end():]


def aplicar_xlsx(origem, destino, tabela, respostas, rotulos):
    import openpyxl
    wb = openpyxl.load_workbook(origem)
    aba = wb.sheetnames.index(tabela.ref) + 1
    alvo = "xl/worksheets/sheet%d.xml" % aba
    with zipfile.ZipFile(origem) as z:
        itens = [(i, z.read(i.filename)) for i in z.infolist()]

    c_at, c_ju = tabela.colunas["atend"], tabela.colunas["just"]
    c_pk = c_ju + 1 if any(r[2] for r in respostas.values()) else None
    porlinha = {num: (ident, prio) for num, ident, _, prio in tabela.linhas}

    def transformar(linha_xml):
        num = int(re.search(r'<row r="(\d+)"', linha_xml).group(1))
        if num == tabela.cabecalho:
            est = estilo_de(linha_xml, c_at)
            if tabela.criar_just:
                linha_xml = gravar_celula(linha_xml, num, c_ju, "JUSTIFICATIVA / CUSTOMIZAÇÃO NECESSÁRIA", est)
            if c_pk is not None:
                linha_xml = gravar_celula(linha_xml, num, c_pk, "PACKS SANKHYA", est)
            return linha_xml
        if num not in porlinha:
            return linha_xml
        ident = porlinha[num][0]
        if ident not in respostas:
            return linha_xml
        classe, just, packs = respostas[ident]
        est_at = estilo_de(linha_xml, c_at) or estilo_de(linha_xml, tabela.colunas.get("prio", c_at))
        est_ju = estilo_de(linha_xml, tabela.colunas.get("req", c_ju)) or est_at
        linha_xml = gravar_celula(linha_xml, num, c_at, rotulos[classe], est_at)
        linha_xml = gravar_celula(linha_xml, num, c_ju, just, est_ju)
        if c_pk is not None and packs:
            linha_xml = gravar_celula(linha_xml, num, c_pk, packs, est_ju)
        return linha_xml

    def ajustar(xml):
        ultima = c_ju if c_pk is None else c_pk
        xml = re.sub(r'\sspans="[^"]*"', "", xml)
        xml = re.sub(r'<dimension ref="([A-Z]+\d+):[A-Z]+(\d+)"/>',
                     lambda m: '<dimension ref="%s:%s%s"/>' % (m.group(1), letra(ultima), m.group(2)), xml)
        if tabela.criar_just:
            xml = ajustar_cols(xml, c_ju)
        if c_pk is not None:
            xml = ajustar_cols(xml, c_pk, 60)
        padrao = r'<row r="\d+"[^>]*/>|<row r="\d+".*?</row>'
        return re.sub(padrao, lambda m: transformar(m.group(0)), xml, flags=re.S)

    with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as saida:
        for info, conteudo in itens:
            if info.filename == alvo:
                conteudo = ajustar(conteudo.decode("utf-8")).encode("utf-8")
            saida.writestr(info, conteudo)


def aplicar_docx(origem, destino, tabela, respostas, rotulos):
    import copy
    import docx
    shutil.copy2(origem, destino)
    doc = docx.Document(destino)
    tb = doc.tables[int(tabela.ref)]
    c_at, c_ju = tabela.colunas["atend"], tabela.colunas["just"]

    def escrever(celula, texto, modelo):
        p = celula.paragraphs[0]
        for r in list(p.runs):
            r._element.getparent().remove(r._element)
        run = p.add_run(texto)
        if modelo is not None and modelo.runs:
            fonte = modelo.runs[0].font
            run.font.name, run.font.size = fonte.name, fonte.size
        return run

    if tabela.criar_just:
        grade = tb._tbl.tblGrid
        grade.append(copy.deepcopy(grade[-1]))
        for linha in tb.rows:
            ultima = linha._tr.tc_lst[-1]
            nova = copy.deepcopy(ultima)
            for par in nova.findall(".//{%s}p" % nova.nsmap["w"]):
                par.getparent().remove(par)
            nova.append(copy.deepcopy(ultima.findall("{%s}p" % ultima.nsmap["w"])[0]))
            ultima.addnext(nova)
        for linha in tb.rows:
            linha.cells[c_ju].text = ""
        tb.rows[tabela.cabecalho].cells[c_ju].text = "JUSTIFICATIVA / CUSTOMIZAÇÃO"

    for num, ident, _, _ in tabela.linhas:
        if ident not in respostas:
            continue
        classe, just = respostas[ident][:2]
        cel = tb.rows[num].cells
        escrever(cel[c_at], rotulos[classe], cel[tabela.colunas.get("req", c_at)].paragraphs[0])
        escrever(cel[c_ju], just, cel[tabela.colunas.get("req", c_ju)].paragraphs[0])
    doc.save(destino)


# ---------------------------------------------------------------- comandos
def escolher(tabelas, mapa):
    if mapa and "!" in mapa:
        ref = mapa.split("!")[0]
        for t in tabelas:
            if t.ref == ref:
                return t
    return max(tabelas, key=lambda t: len(t.linhas))


def cmd_scan(args):
    tabelas = ler(args.arquivo)
    if not tabelas:
        print("NENHUM BLOCO DE REQUISITOS DETECTADO - informe --map manualmente")
        return
    for t in tabelas:
        print("MAPA %s | requisitos=%d | criar_justificativa=%s" % (t.mapa(), len(t.linhas), t.criar_just))
        if t.rotulos:
            print("ROTULOS %s" % " | ".join(t.rotulos))


def cmd_extract(args):
    tabela = escolher(ler(args.arquivo), args.map)
    cache = [] if args.all else ler_cache()
    auto, pend = [], []
    for _, ident, req, prio in tabela.linhas:
        achado, escore = buscar_cache(cache, req) if cache else (None, 0.0)
        if achado:
            auto.append("%s\t%s\t%s" % (ident, achado[0], achado[1]))
        else:
            pend.append((ident, prio_curta(prio), req, escore))
    if auto:
        with open(args.auto, "w", encoding="utf-8") as fp:
            fp.write("\n".join(auto) + "\n")
    print("MAPA %s | total=%d | cache=%d | pendentes=%d" % (
        tabela.mapa(), len(tabela.linhas), len(auto), len(pend)))
    if tabela.rotulos:
        print("ROTULOS %s" % " | ".join(tabela.rotulos))
    for ident, prio, req, _ in pend:
        print("%s|%s|%s" % (ident, prio, req))


def cmd_apply(args):
    tabela = escolher(ler(args.arquivo), args.map)
    respostas = {}
    for caminho in args.respostas:
        with open(caminho, encoding="utf-8") as fp:
            for linha in fp:
                partes = linha.rstrip("\n").split("\t")
                if len(partes) >= 3 and partes[1].upper() in CLASSES:
                    packs = partes[3].strip() if len(partes) > 3 else ""
                    respostas[partes[0].strip()] = (partes[1].upper(), partes[2], packs)
    rotulos = dict(CLASSES)
    origem_rot = args.rotulos.split("|") if args.rotulos else tabela.rotulos
    if len(origem_rot) >= 3:
        for cod, valor in zip("TPN", origem_rot[:3]):
            rotulos[cod] = valor.strip()

    base, ext = os.path.splitext(args.arquivo)
    destino = args.out or (base + SUFIXO + ext)
    if ext.lower() in (".xlsx", ".xlsm"):
        aplicar_xlsx(args.arquivo, destino, tabela, respostas, rotulos)
    else:
        aplicar_docx(args.arquivo, destino, tabela, respostas, rotulos)

    faltando = [i for _, i, _, _ in tabela.linhas if i not in respostas]
    contagem = {c: sum(1 for v in respostas.values() if v[0] == c) for c in "TPN"}
    print("GERADO %s" % destino)
    print("ROTULOS %s" % " | ".join(rotulos[c] for c in "TPN"))
    print("T=%d P=%d N=%d | sem resposta=%d" % (contagem["T"], contagem["P"], contagem["N"], len(faltando)))
    if faltando:
        print("FALTAM %s" % ", ".join(faltando[:40]))
    obrig = [i for _, i, _, p in tabela.linhas
             if prio_curta(p) == "O" and respostas.get(i, ("T",))[0] != "T"]
    if obrig:
        print("RISCO obrigatorios nao-Total=%d: %s" % (len(obrig), ", ".join(obrig)))


def cmd_cache(args):
    tabela = escolher(ler(args.arquivo), args.map)
    texto = {ident: req for _, ident, req, _ in tabela.linhas}
    vistos = {norm(t[1]) for t in [(0, l.split("\t")[1], 0) for l in open(CACHE, encoding="utf-8")]} \
        if os.path.exists(CACHE) else set()
    novos = 0
    os.makedirs(os.path.dirname(CACHE), exist_ok=True)
    with open(CACHE, "a", encoding="utf-8") as saida:
        for caminho in args.respostas:
            with open(caminho, encoding="utf-8") as fp:
                for linha in fp:
                    partes = linha.rstrip("\n").split("\t")
                    if len(partes) < 3 or partes[1].upper() not in CLASSES:
                        continue
                    req = texto.get(partes[0].strip())
                    if not req or norm(req) in vistos:
                        continue
                    vistos.add(norm(req))
                    saida.write("%s\t%s\t%s\n" % (partes[1].upper(), req, partes[2]))
                    novos += 1
    print("CACHE +%d entradas" % novos)


def main():
    p = argparse.ArgumentParser(prog="rfp")
    sub = p.add_subparsers(dest="cmd")
    for nome in ("scan", "extract", "apply", "cache"):
        s = sub.add_parser(nome)
        s.add_argument("arquivo")
        s.add_argument("--map", default=None)
        if nome in ("apply", "cache"):
            s.add_argument("respostas", nargs="+")
        if nome == "extract":
            s.add_argument("--all", action="store_true")
            s.add_argument("--auto", default="auto.tsv")
        if nome == "apply":
            s.add_argument("--out", default=None)
            s.add_argument("--rotulos", default=None)
    args = p.parse_args()
    if not args.cmd:
        p.print_help()
        return
    {"scan": cmd_scan, "extract": cmd_extract, "apply": cmd_apply, "cache": cmd_cache}[args.cmd](args)


if __name__ == "__main__":
    main()
