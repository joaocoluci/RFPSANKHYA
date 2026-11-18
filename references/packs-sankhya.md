# Packs Sankhya — base para indicar o PACK na RFP

Fonte: `Horas por Produto - Engenharia de Valor.xlsm` (aba Produtos_Novo + Valor_Inicial), gerado em 2026-10-26.
Planilha nova → regerar este arquivo (ver "Atualização" no fim do SKILL.md).

## Como usar

- Usar só quando o usuário pedir os packs; RFP padrão não leva pack.
- Pedido feito → listar **Nº + nome do pack** na coluna
  PACKS SANKHYA (4º campo do resp.tsv), não na justificativa. Ex.: `5339 Serviços - Pack 1 / Controle de Contratos`.
- Um requisito pode exigir mais de um pack; listar só os necessários, sem inflar.
- **Depende de** = usuário/pack pré-requisito (ex.: Contabilidade exige usuário Especialista Contabilidade). Incluir na indicação.
- **Horas** = implantação padrão do pack. Somar os packs escolhidos para estimar a implantação base
  (P03/Implantação). Customização, migração e integrações sob medida ficam fora dessa soma.
- **Setup/MRR** = preço de lista de referência (R$). Nunca preencher preço da RFP só com isso:
  desconto, faixa de usuários e pacote comercial mudam o valor. Usar para ordem de grandeza e
  avisar o usuário que o comercial precisa validar.
- Classificação:
  - pack do ERP (grupos 01–20) → **Total/Nativo**;
  - SOP (solução padronizada da Sankhya, com setup próprio) → **Parcial** ("produto complementar");
  - ecossistema de parceiro (grupos 21–37: PontoTel, Vixting, Mindsight, Espresso, ASIS, Neppo) → **Terceiro**
    quando a RFP tiver esse rótulo, senão **Parcial**.
- Item sem pack aqui → não inventar número; tratar como customização (Parcial) ou Não Atende.

## Mapa requisito típico → pack

| Requisito típico | Packs |
|---|---|
| Multiempresa, cadastros, usuários | 5837 Usuário BackOffice Avançado; 5640 Sankhya Master (admin) |
| Contas a pagar | 5302 Pagamentos - Pack 1 |
| Contas a receber, boleto, remessa/retorno | 5304 Recebimentos - Pack 1 |
| Rateio / centro de resultado | 5352 Pagamentos - Pack 2 / Centro de Resultado |
| Caixa, contas, conciliação manual/OFX | 5309 Caixas e Bancos - Pack 1 |
| Conciliação bancária automática | 5354 Caixas e Bancos - Pack 3 |
| API bancária (boleto/PIX/pagamentos) | 5984 Basic Pro (só recebimentos, 1.500 tx) · 6075 Standard (3.500 rec + 1.500 pag) · 6076 Professional · 6077 Enterprise — escolher pela volumetria mensal |
| Fluxo de caixa, inadimplência, DRE gerencial | 5312 Gerenciais - Pack 2 |
| Contabilidade, plano de contas, consolidação, ECD/ECF | 5377 Contabilidade + 5376 Contabilização (+ usuário 5839 Especialista Contabilidade) |
| Ativo imobilizado / depreciação | 5378 Controle Patrimonial |
| SPED Fiscal, Bloco H/K, Sintegra | 5316 Fiscal - Pack 1 |
| SPED Contribuições | 5317 Fiscal - Pack 2 |
| EFD-Reinf / retenções | 5318 Fiscal - Pack 3 |
| Captura de XML / manifestação MD-e | 5285 Compras - Pack 3 |
| Emissão NF-e de saída | 5294 Vendas - Pack 1 |
| Emissão NFS-e | 5297 Vendas - Pack 4 (ou 5935 SK Tax Pack 2, parceiro ASIS) |
| Regra tributária / reforma | 5930 SK Tax Pack 1 (parceiro ASIS) |
| Compras, requisição, aprovação | 5283 Compras - Pack 1; cotação 5284 Compras - Pack 2 |
| Restrição de lançamento por empresa/CR/natureza (segregação) | 5356 Central de Certificação |
| Contratos recorrentes, reajuste, faturamento de contrato | 5339 Serviços - Pack 1 / Controle de Contratos; SLA 5343; OS 5342 |
| Locação de bens/imobilizado com contrato | 6066 LOCAÇÃO DE BENS /SOP |
| Orçamento previsto x realizado | 5357 Controle Orçamentário e Metas Avançadas |
| BI self-service / IA | 5855 Analytics SK; 5388 Editor de Dashboard |
| Acesso a banco para BI/integração externa | 5925 Sankhya DataLink Access Pack (leitura/DDL) · 6019 DataLink Build Pack (escrita) |
| Integrações genéricas | 6064 PLATAFORMA DE INTEGRAÇÃO /SOP |
| Workflow / BPM | 5361 Sankhya Flow |
| Cloud | 6010 Saas (cloud) Pack |
| Suporte estendido | 5989 24x7 · 5990 Premium · 6073 24x7 + TAM · 5988/6072 SLA reduzido |
| Folha / RH / eSocial | 5381 Pessoal - Pack 2 + 5985 Configurações Folha + 5540 e-Social; 5382 Gestão de Pessoas + e 5383 Pessoas + App opcionais |
| Ponto eletrônico | PontoTel (grupo 21, parceiro) |
| Admissão digital / assinatura | Vixting (grupo 22) · SK Sign (grupo 36) |
| Despesas de viagem / adiantamentos | 30 SK Despesas (Espresso) |
| Régua de cobrança WhatsApp | 32 Régua de Cobrança (Neppo) |

Inconsistências na planilha de origem: Nº 5294 repetido (Vendas - Pack 1 e Fórmula de
Comissionamento); Nº 5370 repetido (GPD APP e Sankhya GPD App). Confirmar antes de citar.

## Catálogo completo (packs ativos)

### 01 - BACK ESSENCIAL

| Nº | Pack | Horas | Setup | MRR | Depende de | Escopo |
|---|---|---|---|---|---|---|
| 5294 | Vendas - Pack 1 | 24.7 | 609.8 | 303.8 | - | Registro dos orçamentos de vendas - Registro e controle dos pedidos de vendas pendentes - Controla limite de crédito dos clientes - Controla limite de desconto dos produtos - Realização do faturamento parcial ou corte de itens dos pedidos de venda - Registro e emissão da NFe de vendas, consignações, entregas futuras,… |
| 5320 | Varejo - Pack 1 / PDV Web | 2 | 483.2 | 237.9 | Especialista Varejo | PDV Online, embarcado na solução SankhyaOm; - Emissão de CF-e (SAT-SP; MFE-CE); - Emissão de NFC-e; - Portal de Caixa. Obs.: é necessário ter o Certificado Digital modelo A1. |
| 5353 | Recebimentos - Pack 4 / Análise de Crédito | 10.8 | 386.6 | 193.9 | - | Permite definir regras para a análise automática de crédito dos clientes, incluindo a sugestão do limite de crédito a ser concedido por meio de uma fórmula configurável. - Podem incluir informações do balanço ou balancete de seus clientes (patrimônio líquido, direitos, obrigações, caixa, endividamento, etc.),… |
| 5336 | Gestão de Veículos - Pack 1 | 28 | 386.6 | 192.7 | Especialista Distribuição | Atacado; Distribuidor - Gestão de Veículos - Pack 1 - Permite o lançamento dos abastecimentos, controlando a quilometragem rodada - Controla a substituição de peças - Permite a criação de relatórios que alertam sobre a necessidade de troca de óleo e; ou envio do Veículo para a Revisão - Controla o horário de Saída e… |
| 5356 | Central de Certificação | 20 | 386.6 | 191.3 | Especialista Contabilidade | Estipular limitações de lançamentos no sistema, a partir da configuração de permissões ou proibições, tanto para Java como para o Delphi. - As limitações de lançamentos serão configuradas por instâncias como, Centro de Resultado, Conta bancária, Local, Natureza, Parceiro, TOP ou pares pré-programados de instâncias… |
| 5283 | Compras - Pack 1 | 12.6 | 369.8 | 181 | - | Reposição do estoque em função do mínimo e máximo - Compra com base em pedidos de venda - Compra em função de solicitações ou requisições internas - Controle dos pedidos de compras e pedidos de vendas pendentes - Registro do orçamento de compra - Registro dos pedidos de compra - Aprovação de compras - Controle do… |
| 5312 | Gerenciais - Pack 2 | 14.8 | 348.4 | 170.7 | - | Análise das despesas e receitas - Comparação das despesas e receitas de determinados grupos de naturezas em períodos diferentes - Análise do fluxo de caixa - Análise do índice de inadimplência - Análise do desempenho das cobranças - Análise do ponto de equilíbrio - Análise do ciclo operacional financeiro e NCG -… |
| 5284 | Compras - Pack 2 / Cotação | 5.7 | 309.3 | 152.6 | - | Lançamento da cotação de compra para análise automática e aprovação - Envio da cotação de compra para os Fornecedores - B2B. |
| 5374 | Estocagem - Pack 2 / Controle de EPI | 32.4 | 289.9 | 142.2 | - | Ferramenta de controle de estoque de equipamentos de proteção individual que são fornecidas para os empregados executarem suas atividades na empresa em que trabalham - Controla a data de validade dos equipamentos - Emite, através de formatadores de relatórios, termo de Responsabilidade, Termo de Devolução, Relatório… |
| 5296 | Vendas - Pack 3 / Controle de Atendimento | 2.7 | 259 | 128 | - | Agendamento e controle dos contatos. |
| 5354 | Caixas e Bancos - Pack 3 / Conciliação Bancária Automática | 16.2 | 226.6 | 116.4 | - | - |
| 5310 | Caixas e Bancos - Pack 2 / Conciliação Cartões de Crédito/Débito | 1.8 | 226.6 | 116.4 | - | Conciliação automática de cartões de crédito; débito. |
| 5322 | Varejo - Pack 3 / Cupom Fiscal, Nota Fiscal E Sankhya Checkout | 0 | 235.3 | 116.4 | Checkout | Varejo - Pack 3; Cupom Fiscal e Nota Fiscal - Notas Fiscais Eletrônica (NFC-e) e Cupom Fiscal Eletrônico(CF-e); SAT. |
| 5292 | Estocagem - Pack 1 | 13.9 | 225.2 | 112.5 | - | Extrato de todas as operações de entrada e saída de estoque - Controle dos produtos por local de estoque para agilizar o processo de entradas e de saídas - Registro das transferências de produtos entre diferentes locais e; ou empresas - Controle do estoque considerando critérios como tamanho, cor, lote, data de… |
| 5307 | Recebimentos - Pack 3 / Recebimento via TEF | 4.5 | 203.9 | 103.4 | - | Trata-se do recebimento de títulos via integração com as operadoras de cartões. |
| 5352 | Pagamentos - Pack 2 / Centro de Resultado | 6.5 | 193.3 | 97 | - | Um Centro de Resultado pode ser definido como um subconjunto ou parte de uma empresa que pode ter suas Receitas e Despesas analisadas separadamente, possibilitando avaliar seu desempenho e compará-lo ao da empresa como um todo. |
| 5297 | Vendas - Pack 4 / NFSe | 2.5 | 168.1 | 85.3 | - | Emissão da NFS-e (Obs.: é necessário ter o Certificado Digital modelo A1). Cidades Homologadas: |
| 5304 | Recebimentos - Pack 1 | 20.2 | 165.9 | 84 | - | Provisão do contas a receber - Contas a receber; - Formação de duplicatas; - Boleto Rápido: Automação via integração por API de boletos e bolepix. Para os Bancos que possuem essa automação junto ao ERP Sankhya, haverá cobrança adicional feita à parte da mensalidade Sankhya;- Remessa e Retorno Bancário via EDI: Para os… |
| 5295 | Vendas - Pack 2 / Metas Simplificadas | 4 | 168.1 | 84 | - | Define e estabelece metas de vendas mensal por vendedor, produto ou serviço, grupo de produto ou serviço. - Define e estabelece metas de vendas por períodos pré-definidos e conjunto de critérios - Acompanhamento das metas x realizado. |
| 5291 | Precificação - Pack 1 | 11.9 | 168.1 | 82.8 | - | Apuração do custo Contábil dos produtos e serviços - Apuração do custo de reposição dos produtos, considerando acréscimos, descontos, tributos, fretes, carga, descarga, etc. - Apuração dos gastos fixos da empresa e dos gastos variáveis incidentes nas vendas dos produtos ou serviços - Apuração do custo gerencial dos… |
| 5309 | Caixas e Bancos - Pack 1 | 6.5 | 139.5 | 72.4 | - | Controle de contas (bancária, caixa, adiantamento, fundos, etc.) - Movimentações financeiras entre contas da empresa - Fechamento de caixa - Conciliação manual de cartões de crédito; débito - Conciliação bancária manual - Conciliação do extrato bancário - Conciliação do extrato bancário através do arquivo OFX. |
| 5313 | Gerenciais - Pack 1 | 16.5 | 134.5 | 67.2 | - | Compras - Sugestão de compra em função da análise do giro dos produtos - Analisa as vendas perdidas por falta de produtos em estoque (ruptura) antes de comprar - Análise do fluxo de caixa para decisões de compras - Análise do perfil de compras por grupo de produtos - Análise do perfil de compras por marca - Análise do… |
| 5302 | Pagamentos - Pack 1 | 7.3 | 98.7 | 53 | - | Provisão do contas a pagar - Contas a pagar - Emissão de cheques - Controle de cheque pré-datados - Pagamento de fornecedores via integração de arquivos com o banco - Baixa de titulos a pagar. |
| 5285 | Compras - Pack 3 / MD-e/DF-e | 4 | 84 | 41.4 | - | Manifesto do Destinatário de nota fiscal eletrônica - MD-e; DF-e. |

### 02 - ATACADO

| Nº | Pack | Horas | Setup | MRR | Depende de | Escopo |
|---|---|---|---|---|---|---|
| 5328 | Atacado / Distribuidor - Pack 5 / Crédito Flex | 8 | 444.6 | 219.8 | Especialista Distribuição | Atacado; Distribuidor - Pack 5 - Controle de Crédito Flex dos vendedores. |
| 5337 | Cálculo de Frete - Pack 1 | 32.4 | 386.6 | 192.7 | Especialista Distribuição | Atacado; Distribuidor - Cálculo de Frete - Pack 1 - Definição de transportadora padrão - Identificação da transportadora preferencial para o parceiro - Definição de rotas considerando, tempo, peso, percentual, frete mínimo e distância - Criação de fórmulas e eventos para o cálculo de frete - Cálculo de frete… |
| 5324 | Atacado / Distribuidor - Pack 1 | 9.7 | 251.3 | 126.7 | Especialista Distribuição | Definição da sequência de entrega por região - Criação e formação da ordem de carga - Mapa de separação da ordem de carga - Acerto da ordem de carga. |
| 5326 | Atacado / Distribuidor - Pack 3 / CTe | 4 | 289.9 | 142.2 | Especialista Distribuição | Atacado; Distribuidor - Pack 3 - Emissão do Conhecimento de Transporte Eletrônico - CTe. |
| 5325 | Atacado / Distribuidor - Pack 2 / MDFe | 4 | 84 | 41.4 | Especialista Distribuição | Atacado; Distribuidor - Pack 2 - Emissão do Manifesto Eletrônico de Documentos Fiscais - MDFe. |
| 5729 | Compras - Pack 5 / Gestão de Verbas | 30 | 258.6 | 290.9 | - | Cadastro de contratos de verbas recebidas; concedidas; - Impressão de contratos de verbas; - Comunicação com parceiros (envio do contrato por e-mail); - Integração das parcelas com financeiro; - Destinação de verbas (Financeiro, Rebaixa de Preços, Rebaixa de Custos); - Painel de Gerência de Verbas (consulta status… |

### 03 - LIVROS FISCAIS

| Nº | Pack | Horas | Setup | MRR | Depende de | Escopo |
|---|---|---|---|---|---|---|
| 5316 | Fiscal - Pack 1 / Livro e SPED Fiscal | 37.8 | 722.8 | 356.9 | - | SPED Fiscal - Bloco H - inventário - SPED Fiscal - Bloco K - Registro de Controle da Produção e do Estoque - SINTEGRA - Geração do arquivo CAT 42 (SP). |
| 5317 | Fiscal - Pack 2 / SPED Contribuições | 27 | 168.1 | 78.9 | - | SPED Contribuições - Registro 0500 - Plano de contas contábil - SPED Contribuições - Registro 0600 - Centro de custo. |
| 5318 | Fiscal - Pack 3 / EFD Reinf | 22.5 | 252.1 | 121.5 | - | Geração do EFD - Reinf - Escrituração Fiscal Digital de Retenções e Outras Informações Fiscais. |

### 04 - CONTABILIDADE

| Nº | Pack | Horas | Setup | MRR | Depende de | Escopo |
|---|---|---|---|---|---|---|
| 5376 | Contabilização | 130 | 502.6 | 219.8 | Especialista Contabilidade | Principais funcionalidades: -Possibilidade de agendamento automático da contabilização com alta performance -Contabilização automática dos lançamentos operacionais -Contabilização em múltiplas partidas atendendo o comunicado Técnico CTG 2001 R1 e a RESOLUÇÃO CFC Nº 1299; 10 -Contabilização do Ajuste a Valor Presente… |
| 5377 | Contabilidade | 70 | 1353.1 | 664.6 | Especialista Contabilidade | Principais funcionalidades disponíveis: - Compartilhamento do Plano de Contas entre empresas - Estrutura do Plano de Contas flexível e configurável - Gerenciamento e controle de Lotes Contábeis - Zeramento das contas de Resultado - Consolidação de Empresas - Lançamentos Contábeis com múltiplas partidas e com… |

### 05 - CONTROLE PATRIMONIAL

| Nº | Pack | Horas | Setup | MRR | Depende de | Escopo |
|---|---|---|---|---|---|---|
| 5378 | Controle Patrimonial | 20 | 1008.5 | 496.5 | - | Principais funcionalidades: - Transferência de Bem - Desmembramento de Bem - Vinculação de Bem - Desvinculação de Bem - Alteração de Código Bem. |

### 06 - PRODUCAO BASICO

| Nº | Pack | Horas | Setup | MRR | Depende de | Escopo |
|---|---|---|---|---|---|---|
| 5812 | Indústria Pack 1.1 - Quality Pack | 40 | 588.3 | 290.3 | Especialista Manufatura | Indústria - Quality Pack Descritivo: O pack de qualidade oferece um controle dos Produtos Acabados e Matérias-Primas em fábricas, que utilizam padrões de classificação, análise de características, coleta e registro de amostras. Este processo resulta em laudos que aprovam ou reprovam etapas do processo produtivo ou a… |
| 5813 | Indústria Pack 1.2 - Advanced Pack | 40 | 588.3 | 290.3 | Especialista Manufatura | Indústria - Advanced Pack Descrição: O pack "Avançado" oferece controle de custos indiretos associados à fabricação de produtos transformados e gerenciamento eficaz de subprodutos, como sucata e refugos. Priorizando o apontamento detalhado de perdas e controle de desvio da produção, ele reduz desperdícios e otimiza a… |
| 5811 | Indústria Pack 1 - Starter Pack | 80 | 1176.6 | 580.5 | Ponto de Apontamento | Indústria - Starter Pack Descritivo: O Starter Pack é fundamental para um processo produtivo eficaz, oferecendo funcionalidades essenciais. Assegura o controle do estoque de produção e a rastreabilidade de matéria-prima (MP) e produto acabado (PA). Inclui a produção de produtos intermediários (PI), apontamento da… |

### 07 - PRODUCAO AVANCADO

| Nº | Pack | Horas | Setup | MRR | Depende de | Escopo |
|---|---|---|---|---|---|---|
| 5814 | Indústria Pack 1.3 - Outsourcing Pack | 40 | 588.3 | 290.3 | Especialista Manufatura | Indústria - Outsourcing Pack Descrição: O Pack Terceirização oferece soluções para produção terceirizada e para terceiros, garantindo eficiência e controle do estoque de materiais, seja na remessa ou no retorno dos itens. Produção: -Produção Terceirizada (Por Terceiros; Em Terceiros); -Produção para Terceiros (De… |
| 5815 | Indústria Pack 1.4 - Specific Pack | 80 | 1176.6 | 580.5 | Especialista Manufatura | Indústria - Specific Pack Descritivo: Este pack permite o uso de recursos da Produção Conjunta onde existe o aparecimento de diversos produtos a partir da mesma matéria-prima, também é possível efetuar cadastros e movimentos que alimentam e permitem o uso do indicador de OEE. Atividades do processo produtivo podem ser… |
| 5331 | Indústria Pack 2 / MRP I | 90 | 1008.5 | 502.9 | Especialista Manufatura | Industria - Pack 2; MRP I - Com o opcional Pack 2, que inclui a funcionalidade MRP I (Planejamento das Necessidades de Material) os gestores de produção passam a contar com auxílio do sistema no momento da execução de seus planejamentos, obtendo assim de forma rápida e fácil sua real necessidade de produção e… |
| 5332 | Indústria Pack 3 / Programação de O.P | 110 | 1344.7 | 667.1 | Especialista Manufatura | Indústria - Pack 3; Programação de O.P Com este pack, é possível programar (sequenciar) as Ordens de Produção automaticamente no gráfico de Gantt, com base na capacidade dos Centros de Trabalho e quantidade de produtos a serem fabricados conforme o MPS (Plano Mestre de Produção). Além da sugestão automática de… |
| 5334 | Indústria Pack 4 / Ponto de Apontamento | 30 | 193.3 | 97 | Ponto de Apontamento | Indústria - Pack 4; Ponto de Apontamento Rotina independente e simplificada para realização de apontamentos da produção. Essa rotina é exclusiva para realização de apontamentos de produção, diferente da tela "Operações de Produção" existente no pack 1, que além do apontamento também possui outros recursos, tais como:… |

### 08 - CONTRATOS

| Nº | Pack | Horas | Setup | MRR | Depende de | Escopo |
|---|---|---|---|---|---|---|
| 5339 | Serviços - Pack 1 / Controle de Contratos | 120 | 579.9 | 289.6 | Especialista Serviços | Recurso que permite o controle financeiro dos Parceiros que têm algum vínculo com determinadas empresas - Controla-se neste contrato, o valor cobrado por produtos e serviços, o tipo de atualização financeira (tipo de pagamento, tipo de financeiro, tipo de contrato, faturamento, provisões financeiras, etc.) e o… |
| 5343 | Serviços - Pack 2 / SLA | 20 | 1014.9 | 502.9 | Especialista Serviços | O objetivo principal do módulo é possibilitar ao parceiro informações para gerenciamento dos acordos de SLA firmados com seus clientes de forma a garantir, em termos contratuais, características de qualidade, eficiência e eficácia de produtos e serviços disponibilizados - Possibilita formalizar acordos estabelecidos… |
| 5342 | Serviços - Pack 4 / Ordem de Serviço | 160 | 289.9 | 142.2 | Especialista Serviços | Este módulo é feito para usuários de Ordem de Serviço no sistema. OBS: Toda a configuração para a utilização de contratos e ordens de serviço continua sendo feita no módulo de contratos. Porém o uso das rotinas relacionadas a OS podem ser feitas a partir deste novo módulo. |

### 09 - WMS

| Nº | Pack | Horas | Setup | MRR | Depende de | Escopo |
|---|---|---|---|---|---|---|
| 5335 | WMS - Pack 2 | 400 | 4202 | 2084.2 | Total Cross - Usuário Coletor WMS Android | Atacado; Distribuidor - WMS - Pack 2 - Warehouse Management Systems (Sistemas de Gerenciamento de Armazém), é um módulo de gestão de armazéns que permite melhorar substancialmente os processos de armazenamento. Possibilita administrar e rastrear toda a cadeia produtiva, que vai desde o recebimento da mercadoria até a… |

### 10 - CONTROLE ORCAMENTARIO

| Nº | Pack | Horas | Setup | MRR | Depende de | Escopo |
|---|---|---|---|---|---|---|
| 5357 | Controle Orçamentário e Metas Avançadas | 100 | 1008.5 | 493.9 | - | Controle do orçamento das despesas - Acompanhamento do previsto x realizado - Orçamentos das despesas, natureza - Planejamento das metas por natureza - Limitação automática das despesas em função do orçamento - Acompanhamento de metas por Empresa, Vendedor, Produto, Grupo de Produtos; Filiais etc - Planejamento de… |
| 5358 | Gestão de Verbas Orçamentárias | 20 | 966.5 | 475.8 | Usuário Gestão de Verbas | Ter um maior controle sobre as solicitações de Suplementação, Transferência e Antecipação de saldo de metas - Rotinas; Liberação de Antecipação, Suplementação e Transferência de Recursos Orçamentários - Avançado; Transferência de Saldo - Nas Centrais de Atendimento e na Movimentação Financeira, ao lançar uma Nota;… |

### 11 - PLANEJAMENTO ORCAMENTARIO

| Nº | Pack | Horas | Setup | MRR | Depende de | Escopo |
|---|---|---|---|---|---|---|
| - | PCO - ANALYTICS | 0 | - | - | - | - |

### 12 - ANALYTICS

| Nº | Pack | Horas | Setup | MRR | Depende de | Escopo |
|---|---|---|---|---|---|---|
| 5855 | Analytics SK | 0 | 1575 | 1081.4 | - | O usuário Sankhya Analytics AI permite explorar e visualizar dados do EIP de forma independente com inteligência artificial e Self Service BI, através da criação de dashboards no-code e interação com a BIA (IA Sankhya) para obter respostas rápidas. O Sankhya Analytics AI democratiza o acesso aos dados, agiliza… |

### 13 - PERSONALIZAÇÃO

| Nº | Pack | Horas | Setup | MRR | Depende de | Escopo |
|---|---|---|---|---|---|---|
| 5391 | Plataforma de Personalização | 0 | 1008.5 | 470.6 | Usuário BackOffice Avançado (EVO POR USUÁRIO) | Ferramenta para a criação e manutenção de telas, personalizando de acordo com a necessidade do usuário. |
| 5388 | Editor de Dashboard | 0 | 1008.5 | 470.6 | Usuário BackOffice Avançado (EVO POR USUÁRIO) | O componente Editor de Dashboard do SankhyaW é uma ferramenta extremamente poderosa. Com ela o usuário pode realizar uma análise completa das informações que o sistema provê, bem como informações de banco de dados de terceiros. Além de flexível, o Dashboard apresenta as informações de forma inteligente, permitindo uma… |

### 14 - BIA COMPOSE

| Nº | Pack | Horas | Setup | MRR | Depende de | Escopo |
|---|---|---|---|---|---|---|
| 6003 | BIA COMPOSE | 0 | 0 | 878.8 | - | O Agente Bia Compose é uma funcionalidade da BIA, o copiloto de gestão da Sankhya, desenvolvido para auxiliar usuários na geração de telas personalizadas dentro do ERP Sankhya. A ferramenta processa comandos em linguagem natural (prompts) para gerar sugestões de estruturas telas personalizadas, que devem ser validados… |

### 15 - BIA CONHECIMENTO

| Nº | Pack | Horas | Setup | MRR | Depende de | Escopo |
|---|---|---|---|---|---|---|
| 6004 | BIA BASE DE CONHECIMENTO | 0 | 0 | 1097.4 | - | O Agente de Base de Conhecimento é uma funcionalidade da BIA que permite às empresas indexar documentos e arquivos próprios (como políticas, manuais e procedimentos) para criar bases de conhecimento customizadas. A ferramenta possibilita que usuários autorizados realizem consultas em linguagem natural. A BIA utiliza o… |

### 16 - GPD

| Nº | Pack | Horas | Setup | MRR | Depende de | Escopo |
|---|---|---|---|---|---|---|
| 5359 | Gestão Estratégica - GPD | 120 | 3865.9 | 1808.8 | Usuário BackOffice Avançado (EVO POR USUÁRIO) | O módulo "Gestão Estratégica" é uma poderosa ferramenta de gestão que tem como objetivo final, a execução do planejamento estratégico da empresa de forma estruturada e disseminada por toda a organização em seus diversos níveis gerenciais e operacionais por meio da definição, desdobramento e acompanhamento das metas e… |
| 5360 | Controle do Plano de Ação | 66.7 | 289.9 | 142.2 | Usuário BackOffice Avançado (EVO POR USUÁRIO) | - |

### 17 - SANKHYA FLOW

| Nº | Pack | Horas | Setup | MRR | Depende de | Escopo |
|---|---|---|---|---|---|---|
| 5361 | Sankhya Flow | 30 | 193.3 | 95.7 | Usuário BackOffice Avançado (EVO POR USUÁRIO) | O SankhyaFlow é um módulo de automatização e gerenciamento de processos de negócios que visa aumentar a produtividade das equipes de trabalho além de tornar simples e eficiente o monitoramento e acompanhamento dos processos de sua empresa - É capaz de modelar processos graficamente; definir suas regras de execução;… |

### 18 - SANKHYA FOLHA

| Nº | Pack | Horas | Setup | MRR | Depende de | Escopo |
|---|---|---|---|---|---|---|
| 5381 | Pessoal - Pack 2 / Pessoal + | 120 | 672.3 | 497.3 | Usuários Pessoal | Simulação de Cálculo de Folha de Pagamento -Cálculo de Folha de Pagamento -Sugestões de cálculo -Gerenciador de Folhas -Integração com Financeiro Sankhya -Integração com Contabilidade Sankhya -Geração -Envio -Acompanhamento -Análises -Central de Benefícios -Lançamento de Benefícios -Cálculo de Benefícios. |
| 5540 | Pessoal - Pack 8 / e-Social | 8 | 1008.5 | 372.9 | - | Esse produto é responsável por extrair, enviar e consultar as informações que compõe a obrigação fiscal denominada e-Social. O sistema de mensageira como é comumente chamado, na prática faz o envio dos Lotes com os eventos e consulta o ambiente para ter acesso aos Números de Recibo e os Retornos com o consolidado do… |
| 5382 | Pessoal - Pack 3 / Gestão de Pessoas + | 8 | 305.6 | 248.6 | Usuários Gestão de Pessoas | Pessoal - Pack 3; Gestão Pessoas + -Análises sobre sua equipe -Lançamento de requisições para liderados -Aprovação de requisições de liderados -Consulta de Férias -Análises de toda a empresa -Lançamento de requisições para toda a empresa -Aprovação de requisições de toda a empresa -Lançamento de requisições diversas… |
| 5383 | Pessoal - Pack 4 / Pessoas + App | 4 | 212.3 | 124 | Usuários Pessoas mais App | Mobilidade e comodidade para digitalizar documentos e atestados - Acesso facilitado as Informações referentes a apuração da Folha de pagamento. - Apoio a Liderança: aprovação de requisições, análises, notificações de requisições de liderados. |
| 5985 | Pessoal - Pack Configurações Folha | 0 | 0 | 494.3 | Pessoal - Pack 2 / Pessoal + | Pacote de configurações do Sankhya Folha. |

### 19 - LMS

| Nº | Pack | Horas | Setup | MRR | Depende de | Escopo |
|---|---|---|---|---|---|---|
| 6021 | LMS -  PLATAFORMA DE GESTÃO DE APRENDIZAGEM | 0 | - | - | - | ANEXO DE CONDIÇÕES ESPECÍFICAS – MÓDULO LMS (SANKHYA LMS) Este documento constitui parte integrante e acessória da Proposta Comercial e; ou Contrato de Licença de Uso de Software (“Contrato Principal”) firmado entre as Partes. As disposições aqui contidas regem especificamente a contratação e o uso do módulo Sankhya… |

### 20 - ARMAZENS GERAIS

| Nº | Pack | Horas | Setup | MRR | Depende de | Escopo |
|---|---|---|---|---|---|---|
| 5556 | Armazéns Gerais - Pack 1 | 200 | 3025.5 | 1499.8 | Especialista Agro | O módulo permite o controle das movimentações do armazém de forma sequencial e integrada, garantindo segurança, fluidez e agilidade nas operações, atendendo a clientes do segmento Agro que prestam serviços de armazenagem de grãos. Entre as soluções disponibilizadas para isso, estão: Gestão de Contratos Definição do… |
| 5747 | Armazéns Gerais - Pack 2 - Comercialização de Grãos | 100 | 1512.7 | 1499.8 | Especialista Agro | O módulo é um recurso complementar ao Armazéns Gerais; W, que viabiliza a gestão e operacionalização da comercialização de grãos integrada ao sistema, com recursos para registro dos contratos, controle de portaria, pesagem, classificação e das movimentações relacionadas ao processo. Entre as soluções disponibilizadas… |

### 21 - PONTOTEL

| Nº | Pack | Horas | Setup | MRR | Depende de | Escopo |
|---|---|---|---|---|---|---|
| 5980 | Pacote 2 - PONTOTEL | 0 | 0 | 0 | - | Contempla os módulos Registro de ponto, Cálculos e tratamento e Redução de riscos; Segurança no registro. Inclui Medidas de Segurança (Registro por Biometria Facial, Geolocalização, Verificador de Manipulação de GPS, Cerca Virtual, Bloqueio por Rede de Internet (IP). |
| 5979 | Pacote 1 - PONTOTEL | 0 | 0 | 0 | - | Contempla os módulos Registro de ponto e Cálculos e tratamento.Inclui BatePonto APP e Web (Senha, Prova de VIda, Voz, Recaptcha), cálculo automatizado dos apontamentos, mas sem necessidade de gestão de solicitações. |
| 5981 | Pacote 3 - PONTOTEL | 0 | 0 | 0 | - | Contempla os módulos Registro de ponto, Cálculos e tratamento, Redução de riscos; Segurança no registro e Gestão de ponto participativa. Inclui módulo de Gestão Participativa (Solicitações de Ajustes, Dispensas, Alterações de Escalas, Inclusão de HE, Conferências, Aprovação de Folha, Travamento Bilateral) |
| 5982 | Pacote 4 - PONTOTEL | 0 | 0 | 0 | - | Contempla os módulos Registro de ponto, Cálculos e tratamento, Redução de riscos; Segurança no registro, Gestão de ponto participativa e Controle de Custos. Inclui módulo de Controle de Custos (Monitoramento em Tempo Real, Planejamento de Escalas, HE e BH, Acompanhamento de HE, Notificações de HE e atrasos). |
| 5983 | Pacote 5 - PONTOTEL | 0 | 0 | 0 | - | Contempla os módulos Registro de ponto, Cálculos e tratamento, Redução de riscos; Segurança no registro, Gestão de ponto participativa, Controle de Custos e Timesheet. Inclui todas as funcionalidades da Pontotel; Planejamento e Registro de Atividades em Tempo Real, Calendário para Acompanhamento e Correção e… |

### 22 - VIXTING

| Nº | Pack | Horas | Setup | MRR | Depende de | Escopo |
|---|---|---|---|---|---|---|
| 5956 | PACK 1 - Admissão Vlow (Vixting) | 0 | 0 | 0 | - | Admissão Digital. Na admissão, automatiza desde o recolhimento e análise de documentos de admissão até a integração com a folha (Sankhya) via API. |
| 5957 | PACK 2 - Mesa de Validação (Vixting) | 0 | 0 | 0 | - | Analistas (BPO) que realizam manualmente a conferência e dupla checagem de documentos enviados por candidatos. |
| 5958 | PACK 3 - Integração com ATS (Vixting) | 0 | 0 | 0 | - | Conexão entre a Admissão Digital e um sistema de recrutamento e seleção de candidatos (ATS). |
| 5959 | PACK 4 - Integração com Folha de Pagamento (Vixting) | 0 | 0 | 0 | - | Conexão entre a Admissão Digital e um sistema de Folha de Pagamento. |
| 5960 | PACK 5 - Integração com Assinatura Digital (Vixting) | 0 | 0 | 0 | - | Conexão entre a Admissão Digital e um sistema de Assinatura Eletrônica próprio da Vixting. |

### 23 - MINDISIGHT

| Nº | Pack | Horas | Setup | MRR | Depende de | Escopo |
|---|---|---|---|---|---|---|
| 6033 | MINDSIGHT COMPLETO ESSENCIAL | 0 | - | - | - | Reúne recrutamento inteligente, pesquisas e engajamento, performance, recompensas e People Analytics em uma única plataforma orientada por dados. Desde a atração de talentos, utilizamos predições precisas de performance e assessments avançados (como o Mindmatch), integrados a portais de vagas, para agilizar triagens e… |
| 6034 | MINDSIGHT COMPLETO AVANÇADO | 0 | - | - | - | Reúne recrutamento inteligente, pesquisas e engajamento, performance, recompensas e People Analytics em uma única plataforma orientada por dados. Desde a atração de talentos, utilizamos predições precisas de performance e assessments avançados (como o Mindmatch), integrados a portais de vagas, para agilizar triagens e… |
| 6035 | MINDSIGHT COMPLETO PREMIUM AI | 0 | - | - | - | Reúne recrutamento inteligente, pesquisas e engajamento, performance, recompensas e People Analytics em uma única plataforma orientada por dados. Desde a atração de talentos, utilizamos predições precisas de performance e assessments avançados (como o Mindmatch), integrados a portais de vagas, para agilizar triagens e… |
| 6036 | MINDSIGHT DESEMPENHO E ENGAJAMENTO ESSENCIAL | 0 | - | - | - | Integra pesquisas e engajamento, performance e recompensas e People Analytics em uma única solução, permitindo compreender percepções da equipe ao longo do tempo, conduzir avaliações de desempenho justas e consistentes e consolidar dados de pessoas para decisões estratégicas. Com análises acionáveis, inteligência… |
| 6037 | MINDSIGHT DESEMPENHO E ENGAJAMENTO AVANÇADO | 0 | - | - | - | Integra pesquisas e engajamento, performance e recompensas e People Analytics em uma única solução, permitindo compreender percepções da equipe ao longo do tempo, conduzir avaliações de desempenho justas e consistentes e consolidar dados de pessoas para decisões estratégicas. Com análises acionáveis, inteligência… |
| 6038 | MINDSIGHT DESEMPENHO E ENGAJAMENTO PREMIUM AI | 0 | - | - | - | Integra pesquisas e engajamento, performance e recompensas e People Analytics em uma única solução, permitindo compreender percepções da equipe ao longo do tempo, conduzir avaliações de desempenho justas e consistentes e consolidar dados de pessoas para decisões estratégicas. Com análises acionáveis, inteligência… |
| 6039 | MINDSIGHT RECRUTAMENTO E SELEÇÃO ESSENCIAL | 0 | - | - | - | Desenvolvida para oferecer predições precisas de performance desde a triagem, o que resulta em seleções mais eficientes. Com uma gestão de vagas que utiliza assessments avançados (Mindmatch) e indicadores para otimizar performance de recrutadores, a plataforma também tem integração com portais de vagas, agilizando a… |
| 6040 | MINDSIGHT RECRUTAMENTO E SELEÇÃO AVANÇADO | 0 | - | - | - | Desenvolvida para oferecer predições precisas de performance desde a triagem, o que resulta em seleções mais eficientes. Com uma gestão de vagas que utiliza assessments avançados (Mindmatch) e indicadores para otimizar performance de recrutadores, a plataforma também tem integração com portais de vagas, agilizando a… |
| 6041 | MINDSIGHT RECRUTAMENTO E SELEÇÃO PREMIUM AI | 0 | - | - | - | Desenvolvida para oferecer predições precisas de performance desde a triagem, o que resulta em seleções mais eficientes. Com uma gestão de vagas que utiliza assessments avançados (Mindmatch) e indicadores para otimizar performance de recrutadores, a plataforma também tem integração com portais de vagas, agilizando a… |

### 30 - SK DESPESAS (ESPRESSO)

| Nº | Pack | Horas | Setup | MRR | Depende de | Escopo |
|---|---|---|---|---|---|---|
| 5927 | Gestão de Despesas (Despesas, Adiantamentos e Títulos) | 0 | 0 | 0 | - | Sankhya Despesas Gestão de Despesas (Despesas, Adiantamentos e Títulos). O Sankhya Despesas é a solução que digitaliza o processo de prestação de contas, reembolsos e adiantamento realizados aos colaboradores, com app mobile e conta digital integrados. - Registro de despesas por categoria; natureza. - Adiantamentos;… |

### 31 - SK TAX (ASIS)

| Nº | Pack | Horas | Setup | MRR | Depende de | Escopo |
|---|---|---|---|---|---|---|
| 5930 | Pack 1 - Consulta e monitoramento de regra tributária | 0 | 0 | 0 | - | Verificação e Revisão de regra tributária do ICMS em lote durante a etapa de configuração do sistema, por meio de arquivos XML disponibilizados pela Licenciada, que será a única responsável por quaisquer decisões ou ações tomadas com base nas informações obtidas no uso da funcionalidade (Tela "Assistente de Melhores… |
| 5935 | Pack 2 - NFS-e | 0 | 0 | 0 | - | Nota Fiscal de Serviço Eletrônica (NFS-e) Realização de captura de Notas Fiscais Eletrônicas de Serviços (NFS-e) de Serviços Tomados, nos municípios onde existe o monitoramento da Asis. Para funcionamento pleno da solução, a Licenciada deverá, quando necessário, fornecer credenciais de acesso (login, senha,… |

### 32 - REGUA COBRANÇA (NEPPO)

| Nº | Pack | Horas | Setup | MRR | Depende de | Escopo |
|---|---|---|---|---|---|---|
| 5987 | Whatsapp na Régua de Cobrança - Plano 1 | 0 | 0 | 1148 | - | Plano 1: 500 notificações. R$1,95 por notificação extra.A Régua de Cobrança da Sankhya, ao integrar-se com a plataforma Neppo, visa aprimorar a eficiência e a eficácia dos processos de cobrança das empresas. Essa integração permite a automação de comunicações com clientes por meio do WhatsApp, facilitando o envio de… |
| 5991 | Whatsapp na Régua de Cobrança - Plano 2 | 0 | 0 | 1548 | - | Plano 2: 1.000 notificações. R$1,31 por notificação extra. A Régua de Cobrança da Sankhya, ao integrar-se com a plataforma Neppo, visa aprimorar a eficiência e a eficácia dos processos de cobrança das empresas. Essa integração permite a automação de comunicações com clientes por meio do WhatsApp, facilitando o envio… |
| 5992 | Whatsapp na Régua de Cobrança - Plano 3 | 0 | 0 | 2747 | - | Plano 3: 2.500 notificações. R$0,93 por notificação extra. A Régua de Cobrança da Sankhya, ao integrar-se com a plataforma Neppo, visa aprimorar a eficiência e a eficácia dos processos de cobrança das empresas. Essa integração permite a automação de comunicações com clientes por meio do WhatsApp, facilitando o envio… |
| 5993 | Whatsapp na Régua de Cobrança - Plano 4 | 0 | 0 | 3947 | - | Plano 4: 4.000 notificações. R$0,84 por notificação extra. &nbsp; A Régua de Cobrança da Sankhya, ao integrar-se com a plataforma Neppo, visa aprimorar a eficiência e a eficácia dos processos de cobrança das empresas. Essa integração permite a automação de comunicações com clientes por meio do WhatsApp, facilitando o… |
| 5994 | Whatsapp na Régua de Cobrança - Plano 5 | 0 | 0 | 5546 | - | Plano 5: 6.000 notificações. R$0,79 por notificação extra. A Régua de Cobrança da Sankhya, ao integrar-se com a plataforma Neppo, visa aprimorar a eficiência e a eficácia dos processos de cobrança das empresas. Essa integração permite a automação de comunicações com clientes por meio do WhatsApp, facilitando o envio… |
| 5995 | Whatsapp na Régua de Cobrança - Plano 6 | 0 | 0 | 8745 | - | Plano 6:10.000 notificações. R$0,74 por notificação extra. A Régua de Cobrança da Sankhya, ao integrar-se com a plataforma Neppo, visa aprimorar a eficiência e a eficácia dos processos de cobrança das empresas. Essa integração permite a automação de comunicações com clientes por meio do WhatsApp, facilitando o envio… |
| 5996 | Whatsapp na Régua de Cobrança - Plano Enterprise | 0 | 0 | 16478 | - | Plano 7: 20.000 notificações. R$0,70 por notificação. A Régua de Cobrança da Sankhya, ao integrar-se com a plataforma Neppo, visa aprimorar a eficiência e a eficácia dos processos de cobrança das empresas. Essa integração permite a automação de comunicações com clientes por meio do WhatsApp, facilitando o envio de… |

### 36 - SK SIGN (VIXTING)

| Nº | Pack | Horas | Setup | MRR | Depende de | Escopo |
|---|---|---|---|---|---|---|
| - | SKSign - START | 0 | 0 | 0 | - | - |
| - | SKSign - PRO | 0 | 0 | 0 | - | - |
| - | SKSign - GROWTH | 0 | 0 | 0 | - | - |
| 6017 | SkSign - GROWTH | 0 | - | - | - | SANKHYA SIGN - PLANO GROWTH 1- Finalidade de (i) gerenciar documentos online de forma colaborativa entre a equipe, (ii) solicitar assinaturas via e-mail pela Plataforma, (iii) assinar documentos eletronicamente por celulares e tablets (iv) enviar lembretes via SMS e WhatsApp e (v) compartilhar documentos pelo Google… |
| 6016 | SkSign - PRO | 0 | - | - | - | SANKHYA SIGN - PLANO PRO 1- Finalidade de (i) gerenciar documentos online de forma colaborativa entre a equipe, (ii) solicitar assinaturas via e-mail pela Plataforma, (iii) assinar documentos eletronicamente por celulares e tablets (iv) enviar lembretes via SMS e WhatsApp e (v) compartilhar documentos pelo Google… |
| 6015 | SkSign - START | 0 | - | - | - | SANKHYA SIGN - PLANO START 1- Finalidade de (i) gerenciar documentos online de forma colaborativa entre a equipe, (ii) solicitar assinaturas via e-mail pela Plataforma, (iii) assinar documentos eletronicamente por celulares e tablets (iv) enviar lembretes via SMS e WhatsApp e (v) compartilhar documentos pelo Google… |

### 37 - SK BENEFICIOS (ESPRESSO)

| Nº | Pack | Horas | Setup | MRR | Depende de | Escopo |
|---|---|---|---|---|---|---|
| - | SK BENEFICIOS + MENSALIDADE SVA | 0 | - | - | - | - |
| 6023 | Sankhya Benefícios | 0 | - | - | - | 1 - O Sankhya Benefícios é uma solução digital na modalidade Software as a Service (SaaS), oferecida pela Espresso Controle de Despesas Ltda. (“Espresso”), destinada à gestão e disponibilização de benefícios corporativos (como vale alimentação, refeição, mobilidade, cultura, entretenimento, home office, educação,… |
| 6028 | SK Benefícios + Mensalidade SVA | 0 | - | - | - | 1 - O Sankhya Benefícios é uma solução digital na modalidade Software as a Service (SaaS), oferecida pela Espresso Controle de Despesas Ltda. (“Espresso”), destinada à gestão e disponibilização de benefícios corporativos (como vale alimentação, refeição, mobilidade, cultura, entretenimento, home office, educação,… |
| - | SANKHYA BENEFICIOS - ESPRESSO | 0 | - | - | - | - |

### 99 - FIT

| Nº | Pack | Horas | Setup | MRR | Depende de | Escopo |
|---|---|---|---|---|---|---|
| 5370 | GPD APP | 0 | 191.7 | 115 | - | - |
| 5335 | Total Cross - Usuário Coletor WMS Android | 0 | 235.1 | 222.2 | WMS - Pack 2 | O Coletor WMS é a solução completa para a gestão eficiente dos armazéns. Foi projetado para simplificar e aprimorar todas as operações logísticas. Conta com recursos avançados de rastreamento de estoque, alocação inteligente de espaço e integração perfeita com o ERP Sankhya. Oferece controle total sobre o ciclo de… |
| 5721 | PDV Web | 0 | 255.6 | 174.2 | Varejo - Pack 1 / PDV Web | Utilizado para frente de loja com exeção de movimentações off line, mas permite negociação nas condições de pagamento. |
| 5322 | Checkout | 18 | 255.6 | 174.2 | Varejo - Pack 3 / Cupom Fiscal, Nota Fiscal E Sankhya Checkout | Utilizado para frente de loja com movimentações off line, sem possiblidade de negociação das condições de pagamento. |
| 5395 | FormViewer | 0 | 255.6 | 174.2 | - | Utilizado para visualização de telas personalizadas. |
| 5504 | DashViewer | 0 | 255.6 | 174.2 | - | Utilizado para visualização de dashboard's personalizados. |
| 5350 | Pedido Web | 0 | 255.6 | 174.2 | - | Utilizado para vendas externas com limitação de emissão de nota fiscal e lançamento de devolução. |
| 5334 | Ponto de Apontamento | 0 | 255.6 | 174.2 | Indústria Pack 1 - Starter Pack | Permite fazer apontamento de produção. |
| 5379 | Tv Corporativa | 0 | 255.6 | 174.2 | - | Permite visualização de informações específicas em uma TV específica. |
| 5367 | Sankhya Vision app | 0 | 191.7 | 115 | - | Permite acesso de dashboard personalizado atraves de aplicativo para smartphones |
| 5370 | Sankhya GPD App | 1 | 168.1 | 82.8 | Sankhya GPD App | Este é um aplicativo exclusivo para clientes da Sankhya Gestão de Negócios, desenvolvido para o controle e acompanhamento de metas. Com o app, a Sankhya da mais um passo para transformar a gestão das empresas brasileiras. Acreditamos que uma organização saudável e forte faz mais que resultados, ela faz bem para a vida… |
| 5608 | Sankhya Fila de Conferência App | 0 | 191.7 | 115 | - | CONFERÊNCIA POR COLETOR APP; W |
| 5911 | ANALYTICS VIEWER SK | 0 | 255.6 | 337.9 | - | Serviços de uso da Inteligência ArtificialOs valores estabelecidos neste contrato; proposta remuneram exclusivamente a prestação de serviço e; ou licenciamento ao CLIENTE. Os custos decorrentes da utilização de serviços de Inteligência Artificial (como a API do Google Gemini por exemplo, ou outra fornecedora) são… |
| 5362 | Lista de Tarefas | 0 | 255.6 | 174.2 | Lista de Tarefas | Operacionaliza a lista de flows pendentes. |

### 99 - USU

| Nº | Pack | Horas | Setup | MRR | Depende de | Escopo |
|---|---|---|---|---|---|---|
| 5551 | Acesso Simultâneo (Venda EVO) | 0 | 1237.3 | 452.5 | - | - |

### 99 - USUARIO

| Nº | Pack | Horas | Setup | MRR | Depende de | Escopo |
|---|---|---|---|---|---|---|
| - | Sankhya Ok App | 0 | 191.7 | 115 | - | Aplicativo para liberação de limites mobile, permitindo ao gestor a análise e liberação de eventos comerciais e financeiros, como atraso, desconto, limite de crédito, dentre outros, com exceção dos eventos de liberação orçamentária. |

### SERV

| Nº | Pack | Horas | Setup | MRR | Depende de | Escopo |
|---|---|---|---|---|---|---|
| - | Customização / Add-ons | 0 | 0 | 0 | Usuário BackOffice Avançado (EVO POR USUÁRIO) | - |

### SERVICOS

| Nº | Pack | Horas | Setup | MRR | Depende de | Escopo |
|---|---|---|---|---|---|---|
| 5898 | Relatórios Personalizados | 0 | 0 | 0 | Usuário BackOffice Avançado (EVO POR USUÁRIO) | - |
| 5294 | Personalização/Fórmula de Comissionamento | 0 | 0 | 0 | Usuário BackOffice Avançado (EVO POR USUÁRIO) | - |
| 5291 | Personalização/Fórmula de Precificação | 0 | 0 | 0 | Usuário BackOffice Avançado (EVO POR USUÁRIO) | - |

### SOP

| Nº | Pack | Horas | Setup | MRR | Depende de | Escopo |
|---|---|---|---|---|---|---|
| 6059 | INTEGRAÇÃO - RECEITA AGRO /SOP | 40 | 2500 | 1500 | - | O SOP Integração Receita Agro é uma solução de integração desenvolvida especialmente para empresas que comercializam agrotóxicos. O objetivo é simplificar e agilizar o processo de emissão de receituários agronômicos, tornando-o totalmente compatível com a legislação vigente. Veja: O que é um receituário agronômico? O… |
| 6060 | INTEGRAÇÃO - HUB COTAÇÕES MED /SOP | 120 | 3500 | 4500 | - | O SOP INTEGRAÇÃO - HUB COTAÇÕES MED; SOP é um módulo do ERP Sankhya que automatiza a participação da empresa em processos de cotação de compras hospitalares. Em vez de acessar manualmente plataformas externas de compras, o sistema faz tudo isso de forma automática, direto no ERP. Fluxo principal O sistema monitora as… |
| 6061 | INTEGRAÇÃO - HUB CONCILIAÇÃO CARD /SOP | 40 | 5000 | 2000 | - | O SOP Conciliadora tem como objetivo integrar as vendas, pagamentos, cancelamentos e taxas de PV com o Parceiro Conciliadora, permitindo a baixa e conciliação das vendas de cartão de crédito do Sankhya. As etapas de configuração, que são essenciais para viabilizar o processo de integração e garantir a correta… |
| 6063 | CONTROLE DE LICITAÇÃO /SOP | 120 | 3500 | 3000 | - | O SOP Contrato de Licitação foi desenvolvido para empresas que atuam com licitações públicas e precisam otimizar o controle de editais, propostas e contratos. Ele centraliza dados essenciais e automatiza processos, reduzindo o risco de erros manuais. Atende equipes responsáveis por cadastrar e acompanhar editais,… |
| 6064 | PLATAFORMA DE INTEGRAÇÃO /SOP | 24 | 2500 | 1000 | - | O SOP Plataforma de Integração oferece recursos avançados de integração para softwares de gestão empresarial. Ele permite automatizar processos e conectar diferentes sistemas, aumentando a eficiência e a produtividade das empresas. A última versão apresentou diversas melhorias e funcionalidades importantes. A seguir,… |
| 6068 | CONTROLE DE QUALIDADE /SOP | 80 | 4000 | 3000 | - | O SOP Controle de Qualidade fornece uma solução integrada para gerenciar e garantir a conformidade e a qualidade dos processos internos e externos relacionados aos produtos e fornecedores. O SOP atua diretamente no acompanhamento, validação e auditoria contínua dos processos críticos que afetam a qualidade e… |
| 6066 | LOCAÇÃO DE BENS /SOP | 120 | 10000 | 4500 | - | O SOP de Contrato de Locação oferece recursos para o controle de todo o ciclo da locação de produtos e imobilizados, da proposta ao faturamento. Faz a gestão de contratos, reajustes, equipamentos, operadores e regras comerciais, atendendo a múltiplos segmentos. Veja os principais recursos: Controle de locação de itens… |
| 6056 | INTEGRAÇÃO - HUBSOFT /SOP | 80 | 10000 | 4000 | - | O SOP Integração HubSoft fornece soluções Integradas para Gestão de Patrimônio e Finanças. É abrangente e inovadora para otimizar a gestão do patrimônio e das finanças de sua empresa. Nossas soluções visam proporcionar maior eficiência e controle por meio de uma variedade de funcionalidades especializadas. Abaixo,… |
| 6069 | MOVIMENTO AUTOMÁTICO /SOP | 60 | 17000 | 3500 | - | O SOP Movimento Automático oferece uma solução personalizável para automatizar o processo de localização de estoque, atendendo às necessidades específicas de cada venda. Com ele, é possível gerar movimentos tanto para atender a requisitos fiscais obrigatórios quanto para otimizar a gestão empresarial, tudo a partir de… |
| 6058 | INTEGRAÇÃO - TRANSFEERA /SOP | 32 | 5000 | 1500 | - | O SOP Transfeera oferece uma aceleração na integração de pagamentos das viagens do TMS efetuando o pagamento via PIX através da integração da API; Aqui estão alguns pontos gerais sobre o que você pode esperar ao usar a Transfeera: Pagamentos e Transferências: Transfeera facilita pagamentos e transferências de dinheiro… |
| 6055 | DISTMED /SOP | 120 | 9500 | 9000 | - | - |
| 6054 | LOGÍSTICA - YMS /SOP | 100 | 10000 | 3500 | - | O SOP YMS é uma solução destinada ao controle de portaria, gestão de acesso, pesagem e fluxo de veículos e produtos, com foco na automação dos processos operacionais e na confiabilidade das informações. A solução integra portaria, logística, recebimento e expedição, conectando-se aos sistemas corporativos e às… |
| 6070 | FICHA DE CHEQUES /SOP | 40 | 3500 | 1000 | - | Controle das operações de cheque utilizando o conceito de lote. ● Impressão automática de recibos ● Integração com o financeiro nati ● Baixas e estornos utilizando as regras nativas do Sankhya ● Rastreamento do cheque ● Controle de pagamento e recebimento ● Digitação do cheque ● Controle de pagamento e recebimento… |
| 6052 | INTEGRAÇÃO - WMS (DELAGE) /SOP | 60 | 3500 | 3000 | - | ABAIXO DESCRITIVO RESUMIDO DAS FUNCIONALIDADES DO SOP OBJETO DESTA PROPOSTA O SOP INTEGRAÇÃO - WMS (DELAGE); SOP é um módulo de integração entre o EIP Sankhya e sistemas de gerenciamento de armazém (WMS), especificamente o Delage. Principais funcionalidades: Compras Quando uma nota de compra é lançada no Sankhya, o… |
| 6065 | ASSISTÊNCIA TÉCNICA /SOP | 120 | 6000 | 3000 | - | O SOP Assistência Técnica é um fluxo estruturado que padroniza o atendimento técnico a parceiros, desde o primeiro contato até o faturamento. Ele oferece rastreabilidade completa das Ordens de Serviço (O.S.), garantindo controle sobre os atendimentos, peças e serviços utilizados, e validações em cada etapa do… |
| 6062 | INTEGRAÇÃO - TINTOMÉTRICO /SOP | 80 | 10000 | 3000 | - | O SOP Tintométrico foi desenvolvido para atender às necessidades de empresas que trabalham com a venda de tintas personalizadas. Ele oferece uma solução robusta e integrada ao ERP, que permite o controle completo da operação — desde a seleção da fórmula até a entrega final do produto ao cliente. Por meio de uma… |
| 6067 | PULSE/SOP | 24 | 1500 | 1000 | - | Funcionalidades do sistema SOP Pulse, um add-on paraanálise gerencial do DRE integrado ao Sankhya. Construção e Configuração do DRE- Estrutura hierárquica personalizável - Definição de contas sintéticas e analíticas- Criação de contas totalizadoras e cálculos entre contas- Integração com dados financeiros e contábeis-… |
| 7009 | LOGISTICA - TMS FIT/SOP | 170 | 5000 | 2000 | - | A suíte de Logística, com o SOP TMS FIT, é uma solução completa para otimizar suas operações logísticas. Veja abaixo os recursos disponíveis: Gerenciamento de risco com registro e controle de aprovação manual (não há integração) Ordem de coleta; entrega com importação do XML das notas do tomador de serviço Gestão… |

### SOP 01 - TMS

| Nº | Pack | Horas | Setup | MRR | Depende de | Escopo |
|---|---|---|---|---|---|---|
| 6057 | INTEGRAÇÃO - MULTI CTE /SOP | 40 | 5000 | 2000 | - | 1. Apresentação da Solução: A integração entre o ERP Sankhya e o portal MultiCTe foi desenvolvida para automatizar o processo de busca e registro de documentos fiscais (CTE e MDFE) emitidos com Certificado Digital de Transporte, promovendo maior eficiência nas operações fiscais e financeiras da sua empresa. Integrar… |
| 6047 | LOGÍSTICA - TMS /SOP | 170 | 15000 | 4000 | - | A suíte de Logística, com o SOP TMS, é uma solução completa para otimizar suas operações logísticas. Veja abaixo os recursos disponíveis:Tabela de preço de frete (a receber e a pagar):Para tomador de serviço; Para o prestador de serviço (motoristas); Composição do preço por: peso, quantidade de entregas, cubagem e… |
| 6053 | LOGÍSTICA - SCANBOT /SOP | 24 | 1500 | 1000 | - | 1. Apresentação da Solução A integração entre o ERP e o Scanbot é definida pela integração de API interna do ERP com uma plataforma de integração e envio de link de um formulário para preenchimento dos dados de cadastros e anexos da CNH e CRLV do veículo efetuando o OCR do Cadastro 2. Objetivo Acelerar o cadastro de… |

### SOP 02 - GESTAO FROTAS

| Nº | Pack | Horas | Setup | MRR | Depende de | Escopo |
|---|---|---|---|---|---|---|
| 6049 | LOGÍSTICA - APP ABASTECIMENTO /SOP/LOG | 24 | 1000 | 450 | - | Aplicativo com foco em gestão operacional de frotas e controle logístico, exclusivo para empresas que usam o SOP Gestão de Frotas.Controle de Veículos e Placas:Permite gerenciar uma lista de veículos cadastrados; O usuário pode selecionar um veículo (placa) e navegar por funcionalidades associadas.Gestão de… |
| 6048 | LOGÍSTICA - GESTÃO DE FROTAS /SOP/LOG | 70 | 15000 | 4000 | - | A suíte de Logística, com o SOP Gestão de Frotas, é uma solução para a gestão completa da sua frota. Veja abaixo os recursos oferecidos: Gestão da portaria, com o controle do movimento de pessoas e veículos (entrada e saída) Gestão de multas e autuações por motoristas e veículos,&nbsp; integrado ao financeiro Gestão… |
| 6050 | LOGÍSTICA - APP CHECKLIST /SOP | 24 | 1000 | 450 | - | 1. Apresentação da Solução O SOP Logística APP de Checklist atende a necessidade de efetuar a “Inspeção da frota” integrado ao módulo de “Gestão de Frotas”, criando checklists para registro documental de itens com defeito apontados pelo inspetor de frotas. 2. Objetivo Acelerar documentar o processo de inspeção da… |
| 6051 | LOGÍSTICA - APP PNEUS /SOP | 24 | 1000 | 450 | - | 1. Apresentação da Solução O SOP Logística APP PNEUS atende a necessidade de efetuar a “Movimentação de Pneus” integrado ao módulo de “Gestão de Frotas”, atualizando as posições de estoque dos pneus aplicados nos veículos efetuando a baixa e movimentações. Execução de inspeção de sulcos, medição de pressão (Manual) e… |
| 7010 | LOGISTICA - GESTÃO DE FROTAS FIT/SOP | 70 | 5000 | 2000 | - | A suíte de Logística, com o SOP Gestão de Frotas FIT, é uma solução para a gestão completa da sua frota. Veja abaixo os recursos oferecidos: Gestão da portaria, com o controle do movimento de pessoas e veículos (entrada e saída) Gestão de multas e autuações por motoristas e veículos, integrado ao financeiro Gestão de… |

### SOP 03 - COMEX

| Nº | Pack | Horas | Setup | MRR | Depende de | Escopo |
|---|---|---|---|---|---|---|
| 6043 | IMPEX - IMPORTAÇÃO /SOP | 90 | 10000 | 4400 | - | O SOP ImpEx - Importação foi desenvolvido para apoiar empresas que realizam operações internacionais, oferecendo uma gestão estruturada e integrada de todo o processo de importação. A solução centraliza informações, organiza etapas críticas e assegura maior rastreabilidade, eficiência operacional e redução de custos.… |
| 6045 | IMPEX - EXPORTAÇÃO /SOP | 90 | 10000 | 4400 | - | Implantação de rotina de proforma; Configuração dos produtos de exportação. A partir da criação do pedido de vendas, o sistema segue as rotinas nativas de venda, sendo assim é de responsabilidade da equipe de Backoffice de vendas. Contratos Cambiais Este módulo melhora a gestão financeira dos contratos cambiais de… |
| 5938 | IMPEX - CONTRATOS CAMBIAIS /SOP | 40 | 3500 | 1500 | - | - |

### SOP FIT

| Nº | Pack | Horas | Setup | MRR | Depende de | Escopo |
|---|---|---|---|---|---|---|
| 6044 | IMPEX FIT - IMPORTAÇÃO /SOP | 90 | 10000 | 2000 | - | O SOP ImpEx FIT - Importação foi desenvolvido para apoiar empresas que realizam operações internacionais, oferecendo uma gestão estruturada e integrada de todo o processo de importação. A solução centraliza informações, organiza etapas críticas e assegura maior rastreabilidade, eficiência operacional e redução de… |

### SUPORTE

| Nº | Pack | Horas | Setup | MRR | Depende de | Escopo |
|---|---|---|---|---|---|---|
| 5988 | SUPORTE SLA REDUZIDO | 0 | 0 | 0 | - | Horário de Atendimento: Segunda a Sexta-feira, das 7h às 19h (exceto feriados), em regime de horas úteis; Nível de Serviço: 85% (oitenta e cinco por cento) das demandas cobertas pelos prazos propostos; Canais de Acionamento: Chat e Formulário (online); Metas de Tempo de Resposta e Solução (Em Horas Úteis):… |
| 5989 | SUPORTE 24 X 7 | 0 | 0 | 0 | - | Horário de Atendimento: 24 horas por dia, 7 dias por semana (inclusive feriados), em regime de horas corridas para atendimento inicial e soluções paliativas; Nível de Serviço: 85% (oitenta e cinco por cento) das demandas cobertas pelos prazos propostos; Canais de Acionamento: Telefone, Chat e Formulário; Metas de… |
| 5990 | SUPORTE PREMIUM | 0 | 0 | 0 | - | Horário de Atendimento: 24 horas por dia, 7 dias por semana (inclusive feriados), em regime de horas corridas para atendimento inicial e soluções paliativas; Nível de Serviço: 85% (oitenta e cinco por cento) das demandas cobertas pelos prazos propostos; Canais de Acionamento: Telefone, Chat e Formulário; Metas de… |
| 6073 | SUPORTE 24 X 7 + TAM | 0 | 0 | 0 | - | Horário de Atendimento: 24 horas por dia, 7 dias por semana (inclusive feriados), em regime de horas corridas para atendimento inicial e soluções paliativas; Nível de Serviço: 85% (oitenta e cinco por cento) das demandas cobertas pelos prazos propostos; Canais de Acionamento: Telefone, Chat e Formulário; Metas de… |
| 6072 | SUPORTE SLA REDUZIDO + TAM | 0 | 0 | 0 | - | Horário de Atendimento: Segunda a Sexta-feira, das 7h às 19h (exceto feriados), em regime de horas úteis; Nível de Serviço: 85% (oitenta e cinco por cento) das demandas cobertas pelos prazos propostos; Canais de Acionamento: Chat e Formulário (online); Metas de Tempo de Resposta e Solução (Em Horas Úteis):… |

### Z

| Nº | Pack | Horas | Setup | MRR | Depende de | Escopo |
|---|---|---|---|---|---|---|
| 5640 | Sankhya Master | 0 | 1237.3 | 452.5 | - | Acesso aos módulos ACESSO WEB SERVICES; W, ANÁLISE DE CRÉDITO; W, ARMAZÉNS GERAIS, CALC FRETE POR TRANSPORTADORA; W, CENTRAL DE CERTIFICAÇÃO; W, COMERCIAL; W, COMERCIALIZAÇÃO DE GRÃOS; W, COMISSÃO POR FÓRMULA; W, CONCILIAÇÃO BANCÁRIA AUTOMÁTICA; W, CONFERÊNCIA POR COLETOR APP; W, CONFIGURAÇÕES; W, CONHECIMENTO DE… |
| 5819 | Especialista Usuário BackOffice | 0 | 1939.4 | 646.5 | - | BásicoAcesso aos módulos ANÁLISE DE CRÉDITO; W, COMERCIAL; W, CONCILIAÇÃO BANCÁRIA AUTOMÁTICA; W, CONTROLE DE EPI; W, COTAÇÃO; W, DISTRIBUIÇÃO DE DF-E; W, EFD-REINF; W, FINANCEIRO; W, GESTÃO DE VERBAS DE FORNECEDOR; W, LIVROS FISCAIS; W, NOTA FISCAL DE SERVIÇO ELETRÔNICA; W, PORTAL DE IMPORTAÇÃO DOC. ELETRÔNICO; W,… |
| 5839 | Especialista Contabilidade | 0 | 2292 | 764 | - | Acesso aos módulos ANÁLISE DE CRÉDITO; W, CENTRAL DE CERTIFICAÇÃO; W, COMERCIAL; W, COMISSÃO POR FÓRMULA; W, CONCILIAÇÃO BANCÁRIA AUTOMÁTICA; W, CONFIGURAÇÕES; W, CONTABILIDADE; W, CONTABILIZAÇÃO; W, CONTROLE DE EPI; W, CONTROLE PATRIMONIAL; W, COTAÇÃO; W, DISTRIBUIÇÃO DE DF-E; W, EFD-REINF; W, FINANCEIRO; W, GESTÃO… |
| 5841 | Especialista Manufatura | 0 | 2292 | 764 | - | Acesso aos módulos ANÁLISE DE CRÉDITO; W, COMERCIAL; W, COMISSÃO POR FÓRMULA; W, CONCILIAÇÃO BANCÁRIA AUTOMÁTICA; W, CONFIGURAÇÕES; W, CONTROLE DE EPI; W, COTAÇÃO; W, DISTRIBUIÇÃO DE DF-E; W, EFD-REINF; W, FINANCEIRO; W, GESTÃO DE VERBAS DE FORNECEDOR; W, INVENTÁRIO; W, LIVROS FISCAIS; W, NOTA FISCAL DE SERVIÇO… |
| 5843 | Especialista Serviços | 0 | 2292 | 764 | - | Acesso aos módulos ANÁLISE DE CRÉDITO; W, COMERCIAL; W, COMISSÃO POR FÓRMULA; W, CONCILIAÇÃO BANCÁRIA AUTOMÁTICA; W, CONFIGURAÇÕES; W, CONTROLE DE CONTRATOS; W, CONTROLE DE EPI; W, COTAÇÃO; W, DISTRIBUIÇÃO DE DF-E; W, EFD-REINF; W, FINANCEIRO; W, GESTÃO DE VERBAS DE FORNECEDOR; W, INVENTÁRIO; W, LISTA DE TAREFAS; W,… |
| 5845 | Especialista Agro | 0 | 2292 | 764 | - | Acesso aos módulos ANÁLISE DE CRÉDITO; W, ARMAZÉNS GERAIS; W, COMERCIAL; W, COMERCIALIZAÇÃO DE GRÃOS; W, COMISSÃO POR FÓRMULA; W, CONCILIAÇÃO BANCÁRIA AUTOMÁTICA; W, CONFIGURAÇÕES; W, CONTROLE DE EPI; W, COTAÇÃO; W, DISTRIBUIÇÃO DE DF-E; W, EFD-REINF; W, FINANCEIRO; W, GESTÃO DE VERBAS DE FORNECEDOR; W, INVENTÁRIO; W,… |
| 5851 | Especialista Vendas | 0 | 1234.2 | 411.4 | - | Acesso aos módulos ANÁLISE DE CRÉDITO; W, COMERCIAL; W, COMISSÃO POR FÓRMULA; W, CUPOM FISCAL ELETRÔNICO (MFE); W, CUPOM FISCAL ELETRÔNICO (SAT); W, FINANCEIRO; W, NOTA FISCAL DE SERVIÇO ELETRÔNICA; W, NOTA FISCAL DO CONSUMIDOR ELETRÔNICA; W, NOTA FISCAL ELETRÔNICA; W, OPERAÇÕES DE CAIXA; W, TELEMARKETING; W, em… |
| 5847 | Especialista Distribuição | 0 | 2292 | 764 | - | Acesso aos módulos ANÁLISE DE CRÉDITO; W, COMERCIAL; W, COMISSÃO POR FÓRMULA; W, CONCILIAÇÃO BANCÁRIA AUTOMÁTICA; W, CONFERÊNCIA POR COLETOR APP; W, CONFIGURAÇÕES; W, CONHECIMENTO DE TRANSPORTE ELETRONICO; W, CONTROLE DE EPI; W, CONTROLE DE VEÍCULOS; W, COTAÇÃO; W, DISTRIBUIÇÃO DE DF-E; W, EFD-REINF; W, FINANCEIRO; W,… |
| 5849 | Especialista Varejo | 0 | 2292 | 764 | - | Acesso aos módulos ANÁLISE DE CRÉDITO; W, COMERCIAL; W, COMISSÃO POR FÓRMULA; W, CONCILIAÇÃO BANCÁRIA AUTOMÁTICA; W, CONFIGURAÇÕES; W, CONTROLE DE EPI; W, COTAÇÃO; W, CUPOM FISCAL ELETRÔNICO (MFE); W, CUPOM FISCAL ELETRÔNICO (SAT); W, DISTRIBUIÇÃO DE DF-E; W, EFD-REINF; W, FINANCEIRO; W, GESTÃO DE VERBAS DE… |
| 5853 | Especialista GPD | 0 | 2292 | 764 | - | Acesso aos módulos COMERCIAL; W, CONTROLE DE CONTRATOS; W, FINANCEIRO; W, GESTÃO DE VERBAS ORÇAMENTÁRIAS; W, GPD - GESTÃO ESTRATÉGICA; W, ORDEM DE SERVIÇO; W, SANKHYA GPD APP; W, SANKHYA OK APP; W, SANKHYAFLOW, SLA; W, em conformidade com os packs constantes no Anexo I. |
| 5837 | Usuário BackOffice Avançado (EVO POR USUÁRIO) | 0 | 1237.3 | 452.5 | - | Acesso aos módulos ANÁLISE DE CRÉDITO; W, COMERCIAL; W, COMISSÃO POR FÓRMULA; W **, CONCILIAÇÃO BANCÁRIA AUTOMÁTICA; W, CONTROLE DE EPI; W, COTAÇÃO; W, DISTRIBUIÇÃO DE DF-E; W, EDITOR DE DASHBOARD; W, EFD-REINF; W, GESTÃO DE VERBAS DE FORNECEDOR; W, GESTÃO DE VERBAS ORÇAMENTÁRIAS; W, GPD - GESTÃO ESTRATÉGICA; W,… |
| - | Sankhya DataLink Access | 0 | 0 | 0 | - | - |
| - | Acesso ao BD / Migração SaaS | 0 | 0 | 0 | - | - |
| 6010 | Saas (cloud) Pack | 0 | 0 | 0 | - | Infraestrutura exclusiva para hospedagem da plataforma Sankhya, sendo vedada a utilização para outras aplicações não relacionadas a ela;- Só é possível realizar integrações com a plataforma Sankhya na modalidade Saas aqui contratada via API;- O modelo adotado é VPN Client-to-Site, com certificado digital e… |
| 5925 | Sankhya DataLink Access Pack | 0 | 0 | 0 | - | Acesso seguro e controlado a dados existentes, com permissão para consultas, alteração e manutenção da estrutura do banco de dados, sob rastreabilidade total.Ideal para: integrações, análises ou manutenção de dados operacionais. Segurança: VPN dedicada + MFA + auditoria de sessões. (DDL) |
| - | Sankhya DataLink Build | 0 | 0 | 0 | - | - |
| 6019 | Sankhya DataLink Build Pack | 0 | 0 | 0 | - | O Sankhya DataLink Build consiste no acesso seguro e supervisionado para manipulação de dados operacionais, permitindo inserções, atualizações e exclusões sob controle de permissões específicas. Também inclui alteração e manutenção da estrutura do banco de dados, com a segurança de VPN dedicada + controle de… |
| 5984 | Pack Basic Pro - Automação Bancária | 0 | - | 250 | - | Quantidade de transações incluídas: 1.500 (mil e quinhentas) Transações;Transações Contempladas: Boleto liquidado por código de barras, boleto liquidado por PIX, PIX recebido (imediato ou cobrança).Valor por transação excedente: Se a volumetria total de Transações no mês for menor que 20 mil (vinte mil): R$0,10 (dez… |
| 6075 | Pack Standard - Automação Bancária | 0 | - | 1125 | - | Quantidade de transações incluídas: 3.500 transações de recebimentos e 1.500 transações de PagamentosTransações contempladas em Recebimentos: Boleto liquidado por código de barras, boleto liquidado por PIX, PIX recebido (imediato ou cobrança), Transações Contempladas em Pagamentos: Título pago, título sincronizado… |
| 6076 | Pack Professional - Automação Bancária | 0 | - | 3250 | - | Quantidade de transações incluídas: 14.000 transações de recebimentos e 6.000 transações de PagamentosTransações contempladas em Recebimentos: Boleto liquidado por código de barras, boleto liquidado por PIX, PIX recebido (imediato ou cobrança)Transações Contempladas em Pagamentos: Título pago, título sincronizado pelo… |
| 6077 | Pack Enterprise - Automação Bancária | 0 | - | 5000 | - | Quantidade de transações incluídas: 28.000 transações de recebimentos e 12.000 transações de PagamentosTransações contempladas em Recebimentos: Boleto liquidado por código de barras, boleto liquidado por PIX, PIX recebido (imediato ou cobrança)Transações Contempladas em Pagamentos: Título pago, título sincronizado… |

## Preço de lista por usuário/CNPJ (MRR, R$ cada)

| Faixa de usuários | Usuário padrão | CNPJ | Pedido Web | Analytics |
|---|---|---|---|---|
| Até 10 | 675 | 350 | 280 | 350 |
| De 11 a 30 | 607.5 | 315 | 252 | 315 |
| De 31 a 50 | 546.8 | 283.5 | 226.8 | 283.5 |
| De 51 a 100 | 492.1 | 255.2 | 204.1 | 255.2 |
| Acima de 101 | 442.9 | 229.6 | 183.7 | 229.6 |
