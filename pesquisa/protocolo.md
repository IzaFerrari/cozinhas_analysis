# Protocolo — Cozinhas Solidárias: unidades recebedoras por organização fornecedora (PAA 2025)

Estado: congelado (fase 3, D-6). Mudança material só por bloco novo em `decisoes.md` (CHANGE_PLAN); o congelamento é o commit que traz este estado.

## Question

Quantas unidades recebedoras do Programa Cozinha Solidária cada organização fornecedora contratada pela CONAB no PAA em 2025 atende, e como esse número se distribui entre as organizações?

Claim: descriptive
Unit of analysis: organização fornecedora, identificada pelo CNPJ, com pelo menos um projeto PAA–Cozinhas de 2025 na planilha da CONAB (DATA1, D-4).
Estimand: para todas as organizações fornecedoras do snapshot DATA1 (população censitária, não amostra), a distribuição do nº de unidades recebedoras distintas (`Código da Cozinha`, D-3) vinculadas aos projetos de 2025 de cada organização. Resumos: mediana e quartis, proporção de organizações com 0, 1, 2–9 e 10 ou mais unidades, máximo, e participação dos 10% maiores no total de vínculos organização–unidade. Estratificado por mecanismo (CDS vs CDAF/CI) e por UF da organização.
Refutation: a pergunta fica errada ou bem mais estreita se (a) o `Código da Cozinha` não identifica unidades recebedoras de forma consistente, e então a contagem deixa de medir "unidades atendidas" e passa a medir "registros"; (b) a aba de unidades não for um registro completo, de modo que os projetos sem unidade sejam lacunas de cadastro e não zeros reais; ou (c) o snapshot mudar materialmente antes da análise final (a fonte é alterável).
Objection: a objeção mais forte é de medida. A granularidade do código varia: há códigos `EG…` que reúnem várias cozinhas, códigos `CS…` com dezenas de nomes de consumidor e o registro "unidade gestora" (CONAB, SESC, CEAGESP) atuando como intermediário. Ela será tratada na fase 4 (relatório de dados), reportando lado a lado as medidas de D-3 (código, nome normalizado, só CS, só CDS). O significado do código fica em aberto por decisão humana (D-3), e o texto falará em "unidades recebedoras registradas".
Who cares: trabalho acadêmico de quem conduz a pesquisa (IzaFerrari). A consequência é de conhecimento: caracterizar como os fornecedores do PAA se ligam às cozinhas solidárias em 2025 e mostrar quanto a resposta depende da unidade de contagem.
Non-goals: não explica por que a distribuição tem essa forma (as linhagens explicativas estão em `Deferred`, D-2); não faz inferência causal; não avalia desempenho do programa, volume entregue, valor ou pessoas atendidas; não cobre outros anos nem outras modalidades além das da planilha; não testa hipóteses confirmatórias com DATA1 (D-4).

## Portfólio ativo

Componentes descritivos adotados da exploração (`pesquisa/exploracao/2026-10-14-explorer.md`), todos dentro do escopo de D-2:

1. Distribuição nacional pela medida principal (código distinto).
2. Sensibilidade à unidade de contagem: nome normalizado (teto), só códigos CS e só projetos CDS (linhagem 1 da exploração).
3. Estratificação por mecanismo e UF, incluindo a decomposição contábil grau médio = (unidades ÷ organizações) × (organizações por unidade), como descrição e não como explicação (linhagens 2 e 4).

Nenhuma hipótese confirmatória é formulada sobre DATA1 (D-4).

## Compromissos congelados

### Hipóteses

Nenhuma. A pesquisa é descritiva (D-2) e DATA1 já foi exposto (D-4). Não há teste primário, regra de confirmação nem registro externo (D-6).

### Dados e população

- Entrada única: DATA1 (D-4), lido só das cópias em `pesquisa/dados/brutos/`, nunca da planilha online. Antes de cada execução, o sha256 dos dois arquivos é conferido com D-4; se divergir, a execução para e o arquivo novo recebe outra identidade (DATA2).
- População: todas as organizações (CNPJ) da aba de contratações de DATA1. É censo do snapshot, não amostra.
- Ligação: `N° DO PROJETO` = `Num TPAF`, mantendo todos os projetos (junção à esquerda). Projeto sem linha na aba de unidades contribui com 0 unidades.

### Medida

Grau de uma organização: nº de valores distintos de `Código da Cozinha` somando todos os projetos do CNPJ (D-3). Códigos `EG…` e o registro "unidade gestora" contam como uma unidade cada.

Sensibilidades (D-3), cada uma recalculando todos os resumos de E1:
- S1: nº de `Nome Consumidor` distintos após a normalização de `pesquisa/scripts/problema.py` (teto);
- S2: só códigos que começam com `CS`;
- S3: só projetos com `MECANISMO RESUMO 2` = CDS; a população passa a ser as organizações com ao menos um projeto CDS.

### Estimandos

**E1. Distribuição nacional do grau (medida principal).**
- Tabela de frequência completa: nº de organizações com grau 0, 1, 2, … até o máximo.
- nº de organizações, nº de vínculos organização–unidade (pares CNPJ–código distintos) e nº de unidades distintas.
- Mínimo, quartis (método linear do pandas), mediana, máximo e média.
- Proporção de organizações com grau 0, 1, 2–9 e 10 ou mais.
- Participação dos 10% maiores no total de vínculos. O nº de organizações do topo é round(0,10 × n), com o `round` do Python; empates no corte não alteram a soma.
- Coeficiente de Gini do grau, com zeros, sem correção de amostra pequena: G = Σᵢ Σⱼ |xᵢ − xⱼ| / (2 n² μ). Entra como resumo adicional, sem substituir a referência de D-5.

**E2. Dependência da unidade de contagem.** Os resumos de E1 sob S1, S2 e S3, lado a lado com a medida principal. Nenhuma variante substitui a principal. Se elas divergirem, a divergência é o resultado: mostra o quanto a resposta depende da granularidade.

**E3. Estratificação (descrição, não explicação).**
- E3a, mecanismo: cada organização entra em uma de três classes pelos `MECANISMO RESUMO 2` de seus projetos: só CDS; só CDAF/CI (CDAF inclui CDAF/EVENTO); ambos. O grau é o da medida principal, com todos os projetos da organização. Por classe: nº de organizações, nº de vínculos, quartis, mediana, média, máximo e proporção com grau 0.
- E3b, UF da organização (`UF ORGANIZAÇÃO`, única por CNPJ em DATA1). Por UF: nº de organizações, nº de unidades distintas ligadas a organizações da UF, nº de vínculos, mediana, média e máximo. Inclui a decomposição contábil grau médio das organizações = (unidades ÷ organizações) × (organizações por unidade), em que organizações por unidade = vínculos ÷ unidades. A identidade é exata por construção. Uma unidade ligada a organizações de mais de uma UF entra em cada uma dessas UFs; por isso a soma das unidades por UF pode passar do total nacional.

### Saídas

- Tabela 1: E1 e E2, com as quatro medidas em colunas.
- Figura 1: barras da frequência do grau (medida principal), com a mediana marcada.
- Tabela 2: E3a.
- Tabela 3: E3b, com todas as UFs e o n de organizações em cada linha.

Os números do texto vêm de agregados gravados em `pesquisa/agregados/` por script que lê DATA1. Qualquer outra tabela ou figura é exploratória e precisa ser rotulada assim.

### Inferência

Não há teste de hipótese, valor-p nem intervalo de confiança: os resumos descrevem o censo do snapshot e não estimam uma população maior. A incerteza que importa é de medida, e E2 a expõe.

### Fronteira de interpretação

Pode afirmar:
- como se distribui, no snapshot DATA1, o nº de unidades recebedoras registradas (códigos) vinculadas aos projetos PAA–Cozinhas de 2025 de cada organização fornecedora;
- quanto essa forma muda com a unidade de contagem (E2);
- diferenças descritivas entre classes de mecanismo e entre UFs, sempre com o n de organizações ao lado;
- a decomposição contábil de E3b como identidade.

Não pode afirmar:
- "cozinhas físicas": o texto fala em "unidades recebedoras registradas" (D-3);
- entregas realizadas: os vínculos são os registrados nos projetos contratados, e a própria fonte avisa que os dados mudam conforme os projetos são executados;
- por que a distribuição tem essa forma, nem causas das diferenças entre UFs ou mecanismos (D-2). A decomposição de E3b não é mecanismo;
- generalização para outros anos, outras modalidades ou a versão atual da planilha;
- comparação direta com o cadastro do MDS (F3);
- que não existem estudos sobre o tema: só "não encontrado na busca da fase 2".

Nomes de organizações individuais não são estimando. Se aparecerem no texto, são ilustração.
