# Como as organizações fornecedoras se ligam às cozinhas solidárias no PAA: um retrato dos vínculos em 2025

Manuscrito de trabalho, **descritivo**. Autoria, venue e licença: a definir (decisão humana).

## Resumo

Descrevemos como as organizações fornecedoras de projetos de Compra com Doação Simultânea (CDS) do PAA–Cozinhas, executado pela CONAB, se ligam às unidades recebedoras. Usamos a planilha pública da CONAB de 2025, num snapshot congelado.

**Grau.** A distribuição é assimétrica: a organização típica atende 2 unidades, a média é 3,42 e o máximo é 23.

**Padrões por UF.** Nas UFs com ao menos dez unidades e três organizações, os vínculos se organizam de dois modos:
- **pool denso** (AL, PB, RN, SC e PE): as organizações compartilham boa parte das mesmas unidades. A densidade do componente principal vai de 0,55 a 0,82, e PE se divide em quatro componentes.
- **rede esparsa sobreposta** (BA, PI, MG e SE).

Territórios exclusivos são raros, salvo no PR, onde mais da metade dos vínculos está em componentes de uma só organização, e, em parte, em MG (0,23).

**Escassez.** Os dois padrões quase coincidem com a razão entre unidades e organizações. As UFs de pool têm de 2,00 a 4,33 unidades por organização; as esparsas, de 1,29 a 1,43.

**Registro.** Faltam como registradas 0,315 das unidades previstas nas propostas, e a perda se concentra nos projetos grandes.

**Regra documentada.** Na versão de 2026 do manual de operações da CONAB, a lista de cozinhas vem do MDS, e o manual prevê chamada aberta, indicação de fornecedores pela própria cozinha e compra direcionada.

**O que fica em aberto.** Um único ano não permite dizer se os padrões vêm de uma regra própria da UF ou da escassez de fornecedores. Deixamos registrado um teste para quando a planilha trouxer outro ano.

## 1. Introdução

O Programa de Aquisição de Alimentos (PAA) compra alimentos de organizações da agricultura familiar e os doa a unidades recebedoras. Há regras específicas para as compras destinadas às cozinhas solidárias ao menos desde dezembro de 2023 (Resolução PAA/GG nº 7/2023, lida só por resumo), e o manual de operações da CONAB tem um subtítulo próprio para elas, o PAA–Cozinhas.

A literatura sobre o PAA privilegia o lado do fornecedor. Um trabalho sobre unidades recebedoras afirmava, em 2015, não haver estudos sobre elas (Silva e De Lorenzo, 2015; somente resumo lido). Nas bases consultadas, não encontramos estudo sobre a **estrutura dos vínculos** entre organizações e unidades (`pesquisa/literatura/fontes.md#lacuna`). A busca não incluiu SciELO, BDTD nem relatórios institucionais diretamente.

A pergunta deste trabalho é descritiva:
- quantas unidades cada organização atende;
- como os vínculos se organizam em cada UF;
- quanto do previsto nas propostas aparece registrado.

O retrato interessa à gestão do programa: mostra onde poucas organizações concentram o atendimento e onde o registro está incompleto.

## 2. A regra documentada

O Manual de Operações da CONAB, Título 30, subtítulo IV, na versão de 14/05/2026, estabelece que o MDS apresenta à CONAB "uma lista das Cozinhas Solidárias cadastradas e habilitadas" (item 35). Pelas disposições gerais, a organização fornecedora cadastra as unidades recebedoras e elabora a proposta (itens 3.1 e 3.2). O manual não diz quem atribui cada unidade da lista a cada organização. <!-- rm:ignore: números de item normativo -->

Para formar os fornecedores de uma cozinha, o manual prevê três formas:
- **chamada aberta:** a CONAB pode abrir chamada sobre a demanda mapeada, e são contratados os projetos que "se declarem aptos com a demanda da cozinha" (itens 36.2 e 37); <!-- rm:ignore: números de item normativo -->
- **indicação pela cozinha:** as cozinhas podem "indicar potenciais organizações fornecedoras" (item 35.3); <!-- rm:ignore: número de item normativo -->
- **compra direcionada:** em casos específicos, segundo orientações do MDS (item 36.3). <!-- rm:ignore: número de item normativo -->

Lemos só a versão de 2026. Uma versão anterior (Ato Dipai nº 05/2024) foi localizada, mas não lida. A ata do GGPAA de 29/01/2025 registra que a contratação para cozinhas em 2025 seria feita "em formato ainda a ser apresentado". <!-- rm:ignore: identificação de ato normativo -->

## 3. Dados

**Fonte.** A planilha pública da CONAB/GEIAF do PAA–Cozinhas, período 2025. É uma planilha única, atualizada à medida que a CONAB acrescenta dados. Usamos um snapshot de 2026-10-14 com hash registrado (`pesquisa/dados/relatorio.md`; números de `pesquisa/agregados/dados.csv`).

**Tamanho e ligação.** A planilha traz 280 projetos de 240 organizações (CNPJ) e 1116 linhas de unidades recebedoras. Todas as linhas de unidades encontram projeto, e 0,921 dos projetos têm ao menos uma unidade.

**Recorte.** CDS, o mecanismo em que a organização entrega diretamente: 219 projetos, 206 organizações com vínculo e 705 vínculos distintos (CNPJ, código da cozinha).

**Medida.** O **código da cozinha** registrado, não a cozinha física. 682 vínculos usam códigos CS, 22 usam códigos EG (que reúnem mais de uma cozinha) e 1 usa o marcador "unidade gestora", que não identifica unidade.

## 4. Métodos

- **Grau.** O grau de uma organização é o nº de códigos distintos vinculados aos seus projetos CDS.
- **Componentes.** Para cada UF, montamos o grafo bipartido organização–código e os seus componentes conexos.
- **Participação de pool.** É a fração dos vínculos da UF em componentes com duas ou mais organizações e densidade de pelo menos metade dos pares possíveis (D-6). <!-- rm:ignore: limiar de método -->
- **Perda.** É a fração das unidades previstas na proposta que não aparecem registradas.
- **Marcador.** Nos resultados por UF (seção 5.2 e a perda por UF), os vínculos com o marcador "unidade gestora" não entram. Nos resultados nacionais (seção 5.1 e a perda total), entram; há um único vínculo assim.

Todos os números são um censo do snapshot, sem inferência amostral. As escolhas de medida foram feitas depois de examinar os dados, e isso está registrado (`pesquisa/decisoes.md`, D-2). Os números descrevem 2025 e não testam hipóteses.

As execuções têm recibo (`.research/runs/RUN-3.json` e `RUN-6.json`) e se regeneram byte a byte a partir do código.

## 5. Resultados

### 5.1 Quantas unidades cada organização atende

Entre as 206 organizações CDS com vínculo, a mediana do grau é 2 e a média é 3,42; nove em cada dez organizações atendem até 9 unidades, e o máximo é 23. A proporção de organizações com uma única unidade é 0,466. <!-- claim:C1 result:R3 -->

### 5.2 Como os vínculos se organizam por UF

Nas onze UFs com ao menos dez unidades e três organizações, a participação de pool separa dois grupos:
- é de 1,00 em AL, PB, RN e SC e de 0,88 em PE;
- é de 0,05 em BA, de 0,03 em PI e de 0,00 em MG e SE;
- PR (0,46) e RS (0,31) ficam entre os dois. <!-- claim:C2 result:R6 -->

Fora o PR, o oposto do pool não é a partição em territórios exclusivos. Em BA, PI e SE, quase todos os vínculos ficam num único componente grande e pouco denso; em MG, eles se dividem em quatro componentes (`pesquisa/problem-brief.md`). Chamamos esse padrão de rede esparsa sobreposta.

**Tabela 1.** UFs com ao menos dez unidades e três organizações, projetos CDS, 2025 (`pesquisa/agregados/h1_data1_ensaio_v4.json`).

| UF | Organizações | Unidades | Vínculos | Unidades por organização | Participação de pool | Perda previsto→registrado |
|---|---|---|---|---|---|---|
| AL | 6 | 18 | 71 | 3,00 | 1,00 | 0,11 |
| PB | 3 | 13 | 32 | 4,33 | 1,00 | 0,00 |
| RN | 5 | 10 | 35 | 2,00 | 1,00 | 0,00 |
| SC | 4 | 10 | 22 | 2,50 | 1,00 | 0,24 |
| PE | 7 | 14 | 33 | 2,00 | 0,88 | 0,67 |
| PR | 5 | 12 | 13 | 2,40 | 0,46 | 0,19 |
| RS | 20 | 29 | 72 | 1,45 | 0,31 | 0,61 |
| BA | 24 | 31 | 109 | 1,29 | 0,05 | 0,25 |
| PI | 21 | 27 | 117 | 1,29 | 0,03 | 0,01 |
| MG | 7 | 10 | 13 | 1,43 | 0,00 | 0,32 |
| SE | 9 | 12 | 22 | 1,33 | 0,00 | 0,12 |

<!-- claim:C9 result:R6 -->

### 5.3 Os padrões quase coincidem com a escassez

As UFs de pool têm de 2,00 a 4,33 unidades por organização: AL 3,00, PB 4,33, RN 2,00, SC 2,50 e PE 2,00. As de rede esparsa têm de 1,29 a 1,43: BA 1,29, PI 1,29, SE 1,33 e MG 1,43. O RS, intermediário, tem 1,45. A exceção é o PR, com 2,40 unidades por organização e participação de pool de 0,46. <!-- claim:C3 result:R6 -->

Onde há mais unidades por organização, as organizações tendem a compartilhar as mesmas unidades. Onde há mais organizações para as unidades disponíveis, os vínculos se espalham. Qualquer corte de razão entre 1,45 e 2,00 separa os dois grupos com uma única exceção, o PR. <!-- rm:ignore: faixa descritiva -->

### 5.4 Quanto do previsto aparece registrado

Em nenhum projeto CDS o nº de unidades registradas passa do previsto na proposta. No conjunto, faltam como registradas 0,315 das unidades previstas. A perda cresce com o tamanho do projeto: é de 0,01 nos projetos que previam uma unidade e de 0,455 nos que previam dez ou mais, que registram 321 das 589 unidades previstas. <!-- claim:C5 result:R3 -->

Entre as UFs da Tabela 1, a perda passa de 0,3 em PE (0,67), RS (0,61) e MG (0,32). <!-- claim:C6 result:R6 -->

Como a planilha é atualizada à medida que dados são acrescentados, parte dessa perda pode ser atraso de registro. Com um só snapshot, não é possível separar atraso de corte. A cauda alta do grau é justamente a parte mais afetada.

### 5.5 Grau e quantidade prevista

Dentro da UF, a elasticidade do grau registrado em relação ao kg previsto é de 0,291, com IC aproximado de 95% de 0,058 a 0,524 (erro-padrão agrupado por UF). Com o grau previsto, é de 0,371 (0,135 a 0,608). <!-- claim:C7 result:R3 -->

Organizações com mais quantidade prevista atendem mais unidades, mas bem menos que proporcionalmente. Isso é descrição: a proposta é montada para atender à demanda das cozinhas (item 37 do manual), e o kg não é comparável entre produtos. <!-- rm:ignore: número de item normativo -->

## 6. Discussão e o que fica em aberto

O retrato de 2025 mostra que a concentração de unidades em poucas organizações não é homogênea entre UFs. Nas UFs com poucas organizações para as unidades habilitadas, cada organização atende boa parte das mesmas cozinhas. Nas UFs com mais organizações, cada uma atende poucas cozinhas, e os conjuntos se sobrepõem parcialmente.

Duas explicações são compatíveis com esse retrato. Ou a escassez de fornecedores força cada organização a atender muitas cozinhas, ou a forma de montar as propostas em cada UF produz o padrão. Pelo manual, essa forma pode ser chamada aberta, indicação pela cozinha ou compra direcionada. Como os padrões quase coincidem com a razão unidades/organizações, os dados de um só ano não separam as duas explicações. A ligação entre as formas do manual e os padrões é inferência nossa: nenhuma fonte lida diz qual forma cada UF usou.

Para quando a planilha trouxer outro ano, deixamos registrado e congelado um teste. Ele olha as UFs cuja razão sair da faixa entre 1,45 e 2,00 para o lado oposto ao do seu padrão e verifica se o padrão persiste ou acompanha a nova razão (`analysis-plan.md#h1`, `pesquisa/registro.md`). Com poucas UFs, o mais provável é que esse teste seja inconclusivo. Mesmo que decida, não dirá se a persistência vem da forma administrativa ou de outra característica estável da UF. <!-- rm:ignore: faixa da regra registrada -->

## 7. Limitações

- Um único ano, com escolhas de medida feitas depois de examinar os dados. A descrição vale para o snapshot de 2025.
- **Medida.**
  - Conta códigos registrados, não cozinhas físicas, e os códigos EG reúnem várias cozinhas.
  - No PR, a única UF fora da coincidência entre padrão e escassez, 0,231 dos vínculos usam códigos EG. Só com códigos CS, o PR tem 3,33 unidades por organização e participação de pool de 0,00, e continua sendo uma UF esparsa com razão alta. <!-- claim:C8 result:R6 -->
- **Registro.**
  - É incompleto, sobretudo nos projetos grandes e em PE, RS e MG.
  - A planilha muda com o tempo; outro snapshot pode dar números diferentes.
- **Vínculos interestaduais.** Em SE e MG, mais de 5% dos vínculos vão para unidades de outra UF. <!-- rm:ignore: limite da checagem K4 -->
- **Fontes lidas.**
  - A regra lida é a versão de 2026 do manual.
  - A Resolução PAA/GG nº 7/2023 e a literatura acadêmica foram lidas só por resumo.
- **Exposição.** Números de notícias de 2025, de 2026 e de ano não verificado foram vistos durante a pesquisa (`pesquisa/literatura/busca.md`).

## 8. Conclusão

Em 2025, a maioria das organizações fornecedoras do PAA–Cozinhas atende poucas unidades, e poucas atendem muitas. O modo como se ligam às cozinhas varia por UF. Onde há poucas organizações para as unidades habilitadas, elas compartilham boa parte das mesmas cozinhas. Onde há mais organizações, os vínculos se espalham numa rede esparsa. Cerca de um terço das unidades previstas nas propostas não aparece registrado, sobretudo nos projetos grandes. Por que os padrões diferem entre UFs fica em aberto, com um teste registrado para o próximo ano de dados.

## Referências

- CONAB. Manual de Operações, Título 30 — Compra com Doação Simultânea (CDS). Ato de Direção Dipai nº 03, de 14/05/2026. <!-- rm:ignore: número do título normativo -->
- GGPAA. Ata de reunião de 29/01/2025.
- GGPAA. Resolução PAA/GG nº 7, de 4 de dezembro de 2023 (lida por resumo).
- Silva, J. B.; De Lorenzo, H. C. (2015). Análise do Programa de Aquisição de Alimentos (PAA) a partir de unidades recebedoras em municípios da Região Administrativa Central do Estado de São Paulo (somente resumo).

As demais fontes consultadas e o nível de leitura estão em `pesquisa/literatura/fontes.md` e `pesquisa/referencias.bib`.

## Declarações

- **Dados e código:** `pesquisa/dados/`, `pesquisa/scripts/`, `pesquisa/agregados/` e `.research/runs/`. A licença de reuso da planilha da CONAB não foi verificada.
- **Uso de IA:** a análise, o código e este texto foram produzidos com assistência de um modelo de linguagem (Claude). A forma da declaração exigida pela venue é decisão humana.
