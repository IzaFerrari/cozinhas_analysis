# REVIEW-1

- Revisor: `reviewer-2` (contexto separado, sem edição), invocado em 2026-10-21
- Commit revisado: `3eefb73`
- Manuscrito: `pesquisa/texto/artigo.md`
- Veredito: **FAIL**
- Separação: só procedimental (outro contexto do mesmo modelo); não é revisão independente por especialista.

## Síntese do revisor

Os números do manuscrito batem com os agregados e com o código, e C1 a C7 têm linhagem completa (R3, R4). R2, R3 e R4 foram regenerados byte a byte a partir dos execution freezes. O REOPEN (D-12) e a retirada do RUN-1 (D-13) não escondem resultado. O FAIL vem de quatro coisas: redação além do que as fontes e o plano permitem, afirmações falsas na D-14 e na D-12, um desenho de H1 que não implementa a D-7, e falhas no código congelado para a execução em DATA2.

## Achados

| Id | Severidade | Local | Achado | Menor correção proposta |
|---|---|---|---|---|
| F1 | material | artigo.md:17 | "A seleção das unidades não é da organização fornecedora" não é sustentada pelo MOC. Os itens 3.1 e 3.2 (a organização cadastra as unidades e elabora a proposta) e os itens 36.2 e 37 (as organizações "interessadas" se declaram aptas) sugerem escolha dentro da lista do MDS | "a lista vem do MDS; o manual não diz quem atribui cada unidade a cada organização" |
| F2 | material | artigo.md:7 (Resumo) | O Resumo omite que a versão do manual é a de 2026, não verificada para 2025, e que a ligação rota→padrão é inferência. "Duas rotas" omite a compra direcionada (item 36.3) | acrescentar as duas ressalvas e o item 36.3 |
| F3 | material | artigo.md:7 e :76 | O Resumo diz que o teste "separa as duas explicações" e a Conclusão diz que "o desenho que decide está registrado". O teste não distingue rota de outras características estáveis da UF e é frágil com poucas UFs discordantes | "separa padrão persistente na UF de padrão que segue a escassez do ano" |
| F4 | material | artigo.md:7 e :59 | "Antes de qualquer dado independente" omite a consequência da exposição à notícia do PI 2026: o ponto médio 1,725 fica logo abaixo de cerca de 1,75, o que tende a tornar o PI discordante se DATA2 for 2026 | tirar "qualquer"; declarar a posição do PI; tratar por CHANGE_PLAN |
| F5 | material | decisoes.md:115 (D-14); relatorio.md:28 | "K6 fica abaixo de 20% em todas as UFs elegíveis" é falso: o PR tem 0,286 de vínculos não-CS. O relatório usou a fração nacional numa checagem por UF. O PR é a única UF discordante. T5 mantém o PR discordante | bloco novo corrigindo a D-14 e linha nas Limitações |
| F6 | material | decisoes.md:99 (D-12) | "Nada mais muda" é falso: K7 passou a valer antes de K2 (6 de até 8 UFs, não de 11), e K3 ficou depois de K2, numa ordem inconsistente. O REOPEN também remove as UFs mais próximas do limiar (PE 2,00; RS 1,45). Nenhuma das duas coisas foi declarada | bloco novo declarando ou revertendo a ordem |
| F7 | material | analysis-plan.md:21, :46; h1_confirmatorio.py:93-101 | "Discordante" não exige que a razão mude entre os anos. O PR já é discordante em DATA1; se ficar igual por inércia, conta como acerto da persistência. O T1 não implementa a exigência da D-7 | CHANGE_PLAN antes de DATA2: exigir que a razão cruze o limiar entre os anos |
| F8 | material | h1_confirmatorio.py | (a) não há filtro de ano nem de projetos já em DATA1; (b) "unidade gestora" vira nó compartilhado e cria pool espúrio; (c) K1 não confere o rótulo CDS, e um rótulo mudado sai INCONCLUSIVE em vez de BLOCKED; (d) o CNPJ não é normalizado; (e) o hash de DATA2 não é conferido contra valor pré-registrado | CHANGE_PLAN antes de DATA2 corrigindo as cinco |
| F9 | menor | artigo.md:49, :67 | "perda > 0,3 em PE, RS e MG" omite GO (0,59) e PA (0,74), que não são elegíveis | "entre as UFs elegíveis" |
| F10 | menor | artigo.md:38, :43 | O RS fica "entre os dois" na l.38 e entra nas esparsas na l.43 | tornar consistente |
| F11 | menor | artigo.md:39; Resumo | "Quase todos os vínculos num componente grande" não vale para MG (0,77). "Territórios exclusivos são raros" sem "fora do PR" | qualificar |
| F12 | menor | artigo.md:19, :28, :44, :61; relatorio.md:46 | Ato Dipai 05/2024 dito "vigente em 2025" sem fonte; a ata está nas referências e não é citada; "verifica o código" exagera (K5, T2 e T3 triviais com referência = alvo); o xlsx da fonte atual não está no repositório, e o relatório afirma o nº de linhas além da leitura declarada; "regeneram byte a byte" sem registro commitado da verificação manual; os números da seção 3 não têm RUN | corrigir a redação e commitar a evidência |
| F13 | menor | relatorio.md:29 | "K4 em DATA1: abaixo do limite" usa a fração nacional; por UF, SE (0,091) e MG (0,077) passam | corrigir |

## Não verificado pelo revisor

O xlsx atual da fonte, que não está commitado. Exposições fora do git. A diferença entre as versões de 2024 e 2026 do manual. A Resolução 7/2023 e os artigos, que só têm resumo.
