# REVIEW-5

- Revisor: `reviewer-2` (contexto separado, sem edição), invocado em 2026-10-21
- Commit revisado: `0a19762` (diff f0a8c93..0a19762 e manuscrito inteiro, já descritivo)
- Veredito: **FAIL** (um achado material)
- Separação: só procedimental.

Os números de C1–C9 (incluindo a Tabela 1) conferem com R3 e R6, que regeneram EXACT. As citações do MOC e da ata conferem com os PDFs.

| Id | Severidade | Achado | Menor correção |
|---|---|---|---|
| F1 | material | §5.3, §6, §8 e Resumo descrevem as UFs esparsas como aquelas em que "cada organização atende poucas cozinhas" e os vínculos "se espalham". Os próprios dados contradizem: vínculos por organização PI 5,57 e BA 4,54 contra SC 5,50 e PE 4,71; organizações por unidade PI 4,33 e BA 3,52 contra PB 2,46, SC 2,20 e PE 2,36; fração de unidades com ≥ 2 organizações PI 0,85 e BA 0,84 contra SC 0,70 e PE 0,64. Além disso, a densidade ≥ 0,5 exige, num componente com O organizações, ≥ O/2 organizações por unidade em média. A classe pool fica mais difícil com mais organizações, e o nº de organizações separa os grupos tão bem quanto a razão. A "coincidência com a escassez" é em parte construída pela métrica, e o §6 omite essa explicação | descrever o contraste como cobertura da UF por organização; informar vínculos por unidade e a densidade do componente principal; declarar a dependência da métrica em relação ao tamanho |
| F2 | moderado | "Unidades habilitadas" e "escassez" sugerem demanda e oferta não medidas; a razão não está definida na §4 | "unidades vinculadas"; definir a razão |
| F3 | moderado | A §4 diz "sem inferência amostral", mas a §5.5 tem IC agrupado; E2 não está no escopo descritivo da D-22 | alinhar |
| F4 | menor/moderado | O manuscrito não diz que o estudo passou de explicativo a descritivo; foram removidas as ressalvas da versão de 2024 do manual, do registro interno reaberto três vezes e do corte ajustado aos dados | restaurar |
| F5 | menor | MG não é "sobreposta": 9 das 10 unidades têm um único fornecedor | descrever MG à parte |
| F6 | menor | Números do Resumo (0,55–0,82; MG 0,23; PR "mais da metade") vêm de `problema.csv`, sem anotação e com a regra antiga do marcador | levar ao corpo com fonte |
| F7 | menor | O título do protocolo ainda é "Por que…"; E3–E5 não estão em "Estimandos" nem no plano | ajustar |
| F8 | menor | `publicacao.md` e o gate 7 apontam para o manuscrito e a revisão anteriores | marcar como pendentes |
