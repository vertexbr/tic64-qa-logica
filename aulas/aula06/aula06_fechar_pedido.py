# Aula 06 - o arquivo da demonstração guiada 2
#
# Quatro funções pequenas, cada uma com uma responsabilidade só, e a quarta
# chamando as três anteriores. É o único lugar da aula em que uma função chama
# outra três vezes, e é isso que vocês precisam ter visto antes da Aula 08.
#
# Repare que fechar_pedido não recalcula nada: ela só chama as outras três na
# ordem e junta o resultado. Se a regra de frete mudar, você mexe em
# calcular_frete e fechar_pedido obedece sem ser tocada. Essa é a resposta
# técnica para a pergunta dos cem testes de login da abertura.
#
# E repare no escopo: subtotal, com_desconto e frete aparecem duas vezes neste
# arquivo, uma dentro de fechar_pedido e uma na margem. São variáveis
# diferentes, em quadrados diferentes.

def calcular_subtotal(preco, quantidade):
    return preco * quantidade


def aplicar_desconto(subtotal, percentual):
    return subtotal - (subtotal * percentual / 100)


def calcular_frete(total, cliente_vip):
    if cliente_vip or total >= 250:
        return 0.0
    return 20.0


def fechar_pedido(preco, quantidade, percentual, cliente_vip):
    subtotal = calcular_subtotal(preco, quantidade)
    com_desconto = aplicar_desconto(subtotal, percentual)
    frete = calcular_frete(com_desconto, cliente_vip)
    return com_desconto + frete


subtotal = calcular_subtotal(100.00, 3)
com_desconto = aplicar_desconto(subtotal, 10)
frete = calcular_frete(com_desconto, False)

print(f"Subtotal:     R$ {subtotal:.2f}")
print(f"Com desconto: R$ {com_desconto:.2f}")
print(f"Frete:        R$ {frete:.2f}")
print(f"Total final:  R$ {com_desconto + frete:.2f}")

# O quarto assert é o que vale mais que os outros: cliente VIP com total baixo
# é o único cenário que testa a SEGUNDA metade do or de calcular_frete. Sem
# ele, um or escrito como and passaria os outros quatro sem reclamar.
assert calcular_subtotal(100.00, 3) == 300.00
assert aplicar_desconto(300.00, 10) == 270.00
assert calcular_frete(100.00, False) == 20.0
assert calcular_frete(100.00, True) == 0.0
assert fechar_pedido(100.00, 3, 10, False) == 270.00
print("Todas as verificações passaram")
