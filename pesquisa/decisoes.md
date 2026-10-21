# Registro de decisões

Blocos só de acréscimo. Uma decisão registrada só muda por um bloco posterior com `Supersedes: D-<n>`.

### D-1 · 2026-10-21 · Recomeço; do trabalho anterior, só o snapshot de dados
Decisão humana (IzaFerrari, 2026-10-21). A pesquisa anterior (commit 67cc73c, removida em e9b94d9) não continua. Nenhuma decisão, medida, referência, estimando ou protocolo dela vale aqui sem nova decisão nesta pasta. Só o snapshot de dados é reaproveitado.
DATA1 é a planilha CONAB/DIPAI/SUPAF/GEIAF, período 2025, baixada em 2026-10-14 às 14:22 (UTC−5) de `https://docs.google.com/spreadsheets/d/1O_mmcnZ2QCBkA6juq_TzKYFv6KDwHsCU`. São duas abas: contratações (gid=1251522308, cabeçalho na linha 11, 280 projetos) e unidades recebedoras (gid=225140418, cabeçalho na linha 7, 1116 linhas). As cópias foram restauradas do commit 67cc73c em 2026-10-21:
- `pesquisa/dados/brutos/contratacoes.csv`, sha256 `480b46c4660add2d8f8f64b1206bd04c05a85e21432b4cc5b9103879ebd31dbc`;
- `pesquisa/dados/brutos/unidades.csv`, sha256 `6754d7152e46ded005c27e61072420b40710a80bec86be79b3184fd0bc1db102`.
Os hashes conferem com os registrados na época. A própria fonte avisa que "as informações contidas na planilha podem ser alteradas a qualquer momento".
Rationale: com o snapshot fixo, os números do notebook podem ser reproduzidos. A planilha online pode ter mudado desde 14/10.
Revision condition: decisão humana de usar outro snapshot. Um arquivo com hash diferente recebe outra identidade (DATA2 ou seguinte), nunca o nome DATA1.

### D-2 · 2026-10-21 · DATA1 já está exposto; papel: descoberta
O conteúdo de DATA1 já foi observado antes desta pesquisa começar:
- no notebook `analise.ipynb`, desde o commit 0746570 (2026-09-30): a distribuição do nº de códigos de cozinha distintos por CNPJ (média 3,08, mediana 1, máximo 23), as 15 maiores, o boxplot por UF (medianas altas em AL, PB e RN) e a cobertura da ligação projeto–unidade; <!-- rm:ignore: números históricos do notebook, citados para registrar exposição, não como resultado -->
- na exploração de 2026-10-14 (commit 092afc8, `pesquisa/exploracao/` hoje removida), que examinou quatro linhagens com DATA1: granularidade do código (EG, CS com muitos nomes, "unidade gestora"), identidade de graus da rede bipartida e densidade por UF, complementaridade de cesta (sobreposição de produtos contra embaralhamento dentro da UF) e arquitetura de entrega (CDS × CDAF/CI);
- nesta sessão (2026-10-21), o orquestrador (Claude) leu o log de decisões, o problem brief e o resumo dessa exploração no histórico antes de formular a pergunta nova.
Consequência: o papel de DATA1 é `discovery`. Uma hipótese gerada ou selecionada a partir dessas observações, ou de explorações novas sobre DATA1, não pode ser confirmada nem validada com DATA1. A evidência confirmatória precisa vir de dado independente de DATA1, identificado e com regras fixadas antes de qualquer exposição ao seu conteúdo. Recomeçar os arquivos não apaga essa exposição.
Rationale: lei 3 (descoberta não é confirmação). O git registra a ordem dos commits, mas não prova que não houve outras exposições fora dele.
Revision condition: não revisável; a exposição é um fato histórico.

### D-3 · 2026-10-21 · Escopo explicativo
Decisão humana (IzaFerrari, 2026-10-21). A pesquisa é explicativa: por que algumas organizações fornecedoras atendem muito mais unidades recebedoras do que outras. Isso inclui o desvio entre UFs. Entre as opções oferecidas (mesma pergunta descritiva refeita ou pergunta explicativa), esta foi a escolhida.
Consequência combinada com D-2: DATA1 serve para gerar e afinar mecanismos e predições. Confirmar ou refutar exige dado independente. Se nenhum dado independente adequado for identificado, as hipóteses terminam em `BLOCKED` e o que vier de DATA1 é relatado como `EXPLORATORY`, nunca como confirmação.
Rationale: escolha de quem conduz a pesquisa.
Revision condition: decisão humana de voltar ao escopo descritivo ou de mudar a pergunta.

### D-4 · 2026-10-21 · Orçamento de exploração (registrado antes de rodar)
Foco: mecanismos estruturalmente distintos que expliquem a variação do nº de unidades recebedoras atendidas por organização fornecedora, incluindo a variação entre UFs.
Amplitude: até cinco linhagens candidatas estruturalmente distintas, mais as descartadas explicitamente. O portfólio ativo que sai da fase 1A tem no máximo três; as demais vão para `Deferred`.
Evidência permitida: DATA1 (papel `discovery`, D-2), só leitura das cópias em `pesquisa/dados/brutos/`, por scripts em `pesquisa/exploracao/scripts/`. Conhecimento prévio sobre o PAA e o Programa Cozinha Solidária pode orientar a busca, mas fica marcado como não verificado até a fase 2.
Proibido: baixar, abrir ou resumir qualquer base que possa servir de evidência independente (outro ano da planilha, snapshot atual da mesma planilha, outras bases CONAB/MDS). Abrir uma delas a exporia e a desqualificaria como teste. Também ficam proibidas ações externas e alterações no notebook.
Linhagens já vistas: as quatro de 2026-10-14 (D-2) são conhecidas. A exploração deve ir além delas ou contestá-las, não re-derivá-las como se fossem novas. Se uma delas for reaproveitada, ela conta como gerada por DATA1.
Parada: cada linhagem ativa precisa ter uma observação discriminante que DATA1 não resolve, com o tipo de dado independente que a resolveria; ou cinco linhagens; ou saturação dentro de DATA1.
Saída: `pesquisa/exploracao/2026-10-21-explorer.md`.
Rationale: o gate 1A exige um orçamento registrado antes da exploração. A proibição preserva a possibilidade de um teste confirmatório.
Revision condition: ampliar a amplitude ou a evidência exige um bloco novo antes de rodar.

### D-5 · 2026-10-21 · Fecho do gate 1A: tipo de afirmação, portfólio e adiamentos
Tipo de afirmação: associacional. A pesquisa discrimina mecanismos pelos padrões que cada um prevê no grafo organização–unidade. Não há intervenção nem desenho de identificação que permita leitura causal do regime sobre resultados do programa.
Portfólio ativo (até três, D-4): regime de alocação por UF; funil proposta → registro; diluição × capacidade (`pesquisa/exploracao/2026-10-21-explorer.md`). Vão para `Deferred`: economia de rota, perecibilidade e complementaridade de cesta.
Recorte explicativo: só projetos CDS, em que a organização entrega diretamente. CDAF e CI ficam fora do recorte explicativo.
Objeção acrescentada pelo orquestrador depois da exploração, a partir de números já calculados nela: em PI e BA, cada organização cobre 0,04–0,06 do conjunto da UF, mas cada unidade tem em média 4,3 e 3,5 organizações. Isso sugere vários pools menores e não territórios exclusivos. Se for assim, a diferença entre UFs é a escala do pool e não o regime. A objeção entra como refutação (c) do enunciado e é testada no gate 1B (D-6).
Rationale: lei 3 (DATA1 é descoberta) e o orçamento D-4. CDS é o único mecanismo em que o grau da organização mede entrega direta.
Revision condition: um documento da fase 2 que mostre que CDAF ou CI seguem a mesma regra de montagem; ou o resultado do gate 1B que reformule a pergunta.

### D-6 · 2026-10-21 · Referência do gate 1B (fixada antes de calcular os componentes)
O gate 1B examina duas premissas em DATA1, nos projetos CDS. Os números saem de `pesquisa/scripts/problema.py` para `pesquisa/agregados/`.
P1. Há heterogeneidade a explicar. Entre as organizações CDS com ao menos uma unidade vinculada, a premissa vale se média − mediana do grau ≥ 1 e se os 10% de organizações de maior grau reúnem ≥ 0,20 dos vínculos. Transparência: P1 é informada pelos dados (D-2). A mesma forma de referência foi usada na pesquisa anterior; aqui ela é decisão nova, não herança.
P2. Os regimes sobrevivem à divisão em componentes. São elegíveis as UFs com ≥ 10 unidades CDS vinculadas e ≥ 3 organizações. Em cada UF elegível, monta-se o grafo bipartido organização–código e calculam-se os componentes conexos. Um vínculo é de "pool" quando está num componente com ≥ 2 organizações e densidade (vínculos ÷ organizações × unidades) ≥ 0,5. A participação de pool da UF é a fração dos vínculos da UF que são de pool.
- `SHOWN` se ≥ 2 UFs elegíveis têm participação de pool ≥ 0,6 e ≥ 2 têm ≤ 0,3.
- `NOT_SHOWN` se todas as UFs elegíveis têm participação ≥ 0,5. Nesse caso há pool em toda parte na escala do componente, e a pergunta se reformula para a escala do pool (refutação (c) do enunciado).
- `INCONCLUSIVE` nos demais casos.
Transparência: a cobertura por UF, a densidade da UF inteira e a razão unidades/organizações já foram vistas na exploração. Os componentes conexos e as suas densidades não foram calculados antes desta decisão. Os limiares 0,5, 0,6 e 0,3 são escolhas simples desta pesquisa, não convenção da literatura.
Limite conhecido: componentes conexos não detectam pools sobrepostos dentro de um componente grande e esparso. Se uma UF grande sair "partição", isso não exclui pools locais sobrepostos. Esse limite fica registrado no problem brief.
Rationale: a refutação (c) é a forma mais barata de fazer a premissa do regime desaparecer usando só DATA1.
Revision condition: um limiar só muda por bloco novo e antes de qualquer uso confirmatório. Mudar depois de ver o resultado de P2 torna o veredito exploratório.

### D-7 · 2026-10-21 · Consequências do gate 1B para o portfólio
O problem brief (`pesquisa/problem-brief.md`) dá `SHOWN` para P1 e P2 pela referência da D-6, com duas ressalvas que mudam o portfólio.
1. A linhagem 1 passa a ser "pool denso × rede esparsa sobreposta". Fora do PR, os territórios exclusivos são raros nas UFs elegíveis.
2. Em DATA1, regime e razão unidades/organizações quase coincidem: dez das onze UFs elegíveis; a exceção é o PR. Fica fixado como requisito do teste confirmatório que o dado independente traga variação que separe as duas explicações. Antes de abrir o dado novo, a fase 3 fixa como essa separação será verificada, por exemplo UFs cuja razão muda entre anos. Se o dado independente repetir a colinearidade, a hipótese do regime termina em `INCONCLUSIVE`, e não em `CONFIRMED`.
Rationale: a refutação (c) do enunciado foi testada e não eliminou a premissa, mas mostrou que DATA1 não separa as duas explicações.
Revision condition: um documento da fase 2 que descreva a regra de montagem das propostas por UF. Se ele existir, o regime pode ser observado diretamente, sem depender só da forma do grafo.

### D-8 · 2026-10-21 · Fase 2: lacuna e mecanismo documentado para a linhagem 1
A busca (`pesquisa/literatura/busca.md`) não encontrou estudo sobre a estrutura dos vínculos organização–unidade do PAA nem análise quantitativa do PAA–Cozinhas (`pesquisa/literatura/fontes.md#lacuna`). O Manual de Operações da CONAB (Título 30, versão de 2026, N1) documenta que a lista de cozinhas vem do MDS, que a CONAB pode abrir chamada sobre a demanda mapeada (36.2) e que as cozinhas podem indicar organizações fornecedoras (35.3). Daí a interpretação da linhagem 1: a regra nacional admite duas rotas. A chamada aberta tende a produzir pool, porque várias organizações se declaram aptas à demanda do mesmo conjunto de cozinhas. A indicação pela cozinha tende a produzir rede esparsa, porque cada cozinha traz os seus fornecedores. O regime de uma UF seria a rota predominante na sua execução.
Isso muda a refutação (b) do enunciado: não há "regra nacional em que a organização escolhe livremente as unidades". A organização se candidata a unidades selecionadas pelo MDS. A refutação (b) não ocorreu nas fontes lidas.
Limite: a versão de 2024 do manual, vigente em 2025, não foi lida (N1, W4). Nenhuma fonte lida diz qual rota cada UF usou. A ligação entre rota e regime é inferência, não evidência.
Rationale: lei 1 e CITE. A fonte foi lida e o limite de versão está declarado.
Revision condition: a leitura da versão de 2024 com regra diferente, ou um documento por UF sobre a rota usada.

### D-9 · 2026-10-21 · Revisão do plano de análise (statistical-analysis)
A revisão do plano (statistical-analysis, `review-plan`) aceitou H1 com mudanças e reprovou H2 como confirmatória:
1. Limiar de escassez fixado por regra: o ponto médio do intervalo de limiares que minimiza os erros de classificação em DATA1, (1,45; 2,00], igual a 1,725. Por ser derivado de DATA1, H1 registra `Generated from: DATA1`. Exposição declarada: a notícia sobre o PI em 2026 (razão perto de 1,75, `pesquisa/literatura/busca.md`) foi vista antes de fixar a regra. Daí a sensibilidade T4 (1,60 e 1,85).
2. Rival "inércia de vínculos" acrescentado: checagem K5 e sensibilidade T2 (só vínculos novos).
3. Perda previsto→registrado: checagem K3 com ação prévia (UF com perda > 0,3 sai da contagem). O previsto não identifica quais unidades, por isso não pode ser especificação de H1.
4. Com poucas UFs discordantes, a probabilidade binomial sob p = 0,5 é qualificador obrigatório do relato, não regra de decisão.
5. H2 (diluição × capacidade) é rebaixada a exploratória. A elasticidade grau–kg não discrimina oferta empurrada de atribuição: pelo MOC item 37, a proposta é montada para atender à demanda das cozinhas, e o kg não é comparável entre produtos. O estado terminal previsto é `NOT_VERIFIED`. A diluição com medida de capacidade exógena vai para `Deferred`.
6. O funil proposta→registro não vira hipótese: é checagem (K3) e descrição (H2, T7).
Rationale: lei 2 (as escolhas que um resultado pode influenciar são fixadas antes) e a revisão do plano antes da execução.
Revision condition: só por CHANGE_PLAN depois do congelamento (D-10).

### D-10 · 2026-10-21 · Congelamento do protocolo e do plano; registro interno
O protocolo (`Estado: congelado`), o plano (`Freeze: frozen`), o registro interno (`pesquisa/registro.md`) e o código de H1 se congelam no mesmo commit, o que traz este bloco.
Registro externo (OSF ou outro): não feito. Publicaria a pesquisa fora do repositório, o que é decisão humana. Fica registrado como `internal` no mapa. Se a orientação acadêmica pedir registro externo, ele deve ser feito antes de abrir DATA2, e entra por bloco novo.
Rationale: lei 2. O registro interno prova a ordem dos commits, não a ausência de outras exposições.
Revision condition: mudança de estimando, população, desfecho, preditores, limiares ou regra de decisão só por bloco novo com `Supersedes: D-10`, e antes de abrir DATA2. Depois de abrir DATA2, qualquer mudança torna o resultado exploratório.

### D-11 · 2026-10-21 · Fase 4: DATA1 documentado; DATA2 não identificado
O relatório de dados (`pesquisa/dados/relatorio.md`) documenta a procedência, a ligação, as duplicidades, a granularidade e a população de DATA1. DATA2 não foi identificado: o arquivo-fonte atual só tem 2025, com as mesmas linhas de DATA1, e as buscas não acharam planilha de outro ano. H1 fica `BLOCKED` até DATA2 existir. A fase 4 é dada como alcançada para DATA1, com o bloqueio de DATA2 explícito.
Rationale: lei 1. A falta do dado confirmatório vira estado, não suposição.
Revision condition: DATA2 identificado, com hash e procedência registrados antes de abrir. Isso reabre a fase 4 para DATA2 e permite o FIT de H1.

### D-12 · 2026-10-21 · REOPEN de H1: checagem K7 da classe de DATA1
Supersedes: D-10
CHANGE_PLAN com destino `REOPEN`. O ensaio em amostra RUN-1 (exploratório, só DATA1) mostrou que a perda previsto→registrado em DATA1 passa de 0,3 em PE (0,67), RS (0,61) e MG (0,32) (`pesquisa/agregados/h1_data1_em_amostra.json`). O plano congelado na D-10 aplicava esse limite (K3) só a DATA2. Com isso, a classe de persistência dessas três UFs se apoiava em registro incompleto. O caso mais forte é o PE: classe "pool" calculada sobre um terço das unidades previstas.
Mudança: acrescenta A7/K7 a H1. A UF cuja perda em DATA1 seja > 0,3 sai da população primária, com o mesmo limite de K3. Em DATA1, a população primária máxima passa de onze para oito UFs (AL, BA, PB, PI, PR, RN, SC, SE). O código ganha a constante `EXCLUIDAS_K7` e uma checagem que a recalcula sobre DATA1. Nada mais muda: estimando, desfecho, preditores, limiares e regra de decisão continuam os da D-9 e da D-10.
Transparência: a mudança foi motivada por um diagnóstico de DATA1 visto depois do congelamento da D-10, e **antes** de qualquer exposição a DATA2, que continua não identificado (D-11). DATA1 já constava em `Generated from`. O novo congelamento é o commit que traz este bloco; o congelamento anterior (cd2a582) fica no histórico.
Rationale: lei 2. A mudança é registrada antes da exposição ao dado confirmatório, e o limite é o mesmo já fixado para DATA2.
Revision condition: mudança só por bloco novo com `Supersedes: D-12`, antes de abrir DATA2.

### D-13 · 2026-10-21 · Recibo de RUN-1 retirado por defeito de identidade; RUN-2 o substitui
O recibo `RUN-1` (commit 3b14a99) declarava DATA1 duas vezes, com um caminho para cada CSV. O contrato pede um id por conteúdo commitado, e o validador reprova o recibo (`runs`: "DATA1 maps to multiple committed input contents"). Recibos são só de acréscimo, então ele não foi editado nem apagado. Foi movido sem mudança para `.research/runs/retirados/RUN-1.json`, fora da leitura do validador, e continua no histórico.
`RUN-2` descreve a **mesma execução** (execution freeze 09b4cf7, run commit 445fabf, mesma saída), com DATA1 identificado pelo diretório `pesquisa/dados/brutos` (um único tree no git) e resultado `R2`. `R1` não é usado em nenhum texto.
Rationale: lei 1. A correção recebe identidade nova, e a execução e a saída não mudam.
Revision condition: não revisável; é registro histórico.

### D-14 · 2026-10-21 · Fase 5: estados terminais
FIT de H1: o protocolo e o plano estão congelados (0ef5f3a), o registro interno também, e o código está congelado e ensaiado (RUN-2, RUN-4). Falta o dado confirmatório: DATA2 não está identificado (D-11), e nenhuma execução confirmatória pode expor resultado. **H1 = `BLOCKED`.** Entra quando DATA2 for identificado e registrado antes de abrir (D-11); então se roda `h1_confirmatorio.py` sem mudanças, com recibo confirmatório (`analysis_role: primary`).
**H2 = `NOT_VERIFIED`**, como fixado no plano (D-9): o resultado de RUN-3 (R3) é descrição exploratória de DATA1 e não sustenta mecanismo.
Execuções exploratórias válidas: RUN-2 (H1 em amostra, código da D-10; R2), RUN-3 (H2; R3) e RUN-4 (H1 em amostra, código da D-12; R4). RUN-1 foi retirado (D-13).
Replay: o `replay.py` da ferramenta dá `ERROR` nas três, porque o recibo chama `.venv/bin/python` por caminho relativo e o `.venv` não é versionado. A verificação manual, com worktree no execution freeze, o Python do `.venv` por caminho absoluto e comparação byte a byte, deu `EXACT` em RUN-2, RUN-3 e RUN-4 (2026-10-21). Isso prova regeneração neste ambiente, não correção científica.
Diagnósticos de DATA1 vistos nos ensaios: K7 exclui MG, PE e RS; K4 passa de 5% em SE (0,091) e MG (0,077), o que no plano é limitação a relatar; K6 fica abaixo de 20% em todas as UFs elegíveis.
Rationale: estados terminais sob a regra registrada; capacidade ausente vira `BLOCKED`, não estimativa.
Revision condition: DATA2 identificado reabre H1 (fase 4 → FIT → fase 5).

### D-15 · 2026-10-21 · Correção de afirmações falsas (REVIEW-1, F5, F6, F12, F13)
Supersedes: D-14
A REVIEW-1 (`.research/reviews/REVIEW-1.md`) achou afirmações falsas em blocos anteriores. Elas são corrigidas aqui, sem editar os blocos originais:
1. D-14: "K6 fica abaixo de 20% em todas as UFs elegíveis" é **falso**. Em DATA1, o PR tem 0,286 de vínculos não-CS (4 de 14: EG000109, EG001973 duas vezes e "unidade gestora"). Pela A6, isso exige ler T5 ao lado; em RUN-4, T5 mantém o PR discordante. O PR é a única UF discordante em amostra, e essa limitação entra no manuscrito. O resto da D-14 (estados terminais, execuções, replay) continua valendo.
2. D-12: "Nada mais muda" é **falso** quanto ao código. A exclusão K7 passou a valer antes de K2, que passou a exigir 6 de até 8 UFs em vez de 6 de até 11, e K3 ficou depois de K2, numa ordem inconsistente. O REOPEN também tirou da população PE (razão 2,00) e RS (1,45), as UFs mais próximas do limiar, o que reduz a chance de haver UFs discordantes. Nada disso foi declarado na D-12. A ordem é fixada na D-16.
3. Relatório de dados: K4 e K6 tinham sido avaliadas com frações nacionais, mas são checagens por UF. Corrigido em `pesquisa/dados/relatorio.md`.
4. A checagem estrutural do arquivo-fonte atual passa a ter evidência commitada (`pesquisa/dados/fonte_atual/`). O relatório agora declara que o nº de linhas também foi lido.
Rationale: lei 1. A correção é um bloco novo, e os originais ficam no histórico.
Revision condition: não revisável; é correção de registro.

### D-16 · 2026-10-21 · REOPEN de H1 pela REVIEW-1 (F4, F6, F7, F8), antes de qualquer DATA2
Supersedes: D-12
CHANGE_PLAN com destino `REOPEN`. DATA2 continua não identificado, e nenhum conteúdo dele foi visto. Mudanças:
1. **Discordância exige mudança (F7).** Uma UF só conta como discordante se a sua classe de escassez **muda entre DATA1 e DATA2**, isto é, se a razão cruza 1,725, e a nova classe difere da classe de regime de DATA1. Isso implementa a exigência da D-7. Antes, uma UF que já era discordante em DATA1 (o PR) contaria como acerto da persistência mesmo sem mudar nada. O PR passa a ser relatado à parte.
2. **Exposição do PI (F4).** Se DATA2 for 2026, o PI sai da população primária e é relatado à parte. A razão dele em 2026 (cerca de 1,75, por notícia) foi vista antes de o limiar 1,725 ser fixado, e o limiar ficou logo abaixo dela. A regra é "UF cuja razão do ano confirmatório foi vista antes do congelamento sai". Hoje ela só atinge o PI em 2026.
3. **Ordem das exclusões (F6).** A ordem fica: elegibilidade nos dois anos, K7, K3, exposição e, por fim, K2 (≥ 6 UFs utilizáveis). Foi declarado na D-15 que o REOPEN da D-12 tirou PE e RS, as UFs mais próximas do limiar.
4. **Código (F8).** O script passa a exigir: o ano confirmatório (só linhas com `ANO` igual) e a exclusão dos projetos que já estão em DATA1; vínculos só com códigos `CS<n>` ou `EG<n>`, porque o marcador "unidade gestora" não é unidade e criaria pool espúrio; K1 conferindo os rótulos de mecanismo ⊆ {CDS, CDAF, CI} e a existência de vínculos CDS (senão BLOCKED); o CNPJ normalizado para dígitos; e o sha256 de DATA2 conferido contra valores que precisam ser registrados neste log **antes** de abrir o arquivo. Há um modo explícito `2025-ensaio` para ensaio em amostra, que nunca é teste de H1.
5. **Tabela de DATA1.** Com a regra de código, só o PR muda: participação 0,46 e razão 2,40 (antes 0,43 e 2,17). A classe continua esparsa. O intervalo de limiares que minimiza erros continua (1,45; 2,00], e o limiar continua 1,725.
Consequência declarada: a população utilizável máxima é de oito UFs, ou sete em 2026. Com a exigência de cruzamento, o resultado mais provável é INCONCLUSIVE.
Transparência: as mudanças vêm de uma revisão adversarial do commit 3eefb73 e de diagnósticos sobre DATA1 (descoberta). Nenhuma delas usa conteúdo de DATA2.
Rationale: leis 2 e 5. O desenho é corrigido antes da exposição ao dado confirmatório.
Revision condition: mudança só por bloco novo com `Supersedes: D-16`, antes de abrir DATA2.
