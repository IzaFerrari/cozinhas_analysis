# REVIEW-6

- Revisor: `reviewer-2` (contexto separado, sem edição), invocado em 2026-10-21
- Commit revisado: `280ee95` (diff 0a19762..280ee95 e manuscrito inteiro)
- Veredito: **FAIL** (um achado material)
- Separação: só procedimental.

R3, R6 e R7 regeneram EXACT; as 99 células da Tabela 1 conferem com R7; C1–C10 têm linhagem completa. REVIEW-5: F1 resolvido no essencial (falta a densidade do componente principal), F2–F6 e F8 resolvidos, F7 parcial.

| Id | Severidade | Achado | Menor correção |
|---|---|---|---|
| F1 | material | §5.3: "Os projetos e as UFs com grau alto são justamente os mais afetados" é falso para as UFs: AL 0,11, PB 0,00, RN 0,00 têm a menor perda; PE, RS e MG, de grau médio ou baixo, a maior (postos perda × grau ≈ −0,62) | só os projetos grandes; perda maior em PE, RS e MG, não nas de grau mais alto |
| F2 | moderado | O superlativo "o que mais distingue as UFs é a cobertura" não tem critério e é falso pelas medidas óbvias. A cobertura = (organizações por unidade)/O também depende do tamanho, é a densidade do grafo da UF, e a correlação 0,825 com pool é em parte definicional | tirar o superlativo; declarar a identidade |
| F3 | moderado | "Cobertura alta nas UFs com poucas organizações" falha para PR (5 organizações, 0,22). "O grau alto de AL, PB e RN vem de duas coisas" só vale para AL: em PB pesa a razão, em RN o compartilhamento | "as UFs de cobertura alta têm de 3 a 6 organizações"; decompor por UF |
| F4 | moderado | "Medidas que não dependem do tamanho" é falso como absoluto (limitadas por O e U) | "não têm o limiar O/2, mas são limitadas por O e U" |
| F5 | moderado | PE, RS e MG (perda > 0,3) entram na Tabela 1 e na comparação da §6 sem ressalva | nota na tabela e ressalva na §6 |
| F6 | menor | Falta a densidade do componente principal | acrescentar |
| F7 | menor | `analysis-plan.md` l.5 e a linha Estimand do protocolo ainda usam a leitura antiga | alinhar |
| F8 | menor | IC agrupado chamado de "medida descritiva da variação entre UFs" | "aproximação; não interpretar como inferência" |
| F9 | menor | "Reaberto três vezes" omite os ajustes da D-18 e da D-23 | listar |
| F10 | menor | "Tão alto quanto em AL e RN" vale para organizações por unidade, não para a fração com ≥ 2 fornecedores | qualificar |
