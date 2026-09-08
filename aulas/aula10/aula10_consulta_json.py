# Aula 10 - abrindo a carta: .json(), a leitura por chave e por posição, e o query parameter
#
# Até agora a gente olhou o envelope (status, cabeçalhos). Este arquivo abre o corpo da
# resposta, que é a estrutura da Aula 5 com os dados digitados por um servidor.
#
# REGRA DE NEGÓCIO (o que o slide projeta e o professor lê no início):
#   O corpo de GET /usuarios é um dicionário com as chaves quantidade e usuarios, e dentro
#   de usuarios uma lista de dicionários. Cada item tem nome, email e _id. O filtro por
#   params devolve só os itens que têm aquele nome, e o Requests monta a URL com o valor
#   codificado.

import requests

BASE_URL = "https://serverest.dev"

resposta = requests.get(f"{BASE_URL}/usuarios", timeout=10)
dados = resposta.json()

print(f"Tipo do que voltou: {type(dados)}")
print(f"Chaves do corpo: {list(dados.keys())}")
print(f"Quantidade de usuários: {dados['quantidade']}")

primeiro = dados["usuarios"][0]
print(f"Nome: {primeiro['nome']}")
print(f"E-mail: {primeiro['email']}")
print(f"ID: {primeiro['_id']}")

# --- os dois erros propositais moram em aula10_erro_json.py ---
#
# Eles ficavam comentados aqui, e comentário não roda: passavam a existir em dois lugares, este
# arquivo e o slide. Agora moram num arquivo próprio, que roda de verdade e mostra os dois na
# mesma execução. Rode: python aulas/aula10/aula10_erro_json.py

# --- query parameter: a mesma pergunta, filtrada ---
#
# O nome do filtro sai do primeiro usuário da própria lista, e não de um literal: assim o
# arquivo continua funcionando em qualquer dia, com qualquer base.
nome_do_primeiro = primeiro["nome"]
resposta_filtrada = requests.get(f"{BASE_URL}/usuarios", params={"nome": nome_do_primeiro}, timeout=10)

print(f"URL que o Requests montou: {resposta_filtrada.url}")
print(f"Quantidade filtrada: {resposta_filtrada.json()['quantidade']}")

# --- fim ---
#
# Regra desta aula: valide estrutura e regra, nunca valor específico de dado que não é seu. Dado
# público muda a hora que menos se espera, e "a quantidade filtrada é 1" é uma afirmação sobre um
# servidor que qualquer pessoa do mundo pode alterar.
