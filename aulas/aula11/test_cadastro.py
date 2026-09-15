# Aula 11 - primeira demonstração: cadastrar, conferir e limpar
#
# Rodar só o primeiro teste:  pytest test_cadastro.py::test_cadastro_de_usuario_com_sucesso -v
# Rodar os dois:              pytest test_cadastro.py -v
# Da raiz do repositório:     pytest aulas/aula11/test_cadastro.py -v
#
# O segundo teste PASSA quando recebe 400. O resultado esperado dele é a rejeição, e se um dia
# ele falhar dizendo que veio 201, aí sim há defeito, e grave: a loja passou a aceitar dois
# clientes com o mesmo e-mail.
#
# A asserção do e-mail duplicado é DUPLA, status e mensagem, e isso não é zelo: esta API
# devolve 400 para meia dúzia de motivos diferentes. Validando só o número, o teste continua
# verde no dia em que a recusa passar a ser por outro motivo.
#
# REGRA DE NEGÓCIO (o que o slide projeta e o professor lê no início):
#   Cadastrar com e-mail novo responde 201, com a chave message dizendo Cadastro realizado
#   com sucesso e a chave _id com o identificador. Cadastrar de novo com o mesmo e-mail
#   responde 400, com a mensagem Este email já está sendo usado.

from uuid import uuid4

import requests

BASE_URL = "https://serverest.dev"


def email_unico(prefixo):
    return f"{prefixo}.{uuid4().hex}@qa.com.br"


def montar_payload(email):
    return {"nome": "Aluno Vertex", "email": email,
            "password": "Senha123", "administrador": "false"}


def test_cadastro_de_usuario_com_sucesso():
    payload = montar_payload(email_unico("cadastro.vertex"))
    resposta = requests.post(f"{BASE_URL}/usuarios", json=payload, timeout=10)

    assert resposta.status_code == 201, \
        f"status inesperado: {resposta.status_code}, corpo: {resposta.text}"

    corpo = resposta.json()
    assert "message" in corpo
    assert "_id" in corpo
    assert corpo["message"] == "Cadastro realizado com sucesso"

    requests.delete(f"{BASE_URL}/usuarios/{corpo['_id']}", timeout=10)


def test_email_duplicado_e_rejeitado():
    payload = montar_payload(email_unico("duplicado.vertex"))

    primeira = requests.post(f"{BASE_URL}/usuarios", json=payload, timeout=10)
    assert primeira.status_code == 201, f"a primeira criação falhou: {primeira.text}"
    id_criado = primeira.json()["_id"]

    segunda = requests.post(f"{BASE_URL}/usuarios", json=payload, timeout=10)
    assert segunda.status_code == 400, f"status inesperado: {segunda.status_code}"
    assert segunda.json()["message"] == "Este email já está sendo usado"

    requests.delete(f"{BASE_URL}/usuarios/{id_criado}", timeout=10)

# --- EXPLICACAO LINHA A LINHA · gerado, nao edite aqui ---
#
# Gerado a partir de explicacao-linha-a-linha/slide-15.md.
# Nao edite este bloco: a proxima geracao substitui ele inteiro.
#
# A numeracao abaixo e a DESTE arquivo: a mesma da calha do PyCharm e a mesma
# que aparece no slide 15 da apresentacao.
#
#      40  assert resposta.status_code == 201, \
#          Degrau um: o status. A barra invertida no fim continua a linha, e
#          ela existe só para a mensagem caber na largura do arquivo.
#
#      41  f"status inesperado: {resposta.status_code}, corpo:
#          {resposta.text}"
#          A mensagem do assert carrega o status e o corpo inteiro. Quando
#          este teste falhar às onze da noite, o relatório diz o que o
#          servidor respondeu, sem ninguém precisar rodar de novo com print.
#
#      43  corpo = resposta.json()
#          Guardado numa variável em vez de chamar .json() quatro vezes. Cada
#          chamada decodifica o mesmo texto de novo.
#
#      44  assert "message" in corpo
#          Degrau dois: a existência. O in de dicionário da Aula 5.
#
#      45  assert "_id" in corpo
#          Degrau dois de novo, no segundo campo.
#
#      46  assert corpo["message"] == "Cadastro realizado com sucesso"
#          Degrau três: o valor. Só chega aqui quem passou nos dois primeiros.
#
#      48  requests.delete(f"{BASE_URL}/usuarios/{corpo['_id']}", timeout=10)
#          A limpeza. Este teste criou um usuário, e é ele quem apaga.
#
# --- fim da explicacao linha a linha ---
