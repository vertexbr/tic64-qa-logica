# Aula 11 - segunda demonstração: o veredito acumulado
#
# Rodar:                   pytest test_veredito.py -v
# Da raiz do repositório:  pytest aulas/aula11/test_veredito.py -v
#
# Repare no que esta função é. Ela recebe um dado, aplica um monte de regras, junta os
# problemas numa lista e devolve um veredito. É exatamente o exercício da Aula 5, o da lista de
# usuários com nome vazio e sem perfil. A lógica não mudou; só a origem do dado mudou.
#
# O return dentro do primeiro if é o freio de mão da Aula 4 aplicado a função: status errado,
# para tudo. Assim o degrau um é respeitado por construção, e não por disciplina.
#
# E a linha da limpeza está ANTES do assert final, de propósito. Se o assert vem primeiro e
# falha, o programa para ali e o usuário nunca é apagado. Apague antes de julgar, sempre.
#
# REGRA DE NEGÓCIO (o que o slide projeta e o professor lê no início):
#   A consulta a um usuário existente responde 200 e o corpo traz nome, email, password,
#   administrador e _id. O e-mail devolvido é o que foi cadastrado, o nome não vem vazio, o
#   administrador é o texto true ou o texto false, e status diferente de 200 encerra a
#   verificação, porque não há corpo de usuário para conferir.

from uuid import uuid4

import requests

BASE_URL = "https://serverest.dev"
CAMPOS_OBRIGATORIOS = ["nome", "email", "password", "administrador", "_id"]


def email_unico(prefixo):
    return f"{prefixo}.{uuid4().hex}@qa.com.br"


def montar_payload(email):
    return {"nome": "Aluno Vertex", "email": email,
            "password": "Senha123", "administrador": "false"}


def validar_resposta_de_usuario(resposta, email_esperado):
    erros = []

    # degrau 1: o status. Errado aqui, para tudo: o corpo é uma mensagem de erro.
    if resposta.status_code != 200:
        erros.append(f"status: esperado 200, obtido {resposta.status_code}")
        return erros

    corpo = resposta.json()

    # degrau 2: a existência de cada campo
    for campo in CAMPOS_OBRIGATORIOS:
        if campo not in corpo:
            erros.append(f"campo ausente: {campo}")

    # degrau 3: o valor de cada campo. O .get() é o da Aula 5, e ele existe aqui para o degrau
    # 3 não derrubar o programa quando o degrau 2 já acusou o campo ausente.
    if corpo.get("email") != email_esperado:
        erros.append(f"email: esperado {email_esperado}, obtido {corpo.get('email')}")

    if corpo.get("nome", "").strip() == "":
        erros.append("nome: veio vazio")

    if corpo.get("administrador") not in ["true", "false"]:
        erros.append(f"administrador: esperado true ou false, "
                     f"obtido {corpo.get('administrador')}")

    return erros


def test_usuario_criado_passa_no_veredito():
    email = email_unico("veredito.vertex")
    criado = requests.post(f"{BASE_URL}/usuarios", json=montar_payload(email), timeout=10)
    assert criado.status_code == 201, criado.text
    id_criado = criado.json()["_id"]

    consulta = requests.get(f"{BASE_URL}/usuarios/{id_criado}", timeout=10)
    problemas = validar_resposta_de_usuario(consulta, email)

    requests.delete(f"{BASE_URL}/usuarios/{id_criado}", timeout=10)

    assert problemas == [], f"{len(problemas)} problema(s): " + "; ".join(problemas)


def test_veredito_reprova_usuario_inexistente():
    resposta = requests.get(f"{BASE_URL}/usuarios/aaaaaaaaaaaaaaaa", timeout=10)
    problemas = validar_resposta_de_usuario(resposta, "qualquer@qa.com.br")
    assert problemas == ["status: esperado 200, obtido 400"]

# --- EXPLICACAO LINHA A LINHA · gerado, nao edite aqui ---
#
# Gerado a partir de explicacao-linha-a-linha/slide-22.md.
# Nao edite este bloco: a proxima geracao substitui ele inteiro.
#
# A numeracao abaixo e a DESTE arquivo: a mesma da calha do PyCharm e a mesma
# que aparece no slide 22 da apresentacao.
#
#      26  BASE_URL = "https://serverest.dev"
#          Nada de novo.
#
#      27  CAMPOS_OBRIGATORIOS = [...]
#          Uma lista de cinco textos, no topo do arquivo. Constante de módulo
#          em caixa alta, e ela existe aqui para o laço da linha 50 percorrer.
#
#      39  def validar_resposta_de_usuario(resposta, email_esperado):
#          Dois parâmetros: o objeto que veio da rede e o valor que a regra
#          manda esperar. O segundo é o esperado, e ele vem de fora porque
#          quem sabe qual e-mail foi cadastrado é quem chamou.
#
#      40  erros = []
#          O acumulador da Aula 4 e da Aula 5, começando vazio. Lista vazia no
#          fim significa aprovado.
#
#      42  # degrau 1: o status
#          Comentário, e ele é o mapa da função.
#
#      43  if resposta.status_code != 200:
#          Degrau um.
#
#      44  erros.append(f"status: esperado 200, obtido
#          {resposta.status_code}")
#          A mensagem já traz esperado e obtido, que é o ESPERADO → OBTIDO →
#          CONFERE? da Aula 3 dentro do texto do problema.
#
#      45  return erros
#          O freio de mão da Aula 4 aplicado a função. Status errado, para
#          tudo: o corpo que voltou é uma mensagem de erro, e procurar o nome
#          do usuário dentro dela só produz confusão. Assim o degrau um é
#          respeitado por construção, e não por disciplina.
#
#      47  corpo = resposta.json()
#          Só chega aqui quem passou no degrau um.
#
#      49  # degrau 2: a existência de cada campo
#          Comentário.
#
#      50  for campo in CAMPOS_OBRIGATORIOS:
#          O for da Aula 4 sobre a lista do topo.
#
#      51  if campo not in corpo:
#          O in de dicionário da Aula 5, na forma negada.
#
#      52  erros.append(f"campo ausente: {campo}")
#          Aqui não tem return: o degrau dois acumula todos os campos ausentes
#          em vez de parar no primeiro.
#
# --- fim da explicacao linha a linha ---
