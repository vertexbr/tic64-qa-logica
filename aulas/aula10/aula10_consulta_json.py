# Aula 10 - abrindo a carta: .json(), os dois erros propositais e o query parameter
#
# Ate agora a gente olhou o envelope (status, cabecalhos). Este arquivo abre o corpo da resposta.
import requests

BASE_URL = "https://serverest.dev"

resposta = requests.get(f"{BASE_URL}/usuarios", timeout=10)
dados = resposta.json()

print(f"Tipo do que voltou: {type(dados)}")
print(f"Chaves do corpo: {list(dados.keys())}")
print(f"Quantidade de usuarios: {dados['quantidade']}")

primeiro = dados["usuarios"][0]
print(f"Nome: {primeiro['nome']}")
print(f"E-mail: {primeiro['email']}")
print(f"ID: {primeiro['_id']}")

# --- erro proposital 1: .json() numa resposta que nao e JSON ---
#
# Comente as duas linhas abaixo para rodar o resto do arquivo sem travar: elas existem para
# aparecer na tela quebradas, de proposito. O status vem 200 e o programa estoura assim mesmo,
# porque o que voltou foi uma pagina HTML, nao JSON.
#
# resposta_html = requests.get("https://the-internet.herokuapp.com/login", timeout=10)
# print(resposta_html.status_code)
# print(resposta_html.json())          # requests.exceptions.JSONDecodeError

# --- erro proposital 2: a chave que nao existe ---
#
# Troque "quantidade" por "quantidadee" para ver o KeyError da Aula 5 de novo. So que agora ele
# pode significar duas coisas: erro de digitacao, ou o contrato da API mudou e ninguem avisou.
print(f"Confirmando a chave certa: {dados['quantidade']}")

# --- query parameter: a mesma pergunta, filtrada ---
#
# O nome usado aqui e o do primeiro usuario da lista no dia em que este arquivo foi escrito.
# Rodar de novo pode trazer outro nome, porque a base e publica.
nome_do_primeiro = primeiro["nome"]
resposta_filtrada = requests.get(f"{BASE_URL}/usuarios", params={"nome": nome_do_primeiro}, timeout=10)

print(f"URL que o Requests montou: {resposta_filtrada.url}")
print(f"Quantidade filtrada: {resposta_filtrada.json()['quantidade']}")

# --- fim ---
#
# Regra desta aula: valide estrutura e regra, nunca valor especifico de dado que nao e seu. Dado
# publico muda a hora que menos se espera, e "a quantidade filtrada e 1" e uma afirmacao sobre um
# servidor que qualquer pessoa do mundo pode alterar.
