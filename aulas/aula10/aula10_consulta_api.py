# Aula 10 - o arquivo da primeira demonstracao: dois GET, dois recursos, so olhando
#
# Este e o arquivo que eu escrevo na frente da turma no primeiro bloco de demonstracao. Ele nao
# valida nada de proposito: imprime e para. Imprimir nao julga, quem julga e quem olha a tela, e
# a partir do segundo ciclo o print sai e o assert entra.
import requests

BASE_URL = "https://serverest.dev"

resposta_produtos = requests.get(f"{BASE_URL}/produtos", timeout=10)
print(f"Produtos, status: {resposta_produtos.status_code}")
print(f"Produtos, tipo: {resposta_produtos.headers.get('Content-Type')}")

resposta_usuarios = requests.get(f"{BASE_URL}/usuarios", timeout=10)
print(f"Usuários, status: {resposta_usuarios.status_code}")

# --- fim ---
#
# Saida conferida contra a API real em 08/09/2026: os dois status saem 200 e o tipo de conteudo
# sai application/json; charset=utf-8. Ninguem precisou abrir navegador, e essa e a economia
# inteira do teste de API: quatro linhas fazem o que um clique fazia, e fazem cinquenta vezes em
# dois segundos.
#
# O desafio para quem terminou antes: pedir /usuariosss, com tres esses, e ler a mensagem que o
# servidor devolve. Ele responde 405, e a mensagem aponta a documentacao.
