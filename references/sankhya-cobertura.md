# Mapa de cobertura Sankhya para RFP

Referência de classificação. Ler só quando `extract` retornar pendentes.
Formato: **domínio** — nativo (T) · gap típico (P/N).

## Financeiro
T: contas a pagar/receber, régua de cobrança, baixa por retorno bancário, conciliação OFX/CNAB,
boleto CNAB 240/400, remessa e pagamento em lote, fluxo de caixa projetado x realizado, limite de
crédito por parceiro e grupo, borderô/antecipação, cartões, multimoeda, multiempresa consolidado,
gestão orçamentária (orçado x realizado), DRE gerencial, centro de resultado e rateio.
P: tesouraria avançada, hedge, gestão de covenants, indicadores fora do DRE configurável.

## Fiscal
T: NF-e/NFC-e/NFS-e com contingência, CT-e, MDF-e, motor de cálculo por UF/NCM/CFOP/regime,
exceções fiscais, ST e benefícios, SPED Fiscal/Contribuições, EFD-Reinf, ECD, apuração de créditos,
retenções, importação de XML, Sintegra, comércio exterior (DI, adições, despesas aduaneiras),
validação fiscal prévia com bloqueio. Conformidade legal (inclusive reforma IBS/CBS) entra por release.
P: atualização automática de tabelas tributárias (depende de parceiro tributário), DCTF e calendário
de obrigações com alertas, NFS-e de município com leiaute próprio.

## Contábil
T: plano de contas parametrizável, roteiros de contabilização automática, balancete/BP/DRE por
empresa e centro de resultado, conciliação entre módulos, rateios, ECD, razão/diário, trilha de
auditoria, ativo imobilizado com depreciação, provisões via folha.
P: consolidação com plano de contas estrangeiro e norma contábil de outro país, checklist de
fechamento, workflow de aprovação de ajuste contábil.

## Vendas e CRM
T: orçamento e conversão em pedido, tabelas de preço por parceiro/negociação/região/segmento,
alçadas e workflow de aprovação, comissão por meta e faixa, reserva de estoque, bloqueio por
crédito, promoções/kits/descontos progressivos, contratos e faturamento recorrente, grupo econômico,
funil de CRM com etapas configuráveis, atividades e agenda, forecast por probabilidade, app de
força de vendas, importador de leads.
P: versionamento formal de proposta, hierarquia comercial além de vendedor/supervisor/gerente,
divisão do mesmo cliente entre vendedores por família/segmento, lead scoring, roteirização por mapa,
conectores de WhatsApp/e-mail marketing/chatbot, marketplace e portal de distribuidor, meta por
potencial de mercado, recomendação de mix por IA.

## Suprimentos
T: cadastro nacional/estrangeiro, cotação eletrônica com mapa comparativo, portal do fornecedor,
requisição→OC→recebimento→devolução, alçadas, lead time, contratos, sugestão de compras por
histórico/ponto de pedido/MRP, importação com incoterms e rateio no custo.
P: avaliação estruturada de fornecedor (score), tratamento de reclamações, contrato de câmbio.

## Manufatura
T: OP com apontamento de material/hora/operação, custo real (MP + MO + GGF), MRP, BOM com revisões
e alternativas, roteiro com tempos e recursos, rastreabilidade de lote, refugo com custo.
P: capacidade finita e sequenciamento (APS), MRP II completo, CEP e capabilidade, qualidade
estruturada (planos de inspeção, ação corretiva, 8D), manutenção preditiva, simulação de gargalos,
parâmetros de processo por OP, workflow de aprovação de OP, integração com CLP/sensores.

## Estoque e WMS
T: múltiplos locais, lote e validade com bloqueio, endereçamento, estoque mínimo/máximo/ponto de
pedido, inventário cíclico e anual com ajuste, consignação e demonstração com acerto, coletores e
código de barras, picking/conferência/expedição.
P: RFID, endereçamento dinâmico com regra automática de alocação, lote econômico, produto perigoso
(ONU/FISPQ).

## Logística
T: entrega e faturamento parciais, CT-e, MDF-e, logística reversa, custos de importação rateados,
integração nativa com o WMS.
P: cotação e contratação eletrônica de frete, etiqueta e rastreio por transportadora, roteirização,
SLA por cliente/região com alerta, OTIF e índice de avaria, agendamento com janela de horário,
avaliação de performance de transportadora, app de motorista/canhoto digital.

## Assistência técnica
T: OS com roteiro, técnico e apontamento, faturamento de serviço com NFS-e, remessa/retorno de
garantia e troca, remessa para demonstração com prazo, histórico único com o CRM.
P: base instalada (equipamento do cliente), cobertura e prazo de garantia, processo de recall,
base de conhecimento pesquisável, SLA com escalonamento, decisão de destino na logística reversa.

## Engenharia de produtos
T: hierarquia de grupos multinível, revisão de produto, estrutura alternativa, características e
anexos, similares/substitutos, custo por projeto, estrutura consumida direto pela produção.
P/N: PLM completo (ECO/ECR, workflow de engenharia), versionamento e visualização de arquivo CAD,
parâmetros dimensionais por cliente, aprovação formal de revisão de estrutura.

## BI e Analytics
T: dashboards padrão e livres, drill-down até o documento, rentabilidade, margem, alertas por regra
e agendamento, tabela dinâmica, exportação Excel e consumo por Power BI, BI mobile.
P: geração automática de insights por IA, modelos preditivos de demanda/preço/comportamento.

## Tecnologia
T: SaaS com SLA, web + apps, perfis e permissões granulares, backup com retenção e restauração,
API REST e SOAP, multiempresa/multifilial, auditoria com valor anterior e novo, 2FA/MFA, camada de
customização (Addon Studio / eventos programáveis) preservada nas atualizações, escalabilidade.
P: paridade total de rotinas no app, eliminação de intercompany na consolidação, LGPD no que toca
consentimento/portabilidade/exclusão sob demanda, conector pronto para Zapier/Make/Celonis/MuleSoft.

## Pricing
T: formação de preço por custo com markup e margem, tabela por segmento/canal/unidade, política de
desconto com alçada, margem em tempo real no pedido, histórico de preço por cliente, painel de margem.
P: markup por cliente/grupo com exceção aprovada, versionamento de markup com aprovação,
elasticidade de demanda, precificação dinâmica.
N: inteligência de preços de concorrência (dado não existe no ERP e depende de provedor externo).

## Módulos que exigem contratação à parte
Gestão de Pessoas/folha (provisões, eSocial), WMS, comércio exterior, e-commerce/B2B, manutenção de
ativos. Quando o requisito depende de um deles, classificar T e registrar a dependência na
justificativa — ou P, se além do módulo ainda houver gap funcional.
