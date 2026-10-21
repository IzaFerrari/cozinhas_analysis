# Como as organizações fornecedoras se ligam às cozinhas solidárias no PAA: a estrutura dos vínculos em 2025 e um teste registrado para o regime de alocação por UF

Manuscrito de trabalho. Os resultados são **exploratórios**. A hipótese confirmatória está registrada e congelada, mas **bloqueada** porque o dado independente ainda não foi obtido. Autoria, venue e licença: a definir (decisão humana).

## Resumo

Investigamos por que algumas organizações fornecedoras de projetos de Compra com Doação Simultânea (CDS) do PAA–Cozinhas, executado pela CONAB, atendem muito mais unidades recebedoras do que outras. Usamos a planilha pública da CONAB de 2025. A distribuição é assimétrica: a mediana é de 2 unidades por organização e o máximo é 23. Nas UFs com ao menos dez unidades e três organizações, a forma dos vínculos se separa em dois padrões. Em AL, PB, RN, SC e PE, as organizações compartilham praticamente o mesmo conjunto de unidades (pool denso). Em BA, PI, MG e SE, os vínculos formam uma rede esparsa e sobreposta. Territórios exclusivos são raros. Nesse ano, porém, os dois padrões quase coincidem com a razão entre unidades e organizações. Por isso não é possível separar uma regra de alocação própria da UF da simples escassez de fornecedores. O manual de operações da CONAB documenta duas rotas para formar os fornecedores de uma cozinha: a chamada aberta sobre a demanda mapeada e a indicação de organizações pela própria cozinha. Uma dessas rotas é um mecanismo plausível para os padrões. Registramos antes de qualquer dado independente um teste que separa as duas explicações nas UFs em que elas divergem, mas o teste não pôde ser executado. Também documentamos que 0,315 das unidades previstas nas propostas CDS não aparecem como registradas, com a perda concentrada nos projetos grandes.

## 1. Introdução

O Programa de Aquisição de Alimentos (PAA) compra alimentos de organizações da agricultura familiar e os doa a unidades recebedoras. Desde 2024 há uma vertente para as cozinhas solidárias (PAA–Cozinhas). A literatura sobre o PAA privilegia o lado do fornecedor. Um trabalho sobre unidades recebedoras afirmava, em 2015, não haver estudos sobre elas (Silva e De Lorenzo, 2015; somente resumo lido). Nas bases consultadas, não encontramos estudo sobre a **estrutura dos vínculos** entre organizações e unidades: quantas unidades cada organização atende, se as organizações compartilham unidades e como isso varia entre UFs (`pesquisa/literatura/fontes.md#lacuna`). A busca não incluiu SciELO, BDTD nem relatórios institucionais diretamente. "Não encontrado" vale só para ela.

A pergunta tem alcance de gestão. Se a concentração de unidades em poucas organizações vem do desenho administrativo, a alavanca está nas regras das chamadas e das superintendências. Se vem da escassez de organizações aptas, está no recrutamento de mais fornecedores.

## 2. A regra de seleção documentada

O Manual de Operações da CONAB, Título 30, subtítulo IV (versão de 14/05/2026), estabelece que o MDS apresenta à CONAB "uma lista das Cozinhas Solidárias cadastradas e habilitadas" (item 35). A seleção das unidades não é da organização fornecedora. <!-- rm:ignore: número de item normativo -->
Com a demanda mapeada, "a Conab poderá abrir chamada" para receber propostas das organizações interessadas (item 36.2), e são contratados os projetos que "se declarem aptos com a demanda da cozinha" (item 37). As cozinhas, por sua vez, "se reservam ao direito de indicar potenciais organizações fornecedoras" (item 35.3). <!-- rm:ignore: números de item normativo -->
A regra é nacional, mas admite duas rotas. Na chamada aberta, várias organizações se declaram aptas à demanda de um mesmo conjunto de cozinhas, o que tende a produzir pool. Na indicação pela cozinha, cada cozinha traz os seus fornecedores, o que tende a produzir rede esparsa. Essa ligação é inferência nossa. Nenhuma fonte lida informa qual rota cada UF usou. Lemos a versão de 2026 do manual. A versão vigente nas contratações de 2025 (Ato Dipai nº 05/2024) foi localizada, mas não lida, então as regras acima não estão verificadas para 2025.

## 3. Dados

Usamos a planilha pública da CONAB/GEIAF do PAA–Cozinhas, período 2025, num snapshot de 2026-10-14 com hash registrado (`pesquisa/dados/relatorio.md`). A planilha traz 280 projetos de 240 organizações (CNPJ) e 1116 linhas de unidades recebedoras. A ligação entre projeto e unidade é exata: todas as linhas de unidades encontram projeto, e 0,921 dos projetos têm ao menos uma unidade. O recorte é CDS, o mecanismo em que a organização entrega diretamente. São 219 projetos, 206 organizações com vínculo e 705 vínculos distintos (CNPJ, código da cozinha). A medida é o **código da cozinha** registrado, não a cozinha física. 682 vínculos usam códigos CS e 22 usam códigos EG, que reúnem mais de uma cozinha.

## 4. Métodos

O **grau** de uma organização é o nº de códigos distintos vinculados aos seus projetos CDS. Para cada UF, montamos o grafo bipartido organização–código e calculamos os seus componentes conexos. A **participação de pool** da UF é a fração dos vínculos que estão em componentes com duas ou mais organizações e densidade de pelo menos metade dos pares possíveis. A referência para julgar as premissas foi fixada antes de calcular os componentes (D-6). <!-- rm:ignore: limiares de método -->
Todos os resultados abaixo vêm do mesmo ano em que os padrões foram descobertos, e por isso são exploratórios. As execuções têm recibo (`.research/runs/`) e se regeneram byte a byte a partir do código congelado.

## 5. Resultados exploratórios (2025)

### 5.1 Distribuição do grau

Entre as 206 organizações CDS com vínculo, a mediana do grau é 2 e a média é 3,42; nove em cada dez organizações atendem até 9 unidades, e o máximo é 23. A proporção de organizações com uma única unidade é 0,466. <!-- claim:C1 result:R3 -->

### 5.2 Dois padrões de vínculo entre UFs

Nas onze UFs com ao menos dez unidades e três organizações, a participação de pool separa dois grupos. É de 1,00 em AL, PB, RN e SC e de 0,88 em PE. É de 0,05 em BA, de 0,03 em PI e de 0,00 em MG e SE. PR (0,43) e RS (0,31) ficam entre os dois. <!-- claim:C2 result:R4 -->
O oposto do pool não é a partição em territórios exclusivos. Nas UFs com participação baixa, quase todos os vínculos ficam num componente grande e pouco denso (`pesquisa/problem-brief.md`). Chamamos esse padrão de rede esparsa sobreposta.

### 5.3 Os padrões quase coincidem com a escassez

As UFs de pool têm de 2,00 a 4,33 unidades por organização: AL 3,00, PB 4,33, RN 2,00, SC 2,50 e PE 2,00. As de rede esparsa têm de 1,29 a 1,45: BA 1,29, PI 1,29, SE 1,33, MG 1,43 e RS 1,45. A exceção é PR, com 2,17 unidades por organização e participação de pool de 0,43. <!-- claim:C3 result:R4 -->
Em 2025, portanto, "regra da UF" e "escassez de organizações" preveem o mesmo padrão em dez das onze UFs. Aplicado em amostra a 2025, o teste registrado (seção 6) acha uma única UF discordante (PR) e fica inconclusivo, como esperado: isso verifica o código, não a hipótese. <!-- claim:C4 result:R4 -->

### 5.4 Perda entre unidades previstas e registradas

Em nenhum projeto CDS o nº de unidades registradas passa do previsto na proposta. No conjunto, falta 0,315 das unidades previstas. A perda cresce com o tamanho do projeto: é de 0,01 nos projetos que previam uma unidade e de 0,455 nos que previam dez ou mais, que registram 321 das 589 unidades previstas. <!-- claim:C5 result:R3 -->
Por UF, a perda passa de 0,3 em PE (0,67), RS (0,61) e MG (0,32). Por isso o teste registrado exclui essas UFs da população primária (K7, D-12). <!-- claim:C6 result:R4 -->
A cauda alta do grau, justamente o que se quer explicar, é a parte mais truncada da medida.

### 5.5 Grau e quantidade prevista

Dentro da UF, a elasticidade do grau registrado em relação ao kg previsto é de 0,291, com IC aproximado de 95% de 0,058 a 0,524 (erro-padrão agrupado por UF). Com o grau previsto, é de 0,371 (0,135 a 0,608). <!-- claim:C7 result:R3 -->
Isso descreve a associação em 2025 e não separa mecanismos. A proposta é montada para atender à demanda das cozinhas (item 37 do manual), e o kg não é comparável entre produtos. Por isso essa análise ficou exploratória desde o plano (D-9). <!-- rm:ignore: número de item normativo -->

## 6. O teste registrado e o seu estado

Antes de qualquer dado de outro ano, registramos e congelamos no repositório (registro interno, sem registro externo) a hipótese H1: nas UFs em que o padrão de 2025 e a escassez do ano confirmatório preveem classes diferentes, o padrão do ano confirmatório segue o de 2025 (`analysis-plan.md#h1`, `pesquisa/registro.md`).
O teste conta, nessas UFs discordantes, qual preditor acerta. A decisão exige ao menos três UFs discordantes e acerto em três quartos delas. Há checagens prévias de esquema, de perda de registro, de vínculos interestaduais, de inércia dos mesmos vínculos e de granularidade do código. As sensibilidades são só vínculos novos, banda ambígua da classe, limiares alternativos de escassez e só códigos CS. O limiar de escassez foi derivado de 2025 por regra. Uma notícia sobre o PI em 2026 foi vista antes de fixá-lo, e isso está declarado. <!-- rm:ignore: parâmetros da regra registrada -->
**Estado: bloqueado.** A versão atual da planilha só contém 2025, e não encontramos planilha pública de outro ano (`pesquisa/dados/relatorio.md`). Com o dado de 2024 ou de 2026 no mesmo formato, o teste roda sem mudança. Mesmo assim, ele só distinguirá "padrão persistente na UF" de "padrão que segue a escassez do ano". Ele não poderá dizer se a persistência vem da rota administrativa ou de outra característica estável da UF.

## 7. Limitações

- Todos os resultados vêm de um único ano, já explorado antes desta análise, e nenhum é confirmatório.
- A medida conta códigos registrados, não cozinhas físicas. Os códigos EG reúnem várias cozinhas.
- O registro é incompleto, sobretudo nos projetos grandes e em PE, RS e MG.
- Em SE e MG, mais de 5% dos vínculos vão para unidades de outra UF. <!-- rm:ignore: limite da checagem K4 -->
- A regra lida é a versão de 2026 do manual, e a Resolução PAA/GG nº 7/2023 foi lida só por resumo.
- A literatura acadêmica foi lida só nos resumos.
- A ligação entre rota administrativa e padrão de vínculo é inferência.
- O registro do teste é interno ao repositório, não externo.

## 8. Conclusão

Em 2025, as organizações do PAA–Cozinhas se ligam às unidades de dois modos que variam por UF: um pool denso, em que quase todas atendem o mesmo conjunto, e uma rede esparsa sobreposta. Esses padrões quase coincidem com a escassez de organizações, e os dados de um só ano não dizem qual explicação vale. O desenho que decide está registrado e depende de um segundo ano da mesma planilha.

## Referências

- CONAB. Manual de Operações, Título 30 — Compra com Doação Simultânea (CDS). Ato de Direção Dipai nº 03, de 14/05/2026. <!-- rm:ignore: número do título normativo -->
- GGPAA. Ata de reunião de 29/01/2025.
- GGPAA. Resolução PAA/GG nº 7, de 4 de dezembro de 2023 (lida por resumo).
- Silva, J. B.; De Lorenzo, H. C. (2015). Análise do Programa de Aquisição de Alimentos (PAA) a partir de unidades recebedoras em municípios da Região Administrativa Central do Estado de São Paulo (somente resumo).

As demais fontes consultadas e o nível de leitura estão em `pesquisa/literatura/fontes.md` e `pesquisa/referencias.bib`.

## Declarações

- Dados e código: `pesquisa/dados/`, `pesquisa/scripts/`, `pesquisa/agregados/` e `.research/runs/`. A licença de reuso da planilha da CONAB não foi verificada.
- Uso de IA: a análise, o código e este texto foram produzidos com assistência de um modelo de linguagem (Claude). A forma da declaração exigida pela venue é decisão humana.
