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
