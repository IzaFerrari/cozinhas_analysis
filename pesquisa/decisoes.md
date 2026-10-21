# Registro de decisões

Blocos só de acréscimo. Uma decisão registrada só muda por um bloco posterior com `Supersedes: D-<n>`.

### D-1 · 2026-10-14 · Orçamento de exploração (registrado depois da execução)
A exploração estrutural (`explorer`) buscou mecanismos que explicassem a concentração do nº de cozinhas por organização e o desvio de AL/PB/RN. Amplitude: até quatro linhagens estruturalmente distintas, mais as descartadas explicitamente. Evidência: só DATA1 (D-4), por quatro scripts locais de exploração (`pesquisa/exploracao/scripts/`). Parada: dependência de evidência externa ou saturação revisada dentro de DATA1. Restrições: nenhuma ação externa e nenhuma alteração no notebook. Resultado: `pesquisa/exploracao/2026-10-14-explorer.md`.
Transparência: este orçamento foi registrado **depois** de a exploração rodar (mesma sessão, 2026-10-14), porque ela foi pedida antes de a pesquisa ser iniciada. Ele descreve o que de fato foi feito; não foi um limite prospectivo.
Rationale: o gate 1A exige um orçamento registrado; registrá-lo com a data e a ordem reais é preferível a fabricar uma precedência que não existiu.
Revision condition: qualquer nova rodada de exploração (por exemplo, se o escopo deixar de ser descritivo) exige um orçamento registrado antes de rodar.

### D-2 · 2026-10-14 · Escopo descritivo, para trabalho acadêmico
Decisão humana (IzaFerrari, 2026-10-14). A pesquisa é descritiva: estima quantas unidades recebedoras cada organização fornecedora atende em 2025 e como esse número se distribui. O resultado será usado em trabalho acadêmico. As linhagens explicativas da exploração (complementaridade de cesta, causas da razão cozinhas/organizações por UF) não entram no portfólio ativo; vão para `Deferred` no mapa.
Rationale: escolha de quem conduz a pesquisa, feita entre as opções descritiva, descritiva com teste em dado novo e explicativa só com 2025.
Revision condition: decidir testar mecanismos. Isso exigiria dados independentes de DATA1 (outro ano ou outro snapshot), por causa de D-4.

### D-3 · 2026-10-14 · Medida de "cozinha": Código da Cozinha distinto; nome como sensibilidade
Medida principal: nº de valores distintos de `Código da Cozinha` nos projetos de cada CNPJ, somando todos os projetos da organização. Os projetos sem unidade registrada contam como 0. Medidas de sensibilidade: (a) nº de `Nome Consumidor` distintos após normalização (sem acento, maiúsculas, sem preposições), tratado como teto; (b) só códigos que começam com `CS` (sem `EG…` e sem "unidade gestora"); (c) só projetos `CDS/COZINHAS`.
O significado semântico do código não será investigado agora (decisão humana, 2026-10-14: "ignora essa parte"). A objeção continua aberta. Por isso, a fronteira de interpretação deve falar em "unidades recebedoras registradas (códigos)", e não em "cozinhas físicas".
Transparência: a medida principal antecede a exposição à variação entre medidas; ela está no notebook desde o commit 0746570 (2026-09-30). As sensibilidades (a)–(c) foram escolhidas depois de a exploração mostrar que elas mudam os números, portanto são informadas pelos dados.
Rationale: o código é o identificador que a própria fonte usa e o que o notebook já usava; as variantes delimitam o quanto a resposta depende da granularidade.
Revision condition: uma fonte da CONAB/MDS que defina os códigos CS/EG, ou a decisão de resolver essa definição.

### D-4 · 2026-10-14 · DATA1 já exposto (papel: descoberta)
DATA1 é o snapshot da planilha CONAB/DIPAI/SUPAF/GEIAF de 2025, aba de contratações (gid=1251522308, 280 projetos) e aba de unidades recebedoras (gid=225140418, 1116 linhas), baixado em 2026-10-14 às 14:22 (UTC−5) de `https://docs.google.com/spreadsheets/d/1O_mmcnZ2QCBkA6juq_TzKYFv6KDwHsCU`. Cópias: `pesquisa/dados/brutos/contratacoes.csv` (sha256 480b46c4…31dbc) e `pesquisa/dados/brutos/unidades.csv` (sha256 6754d715…b102). A própria fonte avisa que as informações podem mudar a qualquer momento.
O conteúdo de DATA1 já foi observado no notebook (commits 0746570 a 9c796bb) e na exploração (D-1). Consequência: nenhuma hipótese gerada a partir de DATA1 pode ser confirmada com DATA1. As estimativas descritivas são uma descrição censitária deste snapshot, e as escolhas feitas após a exposição estão declaradas (D-3, D-5).
Rationale: lei 3 (descoberta não é confirmação); o git registra a ordem entre notebook e exploração, mas não prova ausência de outras exposições.
Revision condition: não revisável. A exposição é um fato histórico.

### D-5 · 2026-10-14 · Referência para julgar a premissa de heterogeneidade
A premissa "o nº de cozinhas por organização é heterogêneo a ponto de uma média única descrever mal a organização típica" é considerada material se, na medida avaliada, valerem as duas condições: (i) média − mediana ≥ 1 unidade recebedora; e (ii) os 10% de organizações com mais unidades reúnem ≥ 20% dos vínculos organização–unidade, o dobro da participação proporcional.
Transparência: a referência é informada pelos dados. Foi fixada depois de ver no notebook a média de 3,08 e a mediana de 1. Os limiares são escolhas simples e transparentes desta pesquisa, não uma convenção da literatura.
Rationale: uma diferença de uma unidade inteira entre média e mediana já muda a resposta "típica"; e o dobro da participação proporcional é um sinal grosseiro e legível de concentração.
Revision condition: se a literatura (fase 2) ou a orientação acadêmica indicar uma medida padrão de concentração (por exemplo, Gini), ela entra como análise adicional, sem substituir esta referência em silêncio.
