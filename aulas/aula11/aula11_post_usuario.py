# Aula 11 - o POST com corpo, e as três coisas novas na mesma linha
#
# Muda o verbo, de get para post. Aparece o json=payload, que é o corpo do pedido. E o payload
# é um dicionário Python comum, o mesmo da Aula 5: o Requests converte para JSON e avisa no
# cabeçalho que o conteúdo é JSON. Escrever data=payload manda como formulário, e nesta API o
# cadastro simples até funciona assim, o que é pior: o primeiro corpo com estrutura aninhada
# quebra e ninguém entende por quê.
#
# A última linha apaga o usuário criado. Sem ela, a segunda execução deste arquivo recebe 400
# e morre com KeyError na linha do _id, que é o erro mais comum desta aula.
#
# REGRA DE NEGÓCIO (o que o slide projeta e o professor lê no início):
#   Criar usuário exige nome, email, password e administrador, e o administrador vai como
#   texto entre aspas, true ou false. A resposta de sucesso é 201, com a mensagem de
#   cadastro realizado e o identificador do recurso que passou a existir.

import requests

BASE_URL = "https://serverest.dev"

payload = {
    "nome": "Gaia Silva",
    "email": "gaia.aula11.001@qa.com.br",
    "password": "JL1234!",
    "administrador": "true",
}

resposta = requests.post(f"{BASE_URL}/usuarios", json=payload, timeout=10)

print(f"Status: {resposta.status_code}")
print(f"Mensagem: {resposta.json()['message']}")
print(f"ID criado: {resposta.json()['_id']}")

# O identificador é o endereço do que acabou de nascer, e os três verbos seguintes precisam
# dele. Guardar numa variável é o que permite consultar, alterar e apagar depois.
id_criado = resposta.json()["_id"]
requests.delete(f"{BASE_URL}/usuarios/{id_criado}", timeout=10)

# --- EXPLICACAO LINHA A LINHA · gerado, nao edite aqui ---
#
# Gerado a partir de explicacao-linha-a-linha/slide-05.md.
# Nao edite este bloco: a proxima geracao substitui ele inteiro.
#
# A numeracao abaixo e a DESTE arquivo: a mesma da calha do PyCharm e a mesma
# que aparece no slide 5 da apresentacao.
#
#      17  import requests
#          Nada de novo.
#
#      19  BASE_URL = "https://serverest.dev"
#          Nada de novo.
#
# 21 a 26  o dicionário payload
#          Quatro chaves, e as quatro são exigidas por esta API. O
#          administrador é o texto "true", e não o booleano True do Python:
#          mandar o booleano faz a API recusar.
#
#      28  resposta = requests.post(f"{BASE_URL}/usuarios", json=payload,
#          timeout=10)
#          O json= faz duas coisas: converte o dicionário para JSON e avisa no
#          cabeçalho que o conteúdo é JSON. O timeout=10 é o mesmo da Aula 10.
#
#      30  print(f"Status: {resposta.status_code}")
#          201, e não 200.
#
#      31  print(f"Mensagem: {resposta.json()['message']}")
#          A chave message do corpo. Aspas simples dentro da f-string, porque
#          as duplas já fecham a string.
#
#      32  print(f"ID criado: {resposta.json()['_id']}")
#          A chave _id. Este é o endereço do recurso que passou a existir.
#
#      36  id_criado = resposta.json()["_id"]
#          Guardar numa variável é o que permite consultar, alterar e apagar
#          depois.
#
#      37  requests.delete(...)
#          A limpeza, para o arquivo poder rodar de novo.
#
# --- fim da explicacao linha a linha ---
