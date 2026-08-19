# Aula 04 - o contador também anda para trás
#
# A catraca sobe, o foguete desce. Mecanismo idêntico, sinal trocado:
# contagem = contagem - 1 em vez de aprovados = aprovados + 1.
#
# Os dois juntos ensinam a lição mais importante do dia: a variável de
# controle precisa mudar dentro do laço. Se ela não muda, ou o número
# final está errado, ou o laço nunca acaba.

contagem = 5

for volta in range(5):
    print(f"{contagem}...")
    contagem = contagem - 1

print("Lançamento!")

assert contagem == 0, f"esperado 0, obtido {contagem}"
print("Verificação passou: a contagem chegou a zero")
