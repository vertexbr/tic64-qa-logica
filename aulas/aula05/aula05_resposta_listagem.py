# Aula 05 - a resposta de listagem, e o assert que acha defeito de verdade
#
# Esta é a massa que veio do navegador: uma resposta de listagem de produtos,
# copiada da aba de rede e transcrita para dicionário Python.
#
# Repare na forma: quantidade em cima, produtos embaixo, e produtos é uma
# lista de dicionários, a mesma estrutura do arquivo aula05_suite_casos.py.
#
# O assert do fim é um teste de verdade, do tipo que acha defeito real. A API
# afirma uma quantidade num campo e entrega uma lista noutro, e nada garante
# que os dois batem. Vocês aprenderam len na Aula 04 para contar itens; aqui
# ele acabou de virar uma validação de contrato de API.

resposta = {
    "quantidade": 3,
    "produtos": [
        {"nome": "Api de teste", "preco": 1000, "quantidade": 1, "_id": "4Y9sHbAT4YGPVdnD"},
        {"nome": "TV SONY", "preco": 5000, "quantidade": 10, "_id": "K6leHdftCeOJj8BJ"},
        {"nome": "Mouse Gamer", "preco": 100, "quantidade": 50, "_id": "9OVBpvPYbjaXqBTG"},
    ]
}

print(f"A API disse que trouxe {resposta['quantidade']} produtos")
print(f"A lista tem de verdade {len(resposta['produtos'])} produtos")

assert resposta["quantidade"] == len(resposta["produtos"])
print("Verificação passou: o campo quantidade bate com o tamanho da lista")

# Dois degraus a mais, e os dois são vocabulário que a Aula 08 recicla dentro
# de uma escada de asserções: a lista não veio vazia, e o campo obrigatório
# está presente no primeiro registro.
primeiro = resposta["produtos"][0]

print(f"Primeiro produto: {primeiro['nome']}")

assert len(resposta["produtos"]) > 0
assert "_id" in primeiro
print("Verificações passaram: a lista não veio vazia e o registro tem _id")
