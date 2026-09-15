# Aula 11 - o ciclo completo, e ele tem seis passos e não quatro
#
# Criar, consultar, alterar, consultar de novo para provar a alteração, excluir, e consultar de
# novo para provar a ausência. Os dois passos que quase todo mundo esquece são o quarto e o
# sexto, e eles são o coração da aula: mensagem de sucesso é o servidor dizendo que fez, e o
# GET seguinte é você conferindo que ele fez.
#
# O último GET é a validação do DELETE. Excluir e receber 200 não prova que sumiu, como o
# aula11_status_nao_basta.py mostra. O que prova é procurar depois e não achar.
#
# REGRA DE NEGÓCIO (o que o slide projeta e o professor lê no início):
#   Criar responde 201 com o identificador, consultar responde 200 com o corpo inteiro, e
#   alterar e excluir respondem 200. Depois de alterar, a consulta seguinte traz o valor
#   novo; depois de excluir, ela responde 400 dizendo que o usuário não foi encontrado.
#   O PUT substitui o recurso inteiro, então o corpo enviado leva todos os campos.

from uuid import uuid4

import requests

BASE_URL = "https://serverest.dev"

payload = {
    "nome": "Gaia Silva",
    "email": f"gaia.ciclo.{uuid4().hex}@qa.com.br",
    "password": "JL1234!",
    "administrador": "true",
}

criar = requests.post(f"{BASE_URL}/usuarios", json=payload, timeout=10)
print(f"POST      -> {criar.status_code} {criar.json()['message']}")
id_criado = criar.json()["_id"]

consultar = requests.get(f"{BASE_URL}/usuarios/{id_criado}", timeout=10)
print(f"GET       -> {consultar.status_code} nome={consultar.json()['nome']}")

payload["nome"] = "Gaia Silva Atualizada"
alterar = requests.put(f"{BASE_URL}/usuarios/{id_criado}", json=payload, timeout=10)
print(f"PUT       -> {alterar.status_code} {alterar.json()['message']}")

conferir = requests.get(f"{BASE_URL}/usuarios/{id_criado}", timeout=10)
print(f"GET       -> {conferir.status_code} nome={conferir.json()['nome']}")

excluir = requests.delete(f"{BASE_URL}/usuarios/{id_criado}", timeout=10)
print(f"DELETE    -> {excluir.status_code} {excluir.json()['message']}")

sumiu = requests.get(f"{BASE_URL}/usuarios/{id_criado}", timeout=10)
print(f"GET final -> {sumiu.status_code} {sumiu.json()['message']}")

# --- EXPLICACAO LINHA A LINHA · gerado, nao edite aqui ---
#
# Gerado a partir de explicacao-linha-a-linha/slide-16.md.
# Nao edite este bloco: a proxima geracao substitui ele inteiro.
#
# A numeracao abaixo e a DESTE arquivo: a mesma da calha do PyCharm e a mesma
# que aparece no slide 16 da apresentacao.
#
#      30  criar = requests.post(...)
#          C de criar. O servidor passa a guardar um usuário que não existia.
#
#      31  print(f"POST      -> ...")
#          201 e a mensagem de sucesso.
#
#      32  id_criado = criar.json()["_id"]
#          O identificador que as cinco chamadas seguintes usam. Sem esta
#          linha o ciclo não existe.
#
#      34  consultar = requests.get(f"{BASE_URL}/usuarios/{id_criado}",
#          timeout=10)
#          R de consultar. Agora com o identificador no endereço, e não a
#          lista inteira.
#
#      35  print(f"GET       -> ... nome={consultar.json()['nome']}")
#          200 e o nome original.
#
#      37  payload["nome"] = "Gaia Silva Atualizada"
#          Muda o dicionário na memória. O servidor ainda não sabe de nada.
#
#      38  alterar = requests.put(f"{BASE_URL}/usuarios/{id_criado}",
#          json=payload, timeout=10)
#          U de alterar. O PUT manda o recurso inteiro, e não só o campo que
#          mudou.
#
#      39  print(f"PUT       -> ...")
#          200 e "Registro alterado com sucesso".
#
#      41  conferir = requests.get(...)
#          O quarto passo, e o primeiro que quase todo mundo esquece.
#          Consultar de novo para provar que a alteração pegou.
#
#      42  print(f"GET       -> ... nome={conferir.json()['nome']}")
#          200 e o nome novo. Esta linha é a prova; a mensagem da linha 39 era
#          só a promessa.
#
#      44  excluir = requests.delete(...)
#          D de excluir.
#
#      45  print(f"DELETE    -> ...")
#          200 e "Registro excluído com sucesso".
#
#      47  sumiu = requests.get(...)
#          O sexto passo, e o segundo que quase todo mundo esquece. Procurar
#          depois de apagar.
#
#      48  print(f"GET final -> ...")
#          400, e a mensagem diz "Usuário não encontrado". Esta linha é a
#          prova de que sumiu.
#
# --- fim da explicacao linha a linha ---
