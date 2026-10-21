# Como as organizações fornecedoras se ligam às cozinhas solidárias no PAA: um retrato dos vínculos em 2025

Manuscrito de trabalho, **descritivo**. Autoria, venue e licença: a definir (decisão humana).

## Resumo

Descrevemos como as organizações fornecedoras de projetos de Compra com Doação Simultânea (CDS) do PAA–Cozinhas, executado pela CONAB, se ligam às unidades recebedoras. Usamos a planilha pública da CONAB de 2025, num snapshot congelado. O estudo foi desenhado como explicativo e passou a descritivo, porque não há um segundo ano de dados para testar explicações.

**Grau.** A organização típica atende 2 unidades, a média é 3,42 e o máximo é 23.

**Variação entre UFs.** Nas onze UFs com ao menos dez unidades vinculadas e três organizações, o nº médio de vínculos por organização vai de 1,86 (MG) a 11,83 (AL), e é mais alto em AL, PB e RN. Ele é o produto de dois fatores: unidades vinculadas por organização e organizações por unidade.

**Compartilhamento.** O compartilhamento de unidades entre organizações é comum: na maioria dessas UFs, mais da metade das unidades tem dois ou mais fornecedores. É raro só em PR e MG.

**O indicador de pool.** O que mais distingue as UFs é a fração das unidades da UF que cada organização cobre: de 0,12 a 0,82. Ela é alta nas UFs com poucas organizações. Um indicador de "pool" baseado em densidade acompanha esse tamanho da rede e não deve ser lido como um regime próprio da UF.

**Registro.** Faltam como registradas 0,315 das unidades previstas nas propostas, sobretudo nos projetos grandes.

**O que fica em aberto.** Por que a estrutura varia entre UFs. O manual de operações da CONAB, na versão de 2026, prevê formas diferentes de montar os fornecedores de uma cozinha, mas não lemos a versão vigente em 2025, e nenhuma fonte diz qual forma cada UF usou.

## 1. Introdução

O Programa de Aquisição de Alimentos (PAA) compra alimentos de organizações da agricultura familiar e os doa a unidades recebedoras. Há regras específicas para as compras destinadas às cozinhas solidárias ao menos desde dezembro de 2023 (Resolução PAA/GG nº 7/2023, lida só por resumo), e o manual de operações da CONAB tem um subtítulo próprio para elas, o PAA–Cozinhas.

A literatura sobre o PAA privilegia o lado do fornecedor. Um trabalho sobre unidades recebedoras afirmava, em 2015, não haver estudos sobre elas (Silva e De Lorenzo, 2015; somente resumo lido). Nas bases consultadas, não encontramos estudo sobre a **estrutura dos vínculos** entre organizações e unidades (`pesquisa/literatura/fontes.md#lacuna`). A busca não incluiu SciELO, BDTD nem relatórios institucionais diretamente.

O estudo começou com uma pergunta explicativa: por que algumas organizações atendem muito mais unidades? Testá-la exigiria um segundo ano de dados, que a planilha ainda não tem. Por decisão de quem conduz a pesquisa, o trabalho passou a descritivo (`pesquisa/decisoes.md`, D-22). A pergunta descritiva é:
- quantas unidades cada organização atende;
- como os vínculos se organizam em cada UF;
- quanto do previsto nas propostas aparece registrado.

## 2. A regra documentada

O Manual de Operações da CONAB, Título 30, subtítulo IV, na versão de 14/05/2026, estabelece que o MDS apresenta à CONAB "uma lista das Cozinhas Solidárias cadastradas e habilitadas" (item 35). Pelas disposições gerais, a organização fornecedora cadastra as unidades recebedoras e elabora a proposta (itens 3.1 e 3.2). O manual não diz quem atribui cada unidade da lista a cada organização. <!-- rm:ignore: números de item normativo -->

Para formar os fornecedores de uma cozinha, o manual prevê três formas:
- **chamada aberta:** a CONAB pode abrir chamada sobre a demanda mapeada, e são contratados os projetos que "se declarem aptos com a demanda da cozinha" (itens 36.2 e 37); <!-- rm:ignore: números de item normativo -->
- **indicação pela cozinha:** as cozinhas podem "indicar potenciais organizações fornecedoras" (item 35.3); <!-- rm:ignore: número de item normativo -->
- **compra direcionada:** em casos específicos, segundo orientações do MDS (item 36.3). <!-- rm:ignore: número de item normativo -->

Lemos só a versão de 2026. Uma versão anterior (Ato Dipai nº 05/2024) foi localizada, mas não lida, e não verificamos qual versão regia as contratações de 2025. A ata do GGPAA de 29/01/2025 registra que a contratação para cozinhas em 2025 seria feita "em formato ainda a ser apresentado". <!-- rm:ignore: identificação de ato normativo -->

## 3. Dados

**Fonte.** A planilha pública da CONAB/GEIAF do PAA–Cozinhas, período 2025. É uma planilha única, atualizada à medida que a CONAB acrescenta dados. Usamos um snapshot de 2026-10-14 com hash registrado (`pesquisa/dados/relatorio.md`; números de `pesquisa/agregados/dados.csv`).

**Tamanho e ligação.** A planilha traz 280 projetos de 240 organizações (CNPJ) e 1116 linhas de unidades recebedoras. Todas as linhas de unidades encontram projeto, e 0,921 dos projetos têm ao menos uma unidade.

**Recorte.** CDS, o mecanismo em que a organização entrega diretamente: 219 projetos, 206 organizações com vínculo e 705 vínculos distintos (CNPJ, código da cozinha).

**Medida.** O **código da cozinha** registrado, não a cozinha física. 682 vínculos usam códigos CS, 22 usam códigos EG (que reúnem mais de uma cozinha) e 1 usa o marcador "unidade gestora", que não identifica unidade.

**Universo.** A planilha só traz as unidades **vinculadas** a algum projeto, não o universo das cozinhas habilitadas pelo MDS.

## 4. Métodos

Medidas por organização e por UF (UF da organização):
- **Grau:** nº de códigos distintos vinculados aos projetos CDS da organização.
- **Unidades por organização:** códigos vinculados na UF ÷ organizações da UF.
- **Vínculos por organização:** o grau médio da UF. É igual a unidades por organização × organizações por unidade.
- **Organizações por unidade:** quantos fornecedores cada unidade tem, em média, e a fração de unidades com dois ou mais.
- **Cobertura média:** a fração das unidades da UF que uma organização atende, em média, isto é, vínculos ÷ (organizações × unidades).
- **Participação de pool** (D-6): a fração dos vínculos em componentes conexos com duas ou mais organizações e densidade de pelo menos metade dos pares possíveis. Num componente com O organizações, essa densidade exige que cada unidade tenha, em média, ao menos O/2 fornecedores. Por isso o indicador fica mais difícil de atingir quanto maior a rede. <!-- rm:ignore: limiar de método -->
- **Perda:** a fração das unidades previstas na proposta que não aparecem registradas.

**Regra do marcador.** Nos resultados por UF, os vínculos com o marcador "unidade gestora" não entram. Nos resultados nacionais (seção 5.1 e a perda total), entram; há um único vínculo assim.

**Natureza dos números.** São um censo do snapshot. As escolhas de medida foram feitas depois de examinar os dados, e isso está registrado (D-2). A elasticidade da seção 5.4 traz um intervalo agrupado por UF, que deve ser lido como medida descritiva da variação entre UFs, não como inferência para uma população.

As execuções têm recibo (`.research/runs/RUN-3.json`, `RUN-6.json` e `RUN-7.json`) e se regeneram byte a byte a partir do código.

## 5. Resultados

### 5.1 Quantas unidades cada organização atende

Entre as 206 organizações CDS com vínculo, a mediana do grau é 2 e a média é 3,42; nove em cada dez organizações atendem até 9 unidades, e o máximo é 23. A proporção de organizações com uma única unidade é 0,466. <!-- claim:C1 result:R3 -->

### 5.2 Como os vínculos se organizam por UF

**Tabela 1.** UFs com ao menos dez unidades vinculadas e três organizações, projetos CDS, 2025 (`pesquisa/agregados/descricao_uf.json`).

| UF | Organizações | Unidades | Vínculos | Unidades por organização | Vínculos por organização | Organizações por unidade | Unidades com ≥ 2 organizações | Cobertura média | Participação de pool |
|---|---|---|---|---|---|---|---|---|---|
| AL | 6 | 18 | 71 | 3,00 | 11,83 | 3,94 | 0,94 | 0,66 | 1,00 |
| PB | 3 | 13 | 32 | 4,33 | 10,67 | 2,46 | 0,92 | 0,82 | 1,00 |
| RN | 5 | 10 | 35 | 2,00 | 7,00 | 3,50 | 1,00 | 0,70 | 1,00 |
| SC | 4 | 10 | 22 | 2,50 | 5,50 | 2,20 | 0,70 | 0,55 | 1,00 |
| PE | 7 | 14 | 33 | 2,00 | 4,71 | 2,36 | 0,64 | 0,34 | 0,88 |
| PI | 21 | 27 | 117 | 1,29 | 5,57 | 4,33 | 0,85 | 0,21 | 0,03 |
| BA | 24 | 31 | 109 | 1,29 | 4,54 | 3,52 | 0,84 | 0,15 | 0,05 |
| RS | 20 | 29 | 72 | 1,45 | 3,60 | 2,48 | 0,76 | 0,12 | 0,31 |
| SE | 9 | 12 | 22 | 1,33 | 2,44 | 1,83 | 0,58 | 0,20 | 0,00 |
| MG | 7 | 10 | 13 | 1,43 | 1,86 | 1,30 | 0,10 | 0,19 | 0,00 |
| PR | 5 | 12 | 13 | 2,40 | 2,60 | 1,08 | 0,08 | 0,22 | 0,46 |

<!-- claim:C9 result:R7 -->

**Grau por UF.** O nº de vínculos por organização vai de 1,86 (MG) a 11,83 (AL). É mais alto em AL, PB e RN, que combinam de 2,00 a 4,33 unidades vinculadas por organização com, em média, de 2,46 a 3,94 fornecedores por unidade. <!-- claim:C3 result:R7 -->

**Compartilhamento.** Compartilhar unidades é comum. Na maioria das UFs, mais da metade das unidades tem dois ou mais fornecedores, e no PI e na BA (4,33 e 3,52 organizações por unidade) o compartilhamento é tão alto quanto em AL e RN (3,94 e 3,50). O compartilhamento é raro só em MG (0,10 das unidades com dois ou mais fornecedores) e no PR (0,08). Nessas duas UFs, a maior parte das unidades tem um único fornecedor. <!-- claim:C10 result:R7 -->

**Cobertura e tamanho da rede.** O que mais separa as UFs é a fração das unidades da UF que cada organização cobre: de 0,55 a 0,82 em AL, PB, RN e SC (de 3 a 6 organizações), 0,34 em PE e de 0,12 a 0,22 nas demais. A participação de pool acompanha essa cobertura (correlação de postos 0,825 entre as onze UFs). Ela tem associação negativa com o nº de organizações (−0,745) e positiva com unidades por organização (0,848). Pelo modo como é definida (seção 4), a participação de pool é em boa parte um reflexo do tamanho da rede. Não a interpretamos como um "regime" próprio da UF. <!-- claim:C2 result:R7 -->

### 5.3 Quanto do previsto aparece registrado

Em nenhum projeto CDS o nº de unidades registradas passa do previsto na proposta. No conjunto, faltam como registradas 0,315 das unidades previstas. A perda cresce com o tamanho do projeto: é de 0,01 nos projetos que previam uma unidade e de 0,455 nos que previam dez ou mais, que registram 321 das 589 unidades previstas. <!-- claim:C5 result:R3 -->

Entre as UFs da Tabela 1, a perda passa de 0,3 em PE (0,67), RS (0,61) e MG (0,32). <!-- claim:C6 result:R6 -->

Como a planilha é atualizada à medida que dados são acrescentados, parte dessa perda pode ser atraso de registro. Com um só snapshot, não é possível separar atraso de corte. Os projetos e as UFs com grau alto são justamente os mais afetados.

### 5.4 Grau e quantidade prevista

Dentro da UF, a elasticidade do grau registrado em relação ao kg previsto é de 0,291, com intervalo de 0,058 a 0,524 (erro-padrão agrupado por UF, leitura descritiva). Com o grau previsto, é de 0,371 (0,135 a 0,608). <!-- claim:C7 result:R3 -->

Organizações com mais quantidade prevista atendem mais unidades, mas bem menos que proporcionalmente. A proposta é montada para atender à demanda das cozinhas (item 37 do manual), e o kg não é comparável entre produtos. Por isso essa associação não indica mecanismo. <!-- rm:ignore: número de item normativo -->

## 6. Discussão e o que fica em aberto

O grau alto de AL, PB e RN vem de duas coisas ao mesmo tempo: poucas organizações para as unidades vinculadas e unidades com vários fornecedores. Nas UFs com muitas organizações (PI, BA, RS), cada organização atende um número de unidades parecido com o de SC e PE, e as unidades são até mais compartilhadas. O que muda é que cada organização cobre uma fração pequena das unidades da UF. MG e PR são diferentes: quase todas as unidades têm um único fornecedor.

Por que a estrutura varia entre UFs fica em aberto. Três leituras são compatíveis com os dados:
- a escassez de organizações em relação às unidades vinculadas;
- a forma de montar as propostas em cada UF (chamada aberta, indicação pela cozinha ou compra direcionada, pelo manual);
- o efeito do tamanho da rede sobre as próprias medidas, que explica boa parte da variação do indicador de pool.

Os dados de um só ano não separam essas leituras, e nenhuma fonte lida diz qual forma de montagem cada UF usou.

Durante a pesquisa, registramos e congelamos no repositório um teste para quando a planilha trouxer outro ano (`analysis-plan.md#h1`, `pesquisa/registro.md`). O registro é interno e foi reaberto três vezes antes de qualquer dado novo. Esse teste usa a participação de pool como desfecho e, pela dependência dessa medida em relação ao tamanho da rede, precisa ser refeito com uma medida ajustada por tamanho antes de ser usado (D-23).

## 7. Limitações

- **Um único ano.** As escolhas de medida foram feitas depois de examinar os dados, e o estudo foi redesenhado de explicativo para descritivo. A descrição vale para o snapshot de 2025.
- **Medida.**
  - Conta códigos registrados, não cozinhas físicas, e os códigos EG reúnem várias cozinhas.
  - No PR, 0,231 dos vínculos usam códigos EG. Só com códigos CS, o PR tem 3,33 unidades por organização e participação de pool de 0,00. <!-- claim:C8 result:R6 -->
  - A planilha só traz unidades vinculadas, não o universo das cozinhas habilitadas; "unidades por organização" não mede demanda.
- **Indicador de pool.** Depende do tamanho da rede (seção 4). As comparações entre UFs devem se apoiar nas medidas que não dependem dele (vínculos por organização, organizações por unidade).
- **Registro.**
  - É incompleto, sobretudo nos projetos grandes e em PE, RS e MG.
  - A planilha muda com o tempo; outro snapshot pode dar números diferentes.
- **Vínculos interestaduais.** Em SE e MG, mais de 5% dos vínculos vão para unidades de outra UF. <!-- rm:ignore: limite da checagem K4 -->
- **Fontes lidas.**
  - A regra lida é a versão de 2026 do manual; a vigente em 2025 não foi lida.
  - A Resolução PAA/GG nº 7/2023 e a literatura acadêmica foram lidas só por resumo.
- **Exposição.** Números de notícias de 2025, de 2026 e de ano não verificado foram vistos durante a pesquisa (`pesquisa/literatura/busca.md`).

## 8. Conclusão

Em 2025, a maioria das organizações fornecedoras do PAA–Cozinhas atende poucas unidades, e poucas atendem muitas. O grau é mais alto em AL, PB e RN, onde há poucas organizações para as unidades vinculadas e as unidades têm vários fornecedores. Compartilhar unidades é comum em nove das onze UFs analisadas; só em MG e no PR as unidades costumam ter um único fornecedor. A diferença mais visível entre UFs, a fração das unidades que cada organização cobre, acompanha o tamanho da rede. Cerca de um terço das unidades previstas nas propostas não aparece registrado. Por que a estrutura varia entre UFs fica em aberto.

## Referências

- CONAB. Manual de Operações, Título 30 — Compra com Doação Simultânea (CDS). Ato de Direção Dipai nº 03, de 14/05/2026. <!-- rm:ignore: número do título normativo -->
- GGPAA. Ata de reunião de 29/01/2025.
- GGPAA. Resolução PAA/GG nº 7, de 4 de dezembro de 2023 (lida por resumo).
- Silva, J. B.; De Lorenzo, H. C. (2015). Análise do Programa de Aquisição de Alimentos (PAA) a partir de unidades recebedoras em municípios da Região Administrativa Central do Estado de São Paulo (somente resumo).

As demais fontes consultadas e o nível de leitura estão em `pesquisa/literatura/fontes.md` e `pesquisa/referencias.bib`.

## Declarações

- **Dados e código:** `pesquisa/dados/`, `pesquisa/scripts/`, `pesquisa/agregados/` e `.research/runs/`. A licença de reuso da planilha da CONAB não foi verificada.
- **Uso de IA:** a análise, o código e este texto foram produzidos com assistência de um modelo de linguagem (Claude). A forma da declaração exigida pela venue é decisão humana.
