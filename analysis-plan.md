# Analysis plan

Freeze: frozen

Pesquisa: por que algumas organizações fornecedoras de projetos CDS do PAA–Cozinhas atendem muito mais unidades (`pesquisa/protocolo.md`). Decisões: D-9 (revisão do plano) e D-10 (congelamento). Código: `pesquisa/scripts/h1_confirmatorio.py` (H1) e `pesquisa/scripts/h2_exploratorio.py` (H2), com versões em `pesquisa/requirements.txt`.

## H1

Estimand: E1
Primary test: T1
Mode: confirmatory
<!-- DATA<n> whose observed content generated/selected a non-precommitted confirmatory choice; triggering a frozen rule does not count. -->
Generated from: DATA1

### Design

Claim type: associational
Population: UFs elegíveis no ano confirmatório (DATA2) que também foram elegíveis em DATA1. Elegível é a UF (da organização) com ≥ 10 códigos de cozinha vinculados a projetos CDS e ≥ 3 organizações com vínculo. Em DATA1 são AL, BA, MG, PB, PE, PI, PR, RN, RS, SC e SE.
Exposure: dois preditores da classe de regime de cada UF em DATA2, fixados antes de abrir DATA2. (a) Persistência: a classe da UF em DATA1 (tabela abaixo). (b) Escassez: pool se a razão unidades/organizações da UF em DATA2 for ≥ 1,725, esparsa caso contrário.
Outcome: classe de regime da UF em DATA2. É pool se a participação de pool for ≥ 0,5. A participação de pool é a fração dos vínculos organização–código da UF que estão em componentes conexos com ≥ 2 organizações e densidade ≥ 0,5 (D-6).
Contrast: nas UFs discordantes (preditores (a) e (b) diferentes), a proporção em que a classe observada em DATA2 coincide com (a), contra a proporção em que coincide com (b).
Time: DATA1 = contratações de 2025 (snapshot de 2026-10-14); DATA2 = outro ano do PAA–Cozinhas (2024 ou 2026), na mesma planilha CONAB e com o mesmo esquema, com o snapshot identificado na fase 4 antes de abrir.
Identification: associacional. Não há identificação causal da rota administrativa: a persistência de classe é compatível com qualquer característica estável da UF (rota de montagem das propostas, MOC Título 30 itens 35.3 e 36.2; tamanho; geografia).
Dependence: a unidade é a UF. DATA1 e DATA2 da mesma UF são dependentes por desenho, e é essa dependência que se testa. A dependência entre UFs, por organizações que atendem unidades de outra UF, é pequena em DATA1 e é checada em K4. Não há inferência amostral: o teste é uma contagem sobre um censo administrativo. Com 3 a 6 UFs discordantes nenhum procedimento dá precisão alta, e a probabilidade binomial exata de um acerto tão bom ou melhor sob p = 0,5 é relatada como qualificador obrigatório, nunca como regra de decisão.

Classes de DATA1 congeladas (`pesquisa/agregados/problema.csv`, P2):

| UF | Participação de pool | Unidades por organização | Classe |
|---|---|---|---|
| AL | 1,00 | 3,00 | pool |
| PB | 1,00 | 4,33 | pool |
| RN | 1,00 | 2,00 | pool |
| SC | 1,00 | 2,50 | pool |
| PE | 0,88 | 2,00 | pool |
| PR | 0,43 | 2,17 | esparsa |
| RS | 0,31 | 1,45 | esparsa |
| BA | 0,05 | 1,29 | esparsa |
| PI | 0,03 | 1,29 | esparsa |
| MG | 0,00 | 1,43 | esparsa |
| SE | 0,00 | 1,33 | esparsa |

Limiar de escassez, por regra: em DATA1, os limiares de razão que minimizam os erros de classificação formam o intervalo (1,45; 2,00], com um único erro (PR). O limiar é o ponto médio, 1,725. Ele foi derivado de DATA1 (`Generated from`). A notícia sobre o PI em 2026, que dá uma razão perto de 1,75, foi vista antes desta regra (`pesquisa/literatura/busca.md`); por isso há a sensibilidade T4.

### Decision rule

CONFIRMED when: há ≥ 3 UFs discordantes na população primária e a classe de DATA2 coincide com a de DATA1 em ≥ 75% delas.
REFUTED when: há ≥ 3 UFs discordantes na população primária e a classe de DATA2 coincide com a prevista pela escassez em ≥ 75% delas.
INCONCLUSIVE when: há menos de 3 UFs discordantes (a colinearidade persiste, D-7), nenhuma das duas proporções chega a 75%, ou K2 falha.
BLOCKED when: DATA2 não foi identificado ou K1 falha.

### Assumptions

| ID | Assumption | Check | Failure action |
|---|---|---|---|
| A1 | DATA2 tem o mesmo esquema de DATA1: colunas de projeto, CNPJ, UF da organização, mecanismo CDS, previsto, nº TPAF e código da cozinha; e "CDS" designa o mesmo mecanismo | K1 | BLOCKED: o script para sem resultado |
| A2 | Há ao menos 6 UFs elegíveis nos dois anos | K2 | INCONCLUSIVE, com o motivo registrado |
| A3 | O registro das unidades em DATA2 é completo o bastante para a forma do grafo: perda previsto→registrado ≤ 0,3 na UF | K3 | a UF sai da população primária antes da contagem; se sobrarem < 3 discordantes, INCONCLUSIVE |
| A4 | A UF da organização representa onde o regime opera: vínculos interestaduais ≤ 5% em cada UF elegível | K4 | relatar as UFs acima de 5% como limitação; a decisão não muda |
| A5 | A persistência não é só repetição dos mesmos vínculos de DATA1 (inércia) | K5 | se a sobreposição mediana de pares (CNPJ, código) com DATA1 nas UFs discordantes for > 0,5, a interpretação se restringe a "persistência compatível com inércia de vínculos" e T2 é relatado ao lado; o primário decide |
| A6 | A granularidade do código não cria nem desfaz pools: códigos não-CS (EG, "unidade gestora") ≤ 20% dos vínculos de cada UF | K6 | relatar e ler T5 (só códigos CS) ao lado do primário; se T5 discordar do primário, a palavra "regime" fica qualificada como dependente da unidade de contagem |

### Primary analysis

Test: T1
Estimator: classificação de cada UF elegível em DATA2 pela participação de pool, depois a contagem, nas UFs discordantes, de quantas seguem a persistência e quantas seguem a escassez (`pesquisa/scripts/h1_confirmatorio.py`, função `decidir`).
Inference: contagem exata sobre o censo. Relata-se n de discordantes, acertos de cada preditor e P(X ≥ acertos do vencedor | Binomial(n, 0,5)).
Why this estimates E1: nas UFs discordantes, as duas explicações fazem previsões opostas sobre a mesma observação. Nas concordantes as duas acertam ou erram juntas, sem informação sobre qual é melhor.

### Sensitivity

- T2: o mesmo teste com a participação de pool calculada só sobre vínculos novos, isto é, pares ausentes em DATA1. Só entram UFs com ≥ 5 vínculos novos. Separa persistência de inércia (A5).
- T3: o mesmo teste excluindo as UFs com participação de pool em DATA2 entre 0,4 e 0,6 (banda ambígua da classe).
- T4: o mesmo teste com limiar de escassez 1,60 e 1,85, por causa da exposição prévia à notícia do PI 2026.
- T5: o mesmo teste só com códigos que começam com "CS", recalculando as classes de DATA1 e de DATA2 (granularidade, A6).

### Specification dimensions

- none

### Interpretation boundary

May claim: com CONFIRMED, que nas UFs em que o regime de DATA1 e a escassez de DATA2 divergiam, o regime de DATA2 seguiu o de DATA1 em k de n; que o regime de alocação se comportou como propriedade persistente da UF, não explicada pela razão unidades/organizações do ano, sob a regra registrada e com a probabilidade binomial relatada. Com REFUTED, que seguiu a escassez. Com INCONCLUSIVE, que os dados não separaram as explicações.
May not claim: que a regra ou a rota da superintendência (chamada × indicação pela cozinha) causa o regime; que a rota é o mecanismo, porque ela não é observada; generalização além das UFs elegíveis e dos dois anos; nada sobre cozinhas físicas; nada sobre o valor ou o volume entregue; força estatística além da contagem e da probabilidade binomial relatadas; confirmação com DATA1.

For material construct/mechanism interpretations, record the bridge here (otherwise omit):
- Construct and measure: regime de alocação, isto é, a forma como as organizações de uma UF se ligam às unidades do MDS (pool denso × rede esparsa), medido pela participação de pool. A ligação com a rota de montagem (MOC Título 30, itens 35.3 e 36.2) é inferência, não medida (D-8).
- Rival explanation and discriminating observation: a escassez (razão unidades/organizações) prevê que a classe acompanhe a razão; a persistência prevê que a classe se mantenha quando a razão muda. A observação discriminante são as UFs discordantes. Segundo rival: a inércia dos mesmos vínculos (K5, T2).
- What this design can distinguish; remaining uncertainty: distingue "persistente na UF" de "segue a razão do ano". Não distingue rota administrativa de outras características estáveis da UF. Com poucas UFs discordantes, a decisão é frágil.

## H2

Estimand: E2
Primary test: T6
Mode: exploratory
Generated from: DATA1

### Design

Claim type: associational
Population: organizações CDS com ≥ 1 código vinculado e kg previsto > 0 em DATA1, em UFs com ≥ 2 dessas organizações.
Exposure: log do kg previsto somado nos projetos CDS da organização.
Outcome: log do grau registrado (T6); log do grau previsto (T7, especificação descritiva).
Contrast: elasticidade dentro da UF (efeitos fixos de UF).
Time: 2025 (DATA1).
Identification: nenhuma. É descrição exploratória em dado já exposto (D-2).
Dependence: organizações da mesma UF compartilham unidades e regime. O erro-padrão é agrupado por UF (CR1) e o IC usa t com G − 1 graus de liberdade. Com poucas UFs, o IC é aproximado e só descritivo.

### Decision rule

CONFIRMED when: nunca. H2 é exploratória (D-9) e o seu estado terminal é NOT_VERIFIED.
REFUTED when: nunca. H2 é exploratória (D-9).
INCONCLUSIVE when: não se aplica como decisão. O resultado de T6 é relatado como descrição de DATA1.

### Assumptions

| ID | Assumption | Check | Failure action |
|---|---|---|---|
| A1 | O kg previsto mede uma capacidade de oferta exógena à demanda das unidades atribuídas | K1 | não verificável: pelo MOC item 37, a proposta é montada para atender à demanda das cozinhas, e o kg não é comparável entre produtos. H2 fica NOT_VERIFIED e T6 não sustenta mecanismo |

### Primary analysis

Test: T6
Estimator: MQO de log(grau) em log(kg) após centrar ambos na média da UF (`pesquisa/scripts/h2_exploratorio.py`).
Inference: erro-padrão CR1 agrupado por UF; IC de 95% com t(G − 1). Descritivo.
Why this estimates E2: dentro da UF, a inclinação log–log é a elasticidade média do grau em relação ao kg previsto entre organizações. É uma descrição, não um mecanismo (A1).

### Sensitivity

- T7: grau previsto como desfecho, porque a perda previsto→registrado se concentra nos projetos grandes (D-7).

### Specification dimensions

- none

### Interpretation boundary

May claim: a elasticidade estimada em DATA1 e o seu IC aproximado, como descrição exploratória; a perda previsto→registrado por faixa de tamanho.
May not claim: que a oferta "se dilui" por atribuição de unidades, ou que a capacidade empurra o grau; qualquer confirmação; generalização para outros anos.
