# Aula 04 - o contador também anda para trás
#
# A catraca sobe, o foguete desce. Mecanismo idêntico, sinal trocado:
# contagem = contagem - 1 em vez de aprovados = aprovados + 1.
#
# Os dois juntos ensinam a lição do dia: a variável que carrega o resultado
# precisa mudar dentro do laço, senão o número final sai errado.
#
# E repare no que este laço NAO faz: ele acaba de qualquer jeito. Quem conta
# as cinco voltas é o range, não a contagem. Apagando o decremento, ele roda
# as cinco voltas do mesmo jeito e só entrega o número errado.
#
# O laço que não termina é outro caso, e ele mora no aula04_laco_infinito.py:
# lá a variável está dentro da condição do while, e não mexer nela deixa a
# condição verdadeira para sempre.

contagem = 5

for volta in range(5):
    print(f"{contagem}...")
    contagem = contagem - 1

print("Lançamento!")

assert contagem == 0, f"esperado 0, obtido {contagem}"
print("Verificação passou: a contagem chegou a zero")
