# Aula 11 - o problema do dia: a mesma requisição, duas respostas
#
# Este arquivo manda o MESMO cadastro duas vezes seguidas, com o mesmo e-mail. A primeira vez
# cria; a segunda é recusada. Não mudou uma letra do código entre as duas: mudou o estado do
# servidor, porque a primeira chamada deixou um dado lá. A segunda chamada é exatamente o que
# a segunda execução do seu teste vai encontrar amanhã.
#
# A última linha apaga o usuário criado, e é por isso que este arquivo pode ser rodado quantas
# vezes você quiser sempre com o mesmo resultado. O .get() é o da Aula 5: se a criação falhar,
# ele devolve None em vez de derrubar o programa, e aí não há nada para apagar.
#
# REGRA DE NEGÓCIO (o que o slide projeta e o professor lê no início):
#   O cadastro não aceita dois usuários com o mesmo e-mail. Criar com e-mail novo responde 201
#   com a mensagem de sucesso e o identificador do que nasceu. Repetir o mesmo e-mail responde
#   400 com a mensagem de que aquele e-mail já está sendo usado.

import requests

BASE_URL = "https://serverest.dev"

payload = {
    "nome": "Gaia Silva",
    "email": "gaia.silva.tic64@qa.com.br",
    "password": "JL1234!",
    "administrador": "true",
}

primeira = requests.post(f"{BASE_URL}/usuarios", json=payload, timeout=10)
print(f"Primeira chamada -> {primeira.status_code} {primeira.json()}")

segunda = requests.post(f"{BASE_URL}/usuarios", json=payload, timeout=10)
print(f"Segunda chamada  -> {segunda.status_code} {segunda.json()}")

id_criado = primeira.json().get("_id")
if id_criado:
    requests.delete(f"{BASE_URL}/usuarios/{id_criado}", timeout=10)

# --- EXPLICACAO LINHA A LINHA · gerado, nao edite aqui ---
#
# Gerado a partir de explicacao-linha-a-linha/slide-02.md.
# Nao edite este bloco: a proxima geracao substitui ele inteiro.
#
# A numeracao abaixo e a DESTE arquivo: a mesma da calha do PyCharm e a mesma
# que aparece no slide 2 da apresentacao.
#
#      17  import requests
#          A biblioteca da Aula 10, sem novidade nenhuma.
#
#      19  BASE_URL = "https://serverest.dev"
#          O mapa de ambientes da Aula 5. Uma linha, e o arquivo inteiro troca
#          de servidor.
#
# 21 a 26  o dicionário payload
#          O corpo do pedido, e ele é um dicionário Python comum. O
#          administrador vai como texto, "true" com aspas, porque é assim que
#          esta API pede.
#
#      28  primeira = requests.post(...)
#          Primeira ida à rede. O servidor não conhece este e-mail, cria o
#          usuário e devolve 201 com o identificador.
#
#      29  print(f"Primeira chamada -> ...")
#          Imprime o status e o corpo inteiro. O _id que aparece é diferente a
#          cada execução.
#
#      31  segunda = requests.post(...)
#          Exatamente a mesma linha. O mesmo endereço, o mesmo dicionário, o
#          mesmo verbo.
#
#      32  print(f"Segunda chamada  -> ...")
#          Agora 400, e a mensagem diz o motivo: aquele e-mail já está sendo
#          usado.
#
#      34  id_criado = primeira.json().get("_id")
#          O .get() da Aula 5. Se a primeira chamada tivesse falhado, o corpo
#          não teria _id, e o .get() devolve None em vez de derrubar o
#          programa com KeyError.
#
# 35 e 36  if id_criado: requests.delete(...)
#          A limpeza. É ela que faz este arquivo poder ser rodado quantas
#          vezes você quiser, sempre com o mesmo resultado.
#
# --- fim da explicacao linha a linha ---
