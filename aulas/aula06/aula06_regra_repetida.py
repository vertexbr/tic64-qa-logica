# Aula 06 - a mesma regra escrita três vezes
#
# Este arquivo existe para doer, não para ser copiado. A regra de frete grátis
# está escrita três vezes, uma por cliente, e as três são idênticas.
#
# Rode e olhe as três linhas de saída: resultados diferentes, porque a massa é
# diferente, saindo de uma regra que está escrita palavra por palavra igual em
# três lugares. Agora imagine a notícia que chega numa terça: frete grátis
# passa a valer a partir de 199. Quantos lugares você edita? E se esquecer um,
# o sistema fica com duas regras ao mesmo tempo e ninguém percebe.

subtotal_ana = 199.90 * 3
if subtotal_ana >= 250:
    frete_ana = 0.0
else:
    frete_ana = 20.0

subtotal_beto = 49.90 * 1
if subtotal_beto >= 250:
    frete_beto = 0.0
else:
    frete_beto = 20.0

subtotal_cris = 89.90 * 2
if subtotal_cris >= 250:
    frete_cris = 0.0
else:
    frete_cris = 20.0

print(f"Ana:  R$ {subtotal_ana:.2f} | frete R$ {frete_ana:.2f}")
print(f"Beto: R$ {subtotal_beto:.2f} | frete R$ {frete_beto:.2f}")
print(f"Cris: R$ {subtotal_cris:.2f} | frete R$ {frete_cris:.2f}")
print("A regra está escrita 3 vezes neste arquivo")
