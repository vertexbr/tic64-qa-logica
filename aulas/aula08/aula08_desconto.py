# Aula 08 - a regra de desconto da loja, como o sistema implementou
#
# A regra é a de aulas/aula03/aula03_desconto.py, a mesma escada que a turma
# escreveu na Aula 03 e que vale o curso inteiro. O acréscimo desta aula é que
# ela virou função com return, testável de fora, e que o percentual do VIP
# acima de 200 está em 20 e não em 25.
#
# Os 20 não são erro plantado: 20 é o que a regra do curso sempre disse. Quem
# vai errar é o TESTE do slide, que espera 25, e é isso que a demonstração usa
# para comparar dois jeitos de escrever a mesma verificação.
#
# REGRA DE NEGÓCIO (o que o slide projeta e o professor lê no início):
#   Cliente VIP acima de 200 tem 20% de desconto e VIP até 200 tem 10%. Cupom
#   válido dá 5%, e quem não é VIP nem tem cupom não ganha desconto nenhum.


def calcular_desconto(valor_compra, cliente_vip=False, tem_cupom=False):
    if cliente_vip and valor_compra > 200:
        return 20
    if cliente_vip:
        return 10
    if tem_cupom:
        return 5
    return 0
