# Aula 05 - pertinência: in e not in numa lista de códigos
#
# Compare a linha do assert com o que você escreveria sem a lista:
#
#   codigo == 200 or codigo == 201 or codigo == 204
#
# A versão com lista tem menos lugar para errar, e se lê como frase: "o código
# está entre os de sucesso". O not in é a mesma coisa ao contrário, para o
# cenário negativo.
#
# Guardem os dois. Na Aula 08 eles voltam como asserção de pytest sem mudar
# uma vírgula.

codigos_de_sucesso = [200, 201, 204]
codigos_de_erro_servidor = [500, 502, 503]

codigo = 201

print(f"Status recebido: {codigo}")
print(f"Está entre os de sucesso? {codigo in codigos_de_sucesso}")
print(f"Está entre os erros de servidor? {codigo in codigos_de_erro_servidor}")

assert codigo in codigos_de_sucesso
assert codigo not in codigos_de_erro_servidor
print("Verificações passaram")
