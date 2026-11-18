"""Regera references/packs-sankhya.md a partir da planilha Horas por Produto - Engenharia de Valor.

Uso: python packs.py "<planilha>"
Mantem o cabecalho manual do .md (regras e mapa) ate a marca "## Catálogo completo".
"""
import os
import re
import sys

import openpyxl

DESTINO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "references", "packs-sankhya.md")
MARCA = "## Catálogo completo (packs ativos)\n"


def num(v):
    try:
        return ("%.1f" % float(v)).rstrip("0").rstrip(".")
    except (TypeError, ValueError):
        return "-"


def resumo(txt, nome, limite=320):
    txt = re.sub(r"\s+", " ", str(txt or "").replace("\xa0", " ")).strip()
    if txt.lower().startswith(nome.lower()):
        txt = txt[len(nome):]
    txt = re.sub(r"\s*/\s*-?\s*", "; ", txt).strip("; -")
    return (txt[:limite].rsplit(" ", 1)[0] + "…") if len(txt) > limite else txt


def catalogo(wb):
    saida, grupo, atual = [], None, None
    for r in wb["Produtos_Novo"].iter_rows(min_row=2, values_only=True):
        grupo = r[0] or grupo
        nome = str(r[1] or "").strip()
        if not nome or r[2] is False:
            continue
        if grupo != atual:
            atual = grupo
            saida.append("\n### %s\n\n| Nº | Pack | Horas | Setup | MRR | Depende de | Escopo |\n"
                         "|---|---|---|---|---|---|---|" % grupo)
        saida.append("| %s | %s | %s | %s | %s | %s | %s |" % (
            r[3] or "-", nome, num(r[8]), num(r[10]), num(r[11]),
            str(r[12] or "").strip() or "-", resumo(r[6], nome).replace("|", "/") or "-"))
    return saida


def faixas_usuario(wb):
    linhas = ["| Faixa de usuários | Usuário padrão | CNPJ | Pedido Web | Analytics |", "|---|---|---|---|---|"]
    for r in wb["Valor_Inicial"].iter_rows(min_row=2, max_row=6, values_only=True):
        linhas.append("| %s | %s | %s | %s | %s |" % (r[7], num(r[8]), num(r[9]), num(r[10]), num(r[11])))
    return linhas


def main():
    wb = openpyxl.load_workbook(sys.argv[1], data_only=True)
    with open(DESTINO, encoding="utf-8") as fp:
        cabecalho = fp.read().split(MARCA)[0] + MARCA
    itens = catalogo(wb)
    with open(DESTINO, "w", encoding="utf-8") as fp:
        fp.write(cabecalho + "\n".join(itens))
        fp.write("\n\n## Preço de lista por usuário/CNPJ (MRR, R$ cada)\n\n" + "\n".join(faixas_usuario(wb)) + "\n")
    print("%d packs -> %s" % (sum(1 for i in itens if i.startswith("| ")), os.path.normpath(DESTINO)))


if __name__ == "__main__":
    main()
