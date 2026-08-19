# Aula 04 - acumulador de lista, e a unicidade em uma linha
#
# O acumulador é a versão de coleção do contador: em vez de contar, ele
# guarda. A lista vazia do começo, falhas = [], é o ponto de partida, o
# mesmo papel que o zero tem no contador, e .append(codigo) acrescenta um
# item no fim.
#
# Regra do curso, e ela evita bug difícil de achar: dentro do for você lê
# uma lista e escreve em outra. Remover item da lista que está sendo
# percorrida desloca as posições debaixo dos seus pés, e o laço pula itens
# sem avisar.

codigos = [200, 201, 404, 500, 302, 403]
falhas = []

for codigo in codigos:
    if codigo >= 400:
        falhas.append(codigo)

print(f"Códigos de falha encontrados: {falhas}")

assert len(falhas) == 3, f"esperado 3 falhas, obtido {len(falhas)}"
print("Verificação passou: 3 códigos de falha na execução")

print()

# --- unicidade: uma regra de negócio presente em quase todo sistema ---
# set joga fora as repetições. Se o tamanho da lista e o tamanho do
# conjunto batem, não existe valor repetido. Identificador que repete é
# defeito, e esta é a linha de teste que responde por ele.
ids = [101, 102, 103, 104, 105]

print(f"Itens na lista: {len(ids)}")
print(f"Valores distintos: {len(set(ids))}")

assert len(ids) == len(set(ids))
print("Verificação passou: todo id da listagem é único")

print()

# --- a mesma verificação, com um id duplicado na massa ---
ids_com_duplicado = [101, 102, 103, 102, 105]

print(f"Itens na lista: {len(ids_com_duplicado)}")
print(f"Valores distintos: {len(set(ids_com_duplicado))}")

try:
    assert len(ids_com_duplicado) == len(set(ids_com_duplicado)), (
        f"esperado {len(ids_com_duplicado)} distintos, "
        f"obtido {len(set(ids_com_duplicado))}")
    print("esta linha não chega a ser impressa")
except AssertionError as erro:
    print(f"AssertionError: {erro}")
