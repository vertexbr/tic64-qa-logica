# Aula 10 - abrindo a carta: .json(), a leitura por chave e por posicao, e o query parameter
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

# --- os dois erros propositais moram em aula10_erro_json.py ---
#
# Eles ficavam comentados aqui, e comentario nao roda: passavam a existir em dois lugares, este
# arquivo e o slide. Agora moram num arquivo proprio, que roda de verdade e mostra os dois na
# mesma execucao. Rode: python aulas/aula10/aula10_erro_json.py

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
