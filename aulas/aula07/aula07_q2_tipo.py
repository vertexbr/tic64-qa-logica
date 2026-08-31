# Aula 07 - quebrado 2 de 4: tipos incompatíveis na mesma operação
#
# Rode, leia a ÚLTIMA linha primeiro, e responda o tipo, a linha e a causa.
#
# Este é o mais interessante dos quatro, e vale voltar nele: a mensagem fala de
# "sequence" e de "non-int" e nunca diz a palavra "texto". Mesmo assim, a linha
# apontada tem uma multiplicação e duas variáveis, e olhar o tipo de cada uma
# resolve. Mensagem confusa não é motivo para desistir da mensagem.
#
# Estrutura de demonstração igual à do aula07_q1_indice.py: o erro dentro de
# try/except com print_exc() só para o arquivo seguir até o fim.
#
# REGRA DE NEGÓCIO (o que o slide projeta e o professor lê no início):
#   O total do pedido é o preço do produto vezes a quantidade, mais dez reais de frete.
#   A quantidade chega do formulário como texto.
import traceback

quantidade = "3"
preco = 199.90

try:
    print(f"Total: {preco * quantidade + 10}")
except TypeError:
    traceback.print_exc()

print()
print(f"O tipo de quantidade é {type(quantidade)}, e não número.")
print(f"Com int(quantidade), sai: {preco * int(quantidade) + 10}")
