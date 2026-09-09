# Aula 11 - os três casos que o padrão descreveria com números diferentes
#
# O padrão HTTP tem um número para cada um destes três casos: 409 para conflito com um estado
# que já existe, 422 para conteúdo que desobedece a regra, e 404 para recurso que não está lá.
# Esta API responde 400 nos três, e isso não é bug dela: é a convenção dela.
#
# A consequência prática é a lição do arquivo. Antes de escrever a asserção, descubra qual
# convenção a API usa, e o jeito de descobrir é disparar a requisição e ler o que voltou.
# Nunca escreva assert status == 422 porque o padrão diz que deveria ser 422. E repare que os
# três corpos são diferentes: dois trazem a chave message e um traz a chave email, então o
# status sozinho não distingue os casos nem quando o número é o mesmo.
#
# REGRA DE NEGÓCIO (o que o slide projeta e o professor lê no início):
#   Cadastro com e-mail repetido, cadastro sem campo obrigatório e consulta a usuário
#   inexistente são recusados com 400 nesta API. Os corpos são diferentes: e-mail repetido e
#   usuário inexistente trazem a chave message, e campo ausente traz a chave do campo.

import requests

BASE_URL = "https://serverest.dev"

payload = {
    "nome": "Gaia Silva",
    "email": "gaia.quatrocentos.tic64@qa.com.br",
    "password": "JL1234!",
    "administrador": "true",
}

primeiro = requests.post(f"{BASE_URL}/usuarios", json=payload, timeout=10)
duplicado = requests.post(f"{BASE_URL}/usuarios", json=payload, timeout=10)
print(f"e-mail repetido     -> {duplicado.status_code} {duplicado.json()}")

sem_email = {"nome": "Sem Email", "password": "JL1234!", "administrador": "true"}
faltando = requests.post(f"{BASE_URL}/usuarios", json=sem_email, timeout=10)
print(f"sem o campo email   -> {faltando.status_code} {faltando.json()}")

busca = requests.get(f"{BASE_URL}/usuarios/aaaaaaaaaaaaaaaa", timeout=10)
print(f"usuário inexistente -> {busca.status_code} {busca.json()}")

id_criado = primeiro.json().get("_id")
if id_criado:
    requests.delete(f"{BASE_URL}/usuarios/{id_criado}", timeout=10)

# --- EXPLICACAO LINHA A LINHA · gerado, nao edite aqui ---
#
# Gerado a partir de explicacao-linha-a-linha/slide-09.md.
# Nao edite este bloco: a proxima geracao substitui ele inteiro.
#
# A numeracao abaixo e a DESTE arquivo: a mesma da calha do PyCharm e a mesma
# que aparece no slide 9 da apresentacao.
#
#      29  primeiro = requests.post(...)
#          Cria o usuário. Este cadastro existe só para o próximo ser
#          recusado.
#
#      30  duplicado = requests.post(...)
#          O mesmo payload de novo. O padrão chamaria isto de 409, conflito.
#
#      31  print(f"e-mail repetido     -> ...")
#          400, e o corpo traz a chave message.
#
#      33  sem_email = {...}
#          Um dicionário com três chaves, sem a de e-mail.
#
#      34  faltando = requests.post(...)
#          Campo obrigatório ausente. O padrão chamaria isto de 422, conteúdo
#          inválido.
#
#      35  print(f"sem o campo email   -> ...")
#          400, e o corpo traz a chave email, não message.
#
#      37  busca = requests.get(f"{BASE_URL}/usuarios/aaaaaaaaaaaaaaaa",
#          timeout=10)
#          Recurso que não está lá. O padrão chamaria isto de 404.
#
#      38  print(f"usuário inexistente -> ...")
#          400, e o corpo volta a trazer message.
#
# --- fim da explicacao linha a linha ---
