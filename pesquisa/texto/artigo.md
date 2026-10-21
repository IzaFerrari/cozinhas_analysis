# Como as organizações fornecedoras se ligam às cozinhas solidárias no PAA: a estrutura dos vínculos em 2025 e um teste registrado para o regime de alocação por UF

Manuscrito de trabalho. Os resultados são **exploratórios**. A hipótese confirmatória está registrada e congelada, mas **bloqueada** porque o dado independente ainda não foi obtido. Autoria, venue e licença: a definir (decisão humana).

## Resumo

Investigamos por que algumas organizações fornecedoras de projetos de Compra com Doação Simultânea (CDS) do PAA–Cozinhas, executado pela CONAB, atendem muito mais unidades recebedoras do que outras. Usamos a planilha pública da CONAB de 2025. A distribuição é assimétrica: a mediana é de 2 unidades por organização e o máximo é 23. Nas UFs com ao menos dez unidades e três organizações, a forma dos vínculos se separa em dois padrões. Em AL, PB, RN, SC e PE, as organizações compartilham praticamente o mesmo conjunto de unidades (pool denso). Em BA, PI, MG e SE, os vínculos formam uma rede esparsa e sobreposta. Fora do PR, territórios exclusivos são raros. Em 2025, os dois padrões quase coincidem com a razão entre unidades e organizações, e por isso os dados de um só ano não separam uma regra de alocação própria da UF da simples escassez de fornecedores. Na versão de 2026 do manual de operações da CONAB, a lista de cozinhas vem do MDS. O manual prevê chamada aberta sobre a demanda mapeada, indicação de organizações pela própria cozinha e compra direcionada. Não lemos a versão vigente em 2025. A ligação entre essas formas e os padrões observados é inferência nossa. Antes de obter qualquer planilha de outro ano, registramos um teste que separa "padrão persistente na UF" de "padrão que segue a escassez do ano". O teste não pôde ser executado e não distinguiria a rota administrativa de outras características estáveis da UF. Também documentamos que 0,315 das unidades previstas nas propostas CDS não aparecem como registradas, com a perda concentrada nos projetos grandes.

## 1. Introdução

O Programa de Aquisição de Alimentos (PAA) compra alimentos de organizações da agricultura familiar e os doa a unidades recebedoras. Desde 2024 há uma vertente para as cozinhas solidárias (PAA–Cozinhas). A literatura sobre o PAA privilegia o lado do fornecedor. Um trabalho sobre unidades recebedoras afirmava, em 2015, não haver estudos sobre elas (Silva e De Lorenzo, 2015; somente resumo lido). Nas bases consultadas, não encontramos estudo sobre a **estrutura dos vínculos** entre organizações e unidades: quantas unidades cada organização atende, se as organizações compartilham unidades e como isso varia entre UFs (`pesquisa/literatura/fontes.md#lacuna`). A busca não incluiu SciELO, BDTD nem relatórios institucionais diretamente. "Não encontrado" vale só para ela.

A pergunta tem alcance de gestão. Se a concentração de unidades em poucas organizações vem do desenho administrativo, a alavanca está nas regras das chamadas e das superintendências. Se vem da escassez de organizações aptas, está no recrutamento de mais fornecedores.

## 2. O que a regra documenta

O Manual de Operações da CONAB, Título 30, subtítulo IV, na versão de 14/05/2026, estabelece que o MDS apresenta à CONAB "uma lista das Cozinhas Solidárias cadastradas e habilitadas" (item 35). Pelas disposições gerais do mesmo manual, a organização fornecedora cadastra as unidades recebedoras e elabora a proposta (itens 3.1 e 3.2). O manual não diz quem atribui cada unidade da lista a cada organização. <!-- rm:ignore: números de item normativo -->
Para formar os fornecedores de uma cozinha, o manual prevê três formas. Com a demanda mapeada, "a Conab poderá abrir chamada" para propostas das organizações interessadas, e são contratados os projetos que "se declarem aptos com a demanda da cozinha" (itens 36.2 e 37). As cozinhas "se reservam ao direito de indicar potenciais organizações fornecedoras" (item 35.3). E, em casos específicos, a CONAB pode fazer compra direcionada segundo orientações do MDS (item 36.3). <!-- rm:ignore: números de item normativo -->
Conjecturamos que a chamada aberta tende a produzir pool, porque várias organizações se declaram aptas à demanda de um mesmo conjunto de cozinhas, e que a indicação pela cozinha tende a produzir rede esparsa. Essa ligação é inferência nossa: nenhuma fonte lida informa qual forma cada UF usou.
Lemos só a versão de 2026. Uma versão anterior (Ato Dipai nº 05/2024) foi localizada, mas não lida, e não verificamos qual versão regia as contratações de 2025. A ata do GGPAA de 29/01/2025 registra que a contratação das propostas exclusivas para cozinhas em 2025 seria feita "em formato ainda a ser apresentado". <!-- rm:ignore: identificação de ato normativo -->

## 3. Dados

Usamos a planilha pública da CONAB/GEIAF do PAA–Cozinhas, período 2025, num snapshot de 2026-10-14 com hash registrado (`pesquisa/dados/relatorio.md`; números de `pesquisa/agregados/dados.csv`). A planilha traz 280 projetos de 240 organizações (CNPJ) e 1116 linhas de unidades recebedoras. Todas as linhas de unidades encontram projeto, e 0,921 dos projetos têm ao menos uma unidade. O recorte é CDS, o mecanismo em que a organização entrega diretamente: 219 projetos, 206 organizações com vínculo e 705 vínculos distintos (CNPJ, código da cozinha). A medida é o **código da cozinha** registrado, não a cozinha física. 682 vínculos usam códigos CS, 22 usam códigos EG, que reúnem mais de uma cozinha, e 1 usa o marcador "unidade gestora", que não identifica unidade.

## 4. Métodos

O **grau** de uma organização é o nº de códigos distintos vinculados aos seus projetos CDS. Para cada UF, montamos o grafo bipartido organização–código e calculamos os seus componentes conexos. A **participação de pool** da UF é a fração dos vínculos que estão em componentes com duas ou mais organizações e densidade de pelo menos metade dos pares possíveis (D-6). Nas seções 5.2 e 5.3, os vínculos com o marcador "unidade gestora" não entram (D-16). <!-- rm:ignore: limiares de método -->
Todos os resultados abaixo vêm do mesmo ano em que os padrões foram descobertos, e por isso são exploratórios. As execuções têm recibo (`.research/runs/`). A regeneração byte a byte a partir do código congelado foi verificada à mão para RUN-2, RUN-3 e RUN-4 (D-14; `pesquisa/scripts/replay_manual.sh`) e pela ferramenta de replay para RUN-5.

## 5. Resultados exploratórios (2025)

### 5.1 Distribuição do grau

Entre as 206 organizações CDS com vínculo, a mediana do grau é 2 e a média é 3,42; nove em cada dez organizações atendem até 9 unidades, e o máximo é 23. A proporção de organizações com uma única unidade é 0,466. <!-- claim:C1 result:R3 -->

### 5.2 Dois padrões de vínculo entre UFs

Nas onze UFs com ao menos dez unidades e três organizações, a participação de pool separa dois grupos. É de 1,00 em AL, PB, RN e SC e de 0,88 em PE. É de 0,05 em BA, de 0,03 em PI e de 0,00 em MG e SE. PR (0,46) e RS (0,31) ficam entre os dois. <!-- claim:C2 result:R5 -->
O oposto do pool não é a partição em territórios exclusivos, salvo no PR. Em BA, PI e SE, quase todos os vínculos ficam num único componente grande e pouco denso. Em MG, eles se dividem em quatro componentes (`pesquisa/problem-brief.md`). Chamamos esse padrão de rede esparsa sobreposta.

### 5.3 Os padrões quase coincidem com a escassez

As UFs de pool têm de 2,00 a 4,33 unidades por organização: AL 3,00, PB 4,33, RN 2,00, SC 2,50 e PE 2,00. As de rede esparsa têm de 1,29 a 1,43: BA 1,29, PI 1,29, SE 1,33 e MG 1,43. O RS, intermediário, tem 1,45. A exceção é o PR, com 2,40 unidades por organização e participação de pool de 0,46. <!-- claim:C3 result:R5 -->
Na classificação binária do plano, em que é pool a UF com participação de pelo menos metade, "regra da UF" e "escassez de organizações" preveem o mesmo padrão em dez das onze UFs. Só o PR diverge. <!-- rm:ignore: limiar de método -->
O ensaio do teste registrado em 2025 (seção 6), com o mesmo ano como alvo e referência, mostra só que o código roda e reproduz as classes de 2025. Nele nenhuma UF pode cruzar o limiar, e as checagens de inércia ficam triviais. <!-- claim:C4 result:R5 -->

### 5.4 Perda entre unidades previstas e registradas

Em nenhum projeto CDS o nº de unidades registradas passa do previsto na proposta. No conjunto, falta 0,315 das unidades previstas. A perda cresce com o tamanho do projeto: é de 0,01 nos projetos que previam uma unidade e de 0,455 nos que previam dez ou mais, que registram 321 das 589 unidades previstas. <!-- claim:C5 result:R3 -->
Entre as UFs elegíveis, a perda passa de 0,3 em PE (0,67), RS (0,61) e MG (0,32). Por isso o teste registrado exclui essas UFs da população primária (K7, D-12). <!-- claim:C6 result:R5 -->
A cauda alta do grau, justamente o que se quer explicar, é a parte mais truncada da medida.

### 5.5 Grau e quantidade prevista

Dentro da UF, a elasticidade do grau registrado em relação ao kg previsto é de 0,291, com IC aproximado de 95% de 0,058 a 0,524 (erro-padrão agrupado por UF). Com o grau previsto, é de 0,371 (0,135 a 0,608). <!-- claim:C7 result:R3 -->
Isso descreve a associação em 2025 e não separa mecanismos. A proposta é montada para atender à demanda das cozinhas (item 37 do manual), e o kg não é comparável entre produtos. Por isso essa análise ficou exploratória desde o plano (D-9). <!-- rm:ignore: número de item normativo -->

## 6. O teste registrado e o seu estado

Antes de obter planilha de outro ano, registramos e congelamos no repositório (registro interno, sem registro externo) a hipótese H1 (`analysis-plan.md#h1`, `pesquisa/registro.md`). Nas UFs cuja razão entre unidades e organizações cruza o limiar de escassez entre 2025 e o ano confirmatório, o padrão do ano confirmatório segue o de 2025, e não a nova razão.
O teste conta, nessas UFs, qual preditor acerta. Ele decide com ao menos três UFs nessa situação e acerto em três quartos delas. Há checagens prévias de esquema, ano, hash, perda de registro (em 2025 e no ano confirmatório), vínculos interestaduais, inércia dos mesmos vínculos e granularidade do código. As sensibilidades são só vínculos novos, banda ambígua da classe, limiares alternativos de escassez e só códigos CS. <!-- rm:ignore: parâmetros da regra registrada -->
O limiar de escassez foi derivado de 2025 por regra, como ponto médio de um intervalo. Antes de fixá-lo, vimos uma notícia que dá ao PI, em 2026, uma razão perto de 1,75, logo acima do ponto médio. Por isso, se o ano confirmatório for 2026, o PI sai da população primária e é relatado à parte. O PR, que já diverge em 2025, também é relatado à parte (D-16). <!-- rm:ignore: número de notícia e regra, registrados como exposição -->
**Estado: bloqueado.** A versão atual da planilha só tem linhas de 2025 (`pesquisa/dados/fonte_atual/checagem.json`), e não encontramos planilha pública de outro ano. Com o dado de 2024 ou de 2026 no mesmo formato e o hash registrado antes da abertura, o teste roda sem mudança. Restam no máximo oito UFs utilizáveis, ou sete em 2026, e exige-se que a razão cruze o limiar. O resultado mais provável é inconclusivo. Mesmo que decida, o teste só distinguirá "padrão persistente na UF" de "padrão que segue a escassez do ano". Ele não dirá se a persistência vem da forma de seleção administrativa ou de outra característica estável da UF.

## 7. Limitações

- Todos os resultados vêm de um único ano, já explorado antes desta análise, e nenhum é confirmatório.
- A medida conta códigos registrados, não cozinhas físicas. Os códigos EG reúnem várias cozinhas. No PR, a única UF em que regra e escassez divergem em 2025, 0,231 dos vínculos usam códigos EG, acima do limite da checagem de granularidade do plano. A variante só com códigos CS (T5) não muda a leitura do PR no ensaio.
- O registro é incompleto, sobretudo nos projetos grandes e em PE, RS e MG.
- Em SE e MG, mais de 5% dos vínculos vão para unidades de outra UF. <!-- rm:ignore: limite da checagem K4 -->
- A regra lida é a versão de 2026 do manual, e a Resolução PAA/GG nº 7/2023 foi lida só por resumo.
- A literatura acadêmica foi lida só nos resumos.
- A ligação entre forma de seleção e padrão de vínculo é inferência.
- O registro do teste é interno ao repositório, não externo. Ele foi reaberto duas vezes antes de qualquer dado de outro ano (D-12, D-16), a segunda vez por uma revisão adversarial.
- Números de notícias de 2025 e 2026 foram vistos antes do registro (`pesquisa/literatura/busca.md`).

## 8. Conclusão

Em 2025, as organizações do PAA–Cozinhas se ligam às unidades de dois modos que variam por UF: um pool denso, em que quase todas atendem o mesmo conjunto, e uma rede esparsa sobreposta. Esses padrões quase coincidem com a escassez de organizações, e os dados de um só ano não dizem qual explicação vale. O teste registrado pode separar "padrão persistente na UF" de "padrão que segue a escassez do ano" se houver um segundo ano da mesma planilha em que razões cruzem o limiar. Com poucas UFs, ele tende a ser inconclusivo.

## Referências

- CONAB. Manual de Operações, Título 30 — Compra com Doação Simultânea (CDS). Ato de Direção Dipai nº 03, de 14/05/2026. <!-- rm:ignore: número do título normativo -->
- GGPAA. Ata de reunião de 29/01/2025.
- GGPAA. Resolução PAA/GG nº 7, de 4 de dezembro de 2023 (lida por resumo).
- Silva, J. B.; De Lorenzo, H. C. (2015). Análise do Programa de Aquisição de Alimentos (PAA) a partir de unidades recebedoras em municípios da Região Administrativa Central do Estado de São Paulo (somente resumo).

As demais fontes consultadas e o nível de leitura estão em `pesquisa/literatura/fontes.md` e `pesquisa/referencias.bib`.

## Declarações

- Dados e código: `pesquisa/dados/`, `pesquisa/scripts/`, `pesquisa/agregados/` e `.research/runs/`. A licença de reuso da planilha da CONAB não foi verificada.
- Uso de IA: a análise, o código e este texto foram produzidos com assistência de um modelo de linguagem (Claude). A forma da declaração exigida pela venue é decisão humana.
