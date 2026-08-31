# Aula 07 - try/except de tipo específico, com massa de teste
#
# O cenário real: sua verificação lê um arquivo de massa e um dos valores veio
# como texto. Você não quer que a execução inteira morra por causa de uma linha.
# Você quer tratar aquela linha e seguir.
#
# try marca o bloco arriscado. except ValueError diz o que fazer se for
# exatamente esse erro. E o "as erro" guarda o erro numa caixinha, do mesmo
# jeito que qualquer variável da Aula 02: a mensagem original do Python vira
# parte do seu relatório em vez de derrubar a execução.
#
# A massa é fixa e desenhada à mão, não sorteada: duas entradas boas e duas
# ruins, e a última é a string vazia, que é o caso que ninguém lembra de testar.
#
# REGRA DE NEGÓCIO (o que o slide projeta e o professor lê no início):
#   A idade vem do arquivo de massa como texto e precisa virar número. Linha fora do
#   formato é recusada e registrada, e não derruba a execução das outras.

print("=== uma entrada só, para ver a forma ===")

entrada = "cinquenta"
try:
    idade = int(entrada)
    print(f"Idade: {idade}")
except ValueError:
    print(f"Valor inválido para idade: '{entrada}'")


print()
print("=== a massa inteira, que é o uso de verdade ===")

entradas = ["18", "cinquenta", "42", ""]

for bruta in entradas:
    try:
        idade = int(bruta)
        print(f"'{bruta}' virou {idade}")
    except ValueError as erro:
        print(f"'{bruta}' recusada. O Python disse: {erro}")

print()
print("Quatro linhas de massa, duas boas, duas ruins, nenhuma parada.")

# Vários except embaixo do mesmo try são uma escada, e a escada da Aula 03
# vale aqui igual: DESCE, TESTA o tipo, ACHOU? PARA no primeiro que casa.
# Se o erro for de valor, o except de chave abaixo nem é olhado.
print()
print("=== a escada de except ===")

dados = {"passou": 12}
for chave in ("passou", "ignorado"):
    try:
        print(f"{chave}: {int(dados[chave])}")
    except ValueError as erro:
        print(f"não deu para converter: {erro}")
    except KeyError as erro:
        print(f"a chave não existe: {erro}")
