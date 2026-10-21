# REVIEW-3

- Revisor: `reviewer-2` (contexto separado, sem edição), invocado em 2026-10-21
- Commit revisado: `9f123f4`
- Manuscrito: `pesquisa/texto/artigo.md`
- Veredito: **PASS**
- Separação: só procedimental; não é revisão independente por especialista.

## Status da REVIEW-2

N1, N2, N3, N4, N5, N7, N8, N10, N11, N12 e N15: resolvidos. N6: parcial (achado 1). N9: resolvido no texto, mas o número citado usa a regra antiga (achado 2). N13: declarado; a resolução online das citações não foi verificada pelo revisor. N14: resolvido em parte (achado 3).

## Verificações do revisor

O teste sintético reproduz `resultado.txt` byte a byte. RUN-5 e RUN-6 regeneram byte a byte. Numa execução de ponta a ponta com DATA2 sintético de 2024, em que BA, PI e SE saem da faixa, o resultado foi CONFIRMED 3/3 com p = 0,125, e T2 a T5 e K5 rodaram. O validador deu PASS nas subchecagens e NOT_VERIFIED no global (disclosure, citations). Os três REOPENs são legítimos. A linhagem de C1 a C8 confere com R3 e R6. Os trechos do MOC conferem com o PDF. Não há exposições não declaradas, e o caráter exploratório é respeitado.

## Achados novos (todos menores)

| Id | Local | Achado | Menor correção |
|---|---|---|---|
| 1 | h1_confirmatorio.py `hash_esperado` | Com `DATA2.sha256` vazio ou parcial o script decide sem conferir os dois hashes, e a falha de hash não sai como BLOCKED | exigir as duas entradas; prefixar com "BLOCKED (K1)"; testar |
| 2 | artigo.md Resumo; §4 | O 0,57 do PR é da regra anterior à D-16; com a regra nova, a fração exclusiva é 0,54. A frase do §4 sobre o escopo da exclusão do marcador está incompleta | usar o valor da regra nova ou declarar; ajustar o §4 |
| 3 | artigo.md §5.3 (C4) | "Os demais ramos foram exercitados com dados sintéticos" excede o teste commitado (falta o ponta a ponta com discordantes, K3, K2 < 6, hash divergente, T2 a T5 com discordantes) | reduzir a afirmação ou ampliar o teste |
| 4 | protocolo.md:31; registro.md:8; analysis-plan.md (Population); artigo.md §7 | O enunciado de H1 ainda é o anterior à D-17. "Utilizável" tem dois sentidos. "Notícias de 2025 e 2026" omite que o ano da notícia do RS não foi verificado | alinhar |
| 5 | analysis-plan.md:44; D-17 | "Um CONFIRMED refuta a escassez para qualquer limiar" vai além do May claim | "um CONFIRMED não depende do ponto escolhido dentro da faixa" |
| 6 | artigo.md §1 | "Desde dezembro de 2023" afirma prioridade que a fonte (resumo) não sustenta | "ao menos desde" |
| 7 | analysis-plan.md (Consequência) | Uma UF de pool só pode ficar discordante (razão ≤ 1,45 com ≥ 10 unidades) se tiver ≥ 7 organizações; a assimetria não está declarada | uma frase |
