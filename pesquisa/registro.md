# Registro interno — cozinhas: regime de alocação por UF

Tipo: registro interno, versionado no git. **Não é um registro externo** (OSF, AsPredicted etc.). Este documento se congela no mesmo commit do protocolo e do plano (D-10). O commit e a sua data são a única prova de precedência, e o git não prova ausência de exposição fora dele (D-2).

Derivado de `pesquisa/protocolo.md` e `analysis-plan.md`; em caso de divergência, valem esses dois.

1. **Pergunta.** O grau alto das organizações em algumas UFs vem de um regime de alocação persistente na UF ou da escassez local de organizações?
2. **Hipótese confirmatória H1.** Nas UFs utilizáveis que em 2025 (DATA1) estavam do lado da faixa de escassez correspondente à sua classe e cuja razão unidades/organizações, no ano confirmatório, sai da faixa (1,45; 2,00) para o lado oposto, o regime do ano confirmatório segue o de 2025 (D-17).
3. **Dado confirmatório.** DATA2: a planilha CONAB do PAA–Cozinhas de outro ano, com o mesmo esquema. Não identificado na data do registro; nenhum conteúdo de DATA2 foi visto. Números de notícias de 2026 foram vistos (`pesquisa/literatura/busca.md`).
4. **Desfecho.** Classe de regime da UF (pool se a participação de pool for ≥ 0,5; D-6).
5. **Preditores congelados.** A classe de cada UF em DATA1 (tabela em `analysis-plan.md#h1`) e a faixa de escassez: lado pool com razão ≥ 2,00, lado esparsa com razão ≤ 1,45 (D-17).
6. **Teste primário T1.** Contagem nas UFs discordantes. Discordante é a UF que sai da faixa para o lado oposto ao da sua classe (D-17); o PI sai se o ano confirmatório for 2026 (D-16); o PR é herdado e relatado à parte. CONFIRMED com ≥ 3 discordantes e ≥ 75% de acertos da persistência; REFUTED com ≥ 75% de acertos da escassez; INCONCLUSIVE nos demais casos.
7. **Checagens K1 a K7 e sensibilidades T2 a T5** como no plano. K7 foi acrescentada por REOPEN antes de qualquer DATA2 (D-12). O filtro de ano, a exclusão de projetos já vistos, a regra de código, a normalização do CNPJ e o hash esperado vieram da D-16. Só T1 decide.
8. **Hipótese exploratória H2.** Elasticidade grau–kg em DATA1; nunca confirmatória.
9. **Código.** `pesquisa/scripts/h1_confirmatorio.py`, congelado com este registro.
