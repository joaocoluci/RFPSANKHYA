---
name: rfp-preenchimento
description: >
  Preenche RFP/RFI de seleção de ERP respondendo o grau de atendimento do Sankhya (Total /
  Parcial / Não Atende) e a justificativa de cada requisito, em planilhas Excel ou documentos
  Word, com layout variável. Acionar para "preencher a RFP", "responder RFP", "matriz de
  requisitos do cliente", "checklist de aderência", "questionário de seleção de ERP",
  "responder o edital de ERP", ou quando o usuário apontar uma pasta/arquivo de RFP.
  Não usar para escopo de customização, orçamento de horas ou backlog.
---

# Preenchimento de RFP

Sempre via `scripts/rfp.py`. O modelo **nunca** abre a planilha/documento: o script extrai o
que falta responder e aplica as respostas preservando validações, agrupamentos e formatação.
O original nunca é alterado — a saída é `<nome> - RESPOSTA SANKHYA.<ext>`.

## Fluxo

```bash
P=~/.claude/skills/rfp-preenchimento/scripts/rfp.py
python $P extract "<arquivo>"                      # imprime MAPA, ROTULOS e só os pendentes
python $P apply   "<arquivo>" auto.tsv resp.tsv    # gera a cópia preenchida
python $P cache   "<arquivo>" resp.tsv             # alimenta o cache p/ próximas RFPs
```

1. `extract` — gera `auto.tsv` (respostas reaproveitadas do cache) e imprime `id|prioridade|requisito`
   só do que ficou pendente. Se vier `total=0` ou o bloco errado, rode `scan` e repasse `--map`.
2. Se houver pendentes, ler `references/sankhya-cobertura.md` e classificar cada um.
3. Escrever `resp.tsv` numa única chamada Write: `id⇥T|P|N⇥justificativa`.
4. `apply` — imprime contagem, itens sem resposta e a lista de **Obrigatórios que não ficaram
   Total** (risco de desclassificação). Não reabrir o arquivo para conferir.
5. `cache` — só depois do usuário validar as respostas.
6. Relatar: caminho gerado, contagem T/P/N por módulo quando útil, e o alerta de risco.

## Classificação

- **T (Total)** — nativo ou por parametrização padrão, sem desenvolvimento.
- **P (Parcial)** — existe com limitação, cobre parte, ou depende de customização, integração,
  módulo adicional ou produto complementar. É a resposta correta quando há caminho viável.
- **N (Não Atende)** — não existe e não compensa/não dá para customizar (fora do escopo do
  produto, depende de dado ou sistema de terceiro). Usar sem medo quando for o caso: inflar
  "Parcial" derruba a credibilidade da resposta inteira.

Justificativa: 1–2 frases, até ~220 caracteres, no formato *"<o que é nativo>. <o que falta e
qual customização/integração cobre>."* Não repetir o texto do requisito nem prometer prazo.

## Layouts fora do padrão

- Colunas são detectadas por regex no cabeçalho (ID, Requisito/Descrição, Prioridade,
  Atendimento/Aderência/Resposta, Justificativa/Observação). Se a coluna de justificativa não
  existir, o script cria uma à direita.
- Rótulos (`Total|Parcial|Não Atende`, `Atende|Parcial|Não`, `Sim|Parcial|Não`…) são lidos da
  validação de dados ou da aba de legenda. Se não detectar, passar `--rotulos "A|B|C"` no apply.
- Sem coluna de ID, a chave vira `L<linha>` — usar essa chave no `resp.tsv`.
- Vários blocos/abas de requisitos: rodar `scan`, depois um ciclo por bloco com `--map`.
- Word sem tabela (requisitos em prosa): o script não cobre — tratar manualmente com a skill `docx`.

## Regras de economia de contexto

- Nunca ler o arquivo com Read/openpyxl nem despejar a planilha no contexto.
- Nunca reabrir a saída para validar: `apply` já reporta contagem, faltantes e riscos.
- Um único Write para o `resp.tsv`; nada de editar item a item.
- O cache (`cache/respostas.tsv`) cresce a cada RFP e derruba o volume de pendentes das próximas.
