# Aula 11 - treino em casa: fechar o ciclo com o login
#
# Este arquivo NÃO passa no deck. Ele é o treino que fecha o desafio deixado no fim da Aula 10,
# e tem seção própria no guia de estudo.
#
# Rodar:                   pytest aula11_login_token.py -v
# Da raiz do repositório:  pytest aulas/aula11/aula11_login_token.py -v
#
# O login devolve um token, e o token é a chave que endpoints protegidos exigem. Ele não é
# assunto desta aula: aparece aqui como porta de entrada do desafio final.
#
# O 401 do segundo teste é honesto, e vale reparar: senha errada é problema de autenticação, e
# não de formato. É o único caso da aula em que esta API não responde 400.
#
# REGRA DE NEGÓCIO:
#   Autenticar com o e-mail e a senha de um usuário cadastrado responde 200, com a chave
#   authorization trazendo um token que começa com "Bearer ". Autenticar com senha errada
#   responde 401, com a mensagem "Email e/ou senha inválidos".

import time

import requests

BASE_URL = "https://serverest.dev"


def email_unico(prefixo):
    return f"{prefixo}.{int(time.time())}@qa.com.br"


def montar_payload(email):
    return {"nome": "Aluno Vertex", "email": email,
            "password": "Senha123", "administrador": "false"}


def test_login_devolve_token():
    email = email_unico("login.vertex")
    payload = montar_payload(email)
    criado = requests.post(f"{BASE_URL}/usuarios", json=payload, timeout=10)
    assert criado.status_code == 201, criado.text

    login = requests.post(f"{BASE_URL}/login",
                          json={"email": email, "password": payload["password"]}, timeout=10)

    requests.delete(f"{BASE_URL}/usuarios/{criado.json()['_id']}", timeout=10)

    assert login.status_code == 200, f"status inesperado: {login.status_code}"
    assert "authorization" in login.json()
    assert login.json()["authorization"].startswith("Bearer ")


def test_login_com_senha_errada_e_recusado():
    resposta = requests.post(f"{BASE_URL}/login",
                             json={"email": "fulano@qa.com", "password": "errada"}, timeout=10)
    assert resposta.status_code == 401, f"status inesperado: {resposta.status_code}"
    assert resposta.json()["message"] == "Email e/ou senha inválidos"
