# REVIEW-4

- Revisor: `reviewer-2` (contexto separado, sem edição), invocado em 2026-10-21
- Escopo: diff `9f123f4..8a246a2` (correções da D-18 aos achados da REVIEW-3)
- Commit revisado: `8a246a2`
- Veredito: **PASS**
- Separação: só procedimental.

Status dos achados da REVIEW-3: 1, 2, 3, 5, 6 e 7 corrigidos; 4 parcial. Nenhuma mudança silenciosa de compromisso: a mudança do código está declarada e só torna K1 mais restritiva. `DATA2.sha256` não existe. O teste reproduz `resultado.txt` byte a byte (23 casos), e o modo de ensaio reproduz R6 byte a byte.

Achados (nenhum material):
- N1 (menor): protocolo.md E1 ainda usa "utilizáveis" no sentido antigo, que inclui o PR. Não muda o estimando.
- N2 (menor): registro.md item 3 omite as notícias de 2025 e a do RS.
- N3 (menor): o caso "sensibilidades T2 a T5 e K5 calculadas" só confere se as chaves existem. Com as asserções fortalecidas no scratchpad, os valores saem preenchidos (3 discordantes, K5 = 0,0).
- N4 (trivial): "forte aumento do nº de organizações" não vale para AL (de 6 para 7); o que teria de mudar são as unidades (de 18 para 10).
- N5 (informativo): o ponta a ponta só cobre esparsa → pool; pool → esparsa e REFUTED só estão testados com tabelas construídas.
