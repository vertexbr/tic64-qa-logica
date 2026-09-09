# Aula 11 - o PUT que cria, e por que ele não é defeito
#
# Alterar um recurso que não existe faz o recurso passar a existir. Isso é comportamento
# previsto no padrão HTTP e várias APIs fazem. Quem escreve um teste negativo esperando recusa
# aqui vê o teste falhar, e não há defeito nenhum: o teste é que estava supondo a coisa errada.
#
# E repare no que acontece ao rodar: o arquivo cria um usuário sem querer. Por isso ele apaga
# na linha seguinte. A regra da limpeza vale para o professor também.
#
# REGRA DE NEGÓCIO (o que o slide projeta e o professor lê no início):
#   Alterar um identificador que não existe responde 201, com a mensagem de cadastro realizado
#   e um identificador novo: o PUT criou o recurso. Recusa não é o comportamento previsto, e um
#   teste negativo escrito contra este endpoint precisa esperar a criação.

import time

import requests

BASE_URL = "https://serverest.dev"

fantasma = {
    "nome": "Fantasma",
    "email": f"fantasma.{int(time.time())}@qa.com.br",
    "password": "JL1234!",
    "administrador": "false",
}

resposta = requests.put(f"{BASE_URL}/usuarios/bbbbbbbbbbbbbbbb", json=fantasma, timeout=10)

print(f"Status: {resposta.status_code}")
print(f"Corpo: {resposta.json()}")

requests.delete(f"{BASE_URL}/usuarios/{resposta.json()['_id']}", timeout=10)
print("Limpeza feita: o usuário criado sem querer foi apagado.")

# --- EXPLICACAO LINHA A LINHA · gerado, nao edite aqui ---
#
# Gerado a partir de explicacao-linha-a-linha/slide-18.md.
# Nao edite este bloco: a proxima geracao substitui ele inteiro.
#
# A numeracao abaixo e a DESTE arquivo: a mesma da calha do PyCharm e a mesma
# que aparece no slide 18 da apresentacao.
#
# 21 a 26  o dicionário fantasma
#          Um payload completo, com e-mail único pela marca de tempo. Ele
#          precisa ser único: se o e-mail já existisse, a recusa viria por
#          outro motivo e a demonstração mostraria outra coisa.
#
#      28  resposta = requests.put(f"{BASE_URL}/usuarios/bbbbbbbbbbbbbbbb",
#          json=fantasma, timeout=10)
#          Dezesseis letras b: formato válido, identificador que não existe.
#
#      30  print(f"Status: {resposta.status_code}")
#          201. Não é 200, não é 404, não é recusa: é criação.
#
#      31  print(f"Corpo: {resposta.json()}")
#          A mensagem é "Cadastro realizado com sucesso" e vem um _id novo,
#          diferente das letras b que foram pedidas.
#
#      33  requests.delete(f"{BASE_URL}/usuarios/{resposta.json()['_id']}",
#          timeout=10)
#          A limpeza, e o _id usado aqui é o que o servidor devolveu, não o
#          que foi pedido.
#
#      34  print("Limpeza feita: ...")
#          Confirma na tela que o usuário criado sem querer foi apagado.
#
# --- fim da explicacao linha a linha ---
