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

# A regra do frete grátis é a mesma de aulas/aula02/aula02.py, onde ela era um
# valor_minimo_frete_gratis solto, e da atividade da Aula 04. Aqui ela está
# escrita três vezes de propósito, para doer.
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

# --- EXPLICACAO LINHA A LINHA · gerado, nao edite aqui ---
#
# Gerado a partir de explicacao-linha-a-linha/slide-03.md.
# Nao edite este bloco: a proxima geracao substitui ele inteiro.
#
# A numeracao abaixo e a DESTE arquivo: a mesma da calha do PyCharm e a mesma
# que aparece no slide 3 da apresentacao.
#
#      15  subtotal_ana = 199.90 * 3
#          A multiplicação é resolvida antes da atribuição, então subtotal_ana
#          nasce valendo 599.70.
#
#      16  if subtotal_ana >= 250:
#          599.70 >= 250 responde True. O caminho de cima é o que executa.
#
#      17  frete_ana = 0.0
#          frete_ana passa a existir valendo 0.0. A variável nasce aqui,
#          dentro do if.
#
# 18 e 19  else: e frete_ana = 20.0
#          Não executam nesta passagem. O else só é olhado quando a condição
#          responde False.
#
#      21  subtotal_beto = 49.90 * 1
#          49.90. O * 1 está escrito para o bloco ficar visualmente igual ao
#          dos outros dois.
#
#      22  if subtotal_beto >= 250:
#          49.90 >= 250 responde False. Desta vez quem executa é o else.
#
#      23  frete_beto = 0.0
#          Não executa.
#
# 24 e 25  else: e frete_beto = 20.0
#          frete_beto nasce valendo 20.0.
#
# 27 a 31  o bloco da Cris
#          179.80 não alcança 250, então frete_cris fica 20.0. Estas cinco
#          linhas não estão no slide, e é a terceira cópia da regra.
#
# 33 a 35  os três print de evidência
#          Cada um lê duas variáveis diferentes. São seis nomes de variável
#          para três clientes.
#
#      36  print("A regra está escrita 3 vezes neste arquivo")
#          Fecha a execução com a contagem dita em voz alta pelo próprio
#          programa.
#
# --- fim da explicacao linha a linha ---
