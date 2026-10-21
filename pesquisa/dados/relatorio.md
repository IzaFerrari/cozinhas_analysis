# Relatório de dados (fase 4)

Números de `pesquisa/agregados/dados.csv`, gerado por `pesquisa/scripts/dados.py`, que confere o sha256 de DATA1 antes de rodar.

## DATA1 — planilha CONAB PAA–Cozinhas, período 2025

- **Origem.** CONAB/DIPAI/SUPAF/GEIAF, planilha pública no Google Sheets (`1O_mmcnZ2QCBkA6juq_TzKYFv6KDwHsCU`). Abas exportadas em CSV: contratações (gid=1251522308) e unidades recebedoras (gid=225140418).
- **Versão.** Snapshot de 2026-10-14 14:22 (UTC−5), restaurado do commit 67cc73c (D-1). sha256 `480b46c4…31dbc` (contratações) e `6754d715…b102` (unidades). A fonte avisa que pode ser alterada a qualquer momento.
- **Uso e licença.** Dado público de órgão federal. A licença de reuso não está declarada na planilha: `NOT_VERIFIED`. As cópias brutas no repositório contêm nomes e CNPJs de organizações e de unidades, que são pessoas jurídicas. Não são usadas colunas sobre pessoas físicas. As contagens por perfil de agricultor não entram na análise.
- **Papel.** `discovery`, já exposto (D-2).

### Estrutura e duplicidades

- Contratações: 280 linhas, 280 projetos distintos e 240 CNPJs. Quatro CNPJs aparecem com mais de uma grafia de nome, por isso o agrupamento é sempre pelo CNPJ. Nenhum CNPJ aparece em mais de uma UF.
- Mecanismos: 219 projetos CDS, 32 CDAF e 29 CI.
- Unidades: 1116 linhas, sem código ausente, com 251 códigos distintos. Há 327 linhas que repetem o par (projeto, código), em geral vários nomes de consumidor sob o mesmo código. Por isso o vínculo é o par distinto (CNPJ, código).

### Ligação

- Chave: `N° DO PROJETO` = `Num TPAF`, comparação exata de texto.
- Todas as 1116 linhas de unidades encontram projeto. Dos 280 projetos, 258 (0,921) têm ao menos uma unidade. Os sem unidade são quase todos CDAF ou CI.
- Em CDS: 218 dos 219 projetos têm unidade; 207 organizações, das quais 206 com vínculo; 705 vínculos; 248 códigos distintos.
- Projetos por organização em CDS: 11 organizações têm mais de um projeto CDS. A Resolução PAA/GG nº 7/2023, lida só por resumo (N3), veda projetos **simultâneos** por organização para cozinhas. Projetos em sequência não são vedados, e a planilha não traz datas para distinguir. O grau soma todos os projetos CDS da organização.

### Medida

- **Grau.** Nº de códigos distintos vinculados aos projetos CDS do CNPJ. Mede unidades recebedoras **registradas**, não cozinhas físicas.
- **Granularidade.** Dos 705 vínculos CDS, 682 usam códigos CS, 22 usam códigos EG e 1 tem outro valor ("unidade gestora"). A fração não-CS é 0,033 (K6 de H1 em DATA1: abaixo do limite).
- **Interestaduais.** São 10 vínculos (0,014). Três códigos estão ligados a organizações de mais de uma UF (K4 em DATA1: abaixo do limite).
- **Previsto × registrado.** O previsto está preenchido em todos os projetos CDS. O registrado é igual ao previsto em 173 projetos, menor em 46 e nunca maior. A perda por faixa de tamanho está em `pesquisa/agregados/h2_data1.json` (fase 5).

### População analítica

- H1, para as classes de DATA1: as UFs com ≥ 10 códigos CDS vinculados e ≥ 3 organizações. São onze UFs (`pesquisa/agregados/problema.csv`).
- H2: as organizações CDS com vínculo e kg previsto > 0, em UFs com pelo menos duas dessas organizações.

### Revelação

Os documentos em `pesquisa/texto/` usam só agregados por UF ou nacionais, sem nomes de organizações. Não há piso de revelação no mapa (`floor`). As contagens se referem a pessoas jurídicas de fonte pública, não a pessoas; por isso o validador marca `disclosure` como `NOT_VERIFIED`. A publicação das cópias brutas depende de verificar a licença (fase 8).

## DATA2 — dado confirmatório: `BLOCKED`

Exigência (D-3, D-7, `analysis-plan.md#h1`): a mesma planilha de outro ano, com o mesmo esquema, sem exposição prévia ao conteúdo.

O que foi verificado em 2026-10-21, sem abrir desfechos:
- A versão atual do arquivo-fonte de DATA1 (exportação xlsx, sha256 `52a35d26…6bf`) só tem as abas `DADOS`, `PRODUTOS`, `CONTRATAÇÕES 2025` e `UNIDADES RECEBEDORAS`. Só foram lidos os nomes das abas e os valores distintos da coluna `ANO`: só 2025, com as mesmas 280 e 1116 linhas de DATA1. Não há outro ano nem projetos novos.
- Buscas na web (`pesquisa/literatura/busca.md`, W1 e W5) não encontraram planilha pública de 2024 ou 2026. A ausência vale para esta busca.

Exposições ligadas a um possível DATA2: números de notícias de 2026 (PI, RS) e de 2025 (PR), registrados em `busca.md`. Nenhum é o desfecho de H1.

Consequência: H1 não pode ser executada. O estado é `BLOCKED` até que DATA2 seja identificado (D-11). A entrada exige: (1) obter a planilha de outro ano junto à CONAB/GEIAF, pelo Fala.BR ou com a orientação acadêmica; (2) registrar procedência e hash **antes** de qualquer leitura; (3) rodar `pesquisa/scripts/h1_confirmatorio.py` sem mudanças, seguindo o contrato de execução.
