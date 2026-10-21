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
