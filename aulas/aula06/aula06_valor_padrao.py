# Aula 06 - valor padrão de parâmetro
#
# desconto=0.0 na definição significa "se ninguém passar desconto, use zero".
# A chamada com dois argumentos funciona, a chamada com três funciona, e o
# caso comum fica curto sem perder a opção.
#
# Guardem este rótulo: parâmetro com valor padrão aparece em toda biblioteca
# que vocês vão usar, começando na Aula 10, quando o Requests entrar.

def calcular_total(valor, quantidade, desconto=0.0):
    return valor * quantidade - desconto


sem_desconto = calcular_total(100.00, 3)
com_desconto = calcular_total(100.00, 3, 50.00)

print(f"Sem desconto: R$ {sem_desconto:.2f}")
print(f"Com desconto: R$ {com_desconto:.2f}")
print(f"A diferença é o 3o argumento: R$ {sem_desconto - com_desconto:.2f}")

assert calcular_total(100.00, 3) == 300.00
assert calcular_total(100.00, 3, 50.00) == 250.00
print("As duas verificações passaram")
