# Aula 10 - o arquivo da primeira demonstração: dois GET, dois recursos, só olhando
#
# Este é o arquivo que eu escrevo na frente da turma no primeiro bloco de demonstração. Ele
# não valida nada de propósito: imprime e para. Imprimir não julga, quem julga é quem olha a
# tela, e a partir do segundo ciclo o print sai e o assert entra.
#
# REGRA DE NEGÓCIO (o que o slide projeta e o professor lê no início):
#   Consultar não estraga nada, então o GET é o lugar seguro para errar. Este arquivo só
#   imprime status e tipo de conteúdo de dois recursos, e imprimir não julga: por isso ele
#   ainda não é teste.

import requests

BASE_URL = "https://serverest.dev"

resposta_produtos = requests.get(f"{BASE_URL}/produtos", timeout=10)
print(f"Produtos, status: {resposta_produtos.status_code}")
print(f"Produtos, tipo: {resposta_produtos.headers.get('Content-Type')}")

resposta_usuarios = requests.get(f"{BASE_URL}/usuarios", timeout=10)
print(f"Usuários, status: {resposta_usuarios.status_code}")

# --- fim ---
#
# Saída conferida contra a API real em 08/09/2026: os dois status saem 200 e o tipo de conteúdo
# sai application/json; charset=utf-8. Ninguém precisou abrir navegador, e essa é a economia
# inteira do teste de API: quatro linhas fazem o que um clique fazia, e fazem cinquenta vezes em
# dois segundos.
#
# O treino que vem com este arquivo: peça /usuariosss, com três esses, e leia a mensagem que o
# servidor devolve. Ele responde 405, e a mensagem aponta a documentação.
