# REVIEW-2

- Revisor: `reviewer-2` (contexto separado, sem edição), invocado em 2026-10-21
- Commit revisado: `fbe8629`
- Manuscrito: `pesquisa/texto/artigo.md`
- Veredito: **FAIL**
- Separação: só procedimental; não é revisão independente por especialista.

## Status da REVIEW-1

F1, F2, F4, F5, F6, F7, F9, F10 e F13: resolvidos. F3: resolvido no que foi pedido, mas "separa" continua forte demais (ver N1). F8: resolvido, com ressalvas menores (N5, N6, N7). F11: resolvido em parte (N9). F12: resolvido; a refutação da seção 3 é aceitável, porque os agregados de dados se regeneram EXACT, mas a afirmação sobre a versão de 2024 continua em outros arquivos (N8).

## Verificações do revisor

O validador deu PASS nas subchecagens e NOT_VERIFIED no resultado global (disclosure, citations). O replay por execução direta deu EXACT em RUN-2 a RUN-5; `dados.py`, `problema.py` e `checa_fonte.py` regeneraram EXACT. Um DATA2 sintético exercitou cruzamento, exposição do PI, exclusão de projetos e PR herdado, e tudo funcionou como especificado. As citações do MOC e da ata conferem com os PDFs. Os REOPENs da D-12 e da D-16 são procedimentalmente legítimos (antes de qualquer DATA2).

## Achados novos

| Id | Severidade | Local | Achado | Menor correção |
|---|---|---|---|---|
| N1 | material | analysis-plan.md (limiar, T4, May claim); artigo.md Resumo, §6, §8 | 1,725 é arbitrário dentro de (1,45; 2,00], faixa que DATA1 não identifica. T4 só testa pontos dentro da faixa. O RN está em 2,00, e uma pequena queda o torna discordante. Como as participações de DATA1 estão nos extremos, pequenos cruzamentos favorecem a persistência. Um CONFIRMED só refutaria "escassez com limiar 1,725" | (a) contar só a UF que sai da faixa para o lado oposto; ou (b) exigir que T4 nas bordas concorde; ou (c) estreitar o May claim e a redação |
| N2 | material | artigo.md Resumo e Conclusão | "Praticamente o mesmo conjunto" e "quase todas atendem o mesmo conjunto" são contrariados pela densidade do componente principal (0,55 a 0,82) e pelo PE com quatro componentes | reescrever com as densidades |
| N3 | menor | artigo.md §7 | "T5 não muda a leitura do PR no ensaio" não aparece em R5; a base é R4, já superado | citar ou incluir o PR só-CS na saída |
| N4 | menor | analysis-plan.md | A linha do PR (0,46; 2,40) vem de R5, não de `problema.csv` | apontar a fonte certa |
| N5 | menor | h1_confirmatorio.py | ANO não está nas colunas de K1, e falta dá KeyError em vez de BLOCKED; códigos descartados pela regex somem sem relato | incluir ANO; relatar a fração descartada |
| N6 | menor | h1_confirmatorio.py; respostas F8e | O hash é conferido só contra o argumento, e nada o liga a um bloco commitado antes da abertura | ler o hash de arquivo commitado |
| N7 | menor | h1_confirmatorio.py `perda` | A perda conta o marcador "unidade gestora" como registrado | aplicar a regra de código em `perda` |
| N8 | menor | decisoes.md D-8; fontes.md; busca.md | "Ato Dipai 05/2024, vigente em 2025" continua sem fonte | nota de correção |
| N9 | menor | artigo.md Resumo | "Fora do PR, territórios exclusivos são raros": MG tem 0,23 | qualificar MG |
| N10 | menor | artigo.md §5.3 | "Dez das onze" é em amostra, com limiar ajustado a 2025 | dizer isso |
| N11 | menor | h1_confirmatorio.py (K2) | K2 conta o PR, que nunca pode ser discordante | declarar ou descontar |
| N12 | menor | relatorio.md | "notícias de 2026 (PI, RS)", mas o ano da notícia do RS não foi verificado | corrigir |
| N13 | menor | REVIEW-1-respostas.md | Lista as subchecagens em PASS e omite que o resultado global é NOT_VERIFIED | declarar |
| N14 | menor | RUN-5 | O ensaio não exercita os ramos novos da D-16, e não há teste sintético commitado | commitar teste sintético |
| N15 | menor | artigo.md §1 | "Desde 2024 há uma vertente…" sem citação | citar |
