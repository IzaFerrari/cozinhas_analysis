# Respostas à REVIEW-2

Revisão: `.research/reviews/REVIEW-2.md` (commit revisado `fbe8629`, veredito FAIL). Aplicadas nos commits depois de fab3ee7.

| Achado | Resposta | Onde |
|---|---|---|
| N1 | **Corrigido no desenho (REOPEN, D-17), pelo caminho (a).** A escassez passa a ter três estados: pool com razão ≥ 2,00, esparsa com ≤ 1,45, indeterminado entre os dois. Discordante é a UF que sai da faixa para o lado oposto ao da sua classe. 1,725 passa a ser só sensibilidade (T4: 1,60, 1,725, 1,85). O May claim e a redação do artigo foram estreitados para "nas UFs cuja razão saiu da faixa para o lado oposto" | analysis-plan.md H1; h1_confirmatorio.py `lado_faixa`, `decidir`; artigo.md Resumo, §6, §8 |
| N2 | **Corrigido.** "Compartilham boa parte das mesmas unidades (densidade do componente principal de 0,55 a 0,82; PE em quatro componentes)" | artigo.md Resumo, §8 |
| N3 | **Corrigido.** A saída inclui o PR herdado na variante só-CS (R6: razão 3,33, pool 0,00), e a frase cita R6 (C8) | h1_confirmatorio.py; artigo.md §7 |
| N4 | **Corrigido.** A linha do PR aponta para R5; as demais, para `problema.csv` | analysis-plan.md |
| N5 | **Corrigido.** `ANO` entrou nas colunas de K1, e a fração descartada pela regra de código é relatada por UF (`descartados_por_uf`) | h1_confirmatorio.py; teste "sem coluna ANO: BLOCKED (K1)" |
| N6 | **Corrigido.** O hash esperado é lido de `pesquisa/dados/DATA2.sha256`, que precisa ser commitado antes de abrir e, portanto, antes do execution freeze. Sem o arquivo, BLOCKED | h1_confirmatorio.py `hash_esperado`; teste "sem arquivo de hash" |
| N7 | **Corrigido.** `perda` aplica a regra de código. K7 em DATA1 não muda (MG, PE, RS); a perda do PR passa a 0,188 | h1_confirmatorio.py; R6 |
| N8 | **Corrigido.** A D-17 registra a correção, e `fontes.md` e `busca.md` deixam de chamar a versão de 2024 de "vigente em 2025" | D-17; fontes.md; busca.md |
| N9 | **Corrigido.** "Salvo no PR (0,57) e, em parte, em MG (0,23)" | artigo.md Resumo |
| N10 | **Corrigido.** "Com um corte de razão ajustado aos próprios dados de 2025"; qualquer corte entre 1,45 e 2,00 dá o mesmo resultado | artigo.md §5.3 |
| N11 | **Corrigido.** K2 conta só as UFs utilizáveis não herdadas (`utilizaveis_K2`) | h1_confirmatorio.py; teste "PR herdado, fora de K2" |
| N12 | **Corrigido.** "2026 (PI), de ano não verificado (RS) e de 2025 (PR)" | relatorio.md |
| N13 | **Declarado.** O resultado global do validador é NOT_VERIFIED, por duas razões: `disclosure` sem piso (contagens de pessoas jurídicas de fonte pública; decisão de publicação na fase 8) e `citations` em modo offline. Online, 6 de 8 alvos resolvem; os dois PDFs do gov.br recusam o validador, e as cópias com hash estão no repositório | este arquivo |
| N14 | **Corrigido.** `pesquisa/testes/teste_h1_sintetico.py` com 16 casos (regra de faixa, decisão, DATA2 sintético de 2026, BLOCKED por hash, rótulo, ANO e projetos já vistos), saída em `pesquisa/testes/resultado.txt` | pesquisa/testes/ |
| N15 | **Corrigido.** O texto cita a Resolução PAA/GG nº 7/2023 (lida por resumo) e o subtítulo PAA–Cozinhas do manual | artigo.md §1 |

Checagens refeitas: `validate_all.py --offline` (map, numbers, decisions, notebooks, plan, runs, lineage e exposure em PASS; resultado global NOT_VERIFIED, ver N13); teste sintético com 16 casos passando; RUN-6 com replay da ferramenta EXACT.
