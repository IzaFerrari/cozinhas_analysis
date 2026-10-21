# Respostas à REVIEW-1

Revisão: `.research/reviews/REVIEW-1.md` (commit revisado `3eefb73`, veredito FAIL). As respostas abaixo foram aplicadas nos commits que vêm depois de 4d039f1.

| Achado | Resposta | Onde |
|---|---|---|
| F1 | **Corrigido.** A frase foi retirada. O texto agora diz que a lista vem do MDS, que a organização cadastra as unidades e elabora a proposta (itens 3.1 e 3.2) e que o manual não diz quem atribui cada unidade a cada organização | artigo.md §2 |
| F2 | **Corrigido.** O Resumo declara a versão de 2026, que a versão vigente em 2025 não foi lida e que a ligação é inferência. A compra direcionada (item 36.3) foi incluída: o texto passa de "duas rotas" para "três formas" | artigo.md Resumo, §2 |
| F3 | **Corrigido.** O Resumo e a Conclusão dizem agora que o teste separa "padrão persistente na UF" de "padrão que segue a escassez do ano", que não distingue a rota de outras características estáveis da UF e que tende a ser inconclusivo | artigo.md Resumo, §6, §8 |
| F4 | **Corrigido no texto e no desenho.** "Qualquer" foi retirado, e o texto declara a posição do PI em relação ao limiar. Por REOPEN antes de DATA2 (D-16), o PI sai da população primária se DATA2 for 2026 | artigo.md §6; D-16 |
| F5 | **Corrigido.** A D-15 corrige a D-14. O relatório usa a fração por UF. A limitação de K6 no PR, com T5, entrou no manuscrito | D-15; relatorio.md; artigo.md §7 |
| F6 | **Corrigido.** A D-15 declara o que a D-12 omitiu (a ordem K7→K2 e a saída de PE e RS). A D-16 fixa uma ordem coerente: elegibilidade, K7, K3, exposição, K2 | D-15; D-16; analysis-plan.md A2 |
| F7 | **Corrigido no desenho (REOPEN, D-16).** Discordante passa a ser a UF cuja classe de escassez muda entre os anos. O PR, discordante já em 2025, é relatado à parte e não pode contar | analysis-plan.md H1; h1_confirmatorio.py `decidir` |
| F8 | **Corrigido no código (D-16).** (a) filtro de `ANO` e exclusão de projetos já em DATA1; (b) só códigos `CS<n>` e `EG<n>`; (c) K1 confere os rótulos de mecanismo e a existência de vínculos CDS, senão BLOCKED; (d) CNPJ normalizado; (e) sha256 esperado como argumento obrigatório, registrado no log antes de abrir. Ensaio em amostra RUN-5 (replay da ferramenta: EXACT) | h1_confirmatorio.py; RUN-5 |
| F9 | **Corrigido.** "Entre as UFs elegíveis" | artigo.md §5.4 |
| F10 | **Corrigido.** As esparsas vão de 1,29 a 1,43, e o RS fica como intermediário nas duas seções | artigo.md §5.2, §5.3 |
| F11 | **Corrigido.** BA, PI e SE com um componente grande; MG com quatro; "fora do PR" no Resumo | artigo.md Resumo, §5.2 |
| F12 | **Corrigido em parte.** (i) A versão de 2024 deixou de ser chamada de "vigente"; a ata de 2025 passou a ser citada no texto. (ii) "Verifica o código" foi reescrito, com a trivialidade de K5, T2 e T3 explícita. (iii) O xlsx atual e a checagem estrutural foram commitados (`pesquisa/dados/fonte_atual/`), e o relatório declara que o nº de linhas também foi lido. (iv) O replay manual tem script versionado (`pesquisa/scripts/replay_manual.sh`), que foi rodado de novo: EXACT em RUN-2, RUN-3 e RUN-4. **Rebatido:** os números da seção 3 são descrição de dados da fase 4 (`dados.csv`), não resultados materiais; ficam sem RUN, com a fonte citada | artigo.md §2, §3, §4, §5.3; relatorio.md |
| F13 | **Corrigido.** K4 por UF: SE e MG passam do limite | relatorio.md; D-15 |

Checagens refeitas: `validate_all.py --offline` (map, numbers, decisions, notebooks, plan, runs, lineage e exposure em PASS); replay de RUN-5 pela ferramenta (EXACT); replay manual de RUN-2, RUN-3 e RUN-4 (EXACT). A REVIEW-1 fica obsoleta diante destas mudanças; a REVIEW-2 revisa o novo commit.
