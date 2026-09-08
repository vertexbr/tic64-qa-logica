# Aula 10 - os dois erros propositais da aula, cada um numa funcao que roda de verdade
#
# Os dois erros deste arquivo acontecem de proposito. Eles estao embrulhados em try/except para o
# arquivo seguir ate o fim e mostrar os dois na mesma execucao. AVISO, e ele vale como conteudo:
# engolir erro assim serve para DEMONSTRAR o erro, e e o oposto do que se faz num teste de
# verdade. Numa suite, a falha interrompe, e e isso que faz o relatorio significar alguma coisa.
import requests

BASE_URL = "https://serverest.dev"


def erro_1_json_no_que_nao_e_json():
    """Status 200 e o programa estoura: o que voltou foi HTML, e .json() so abre JSON."""
    resposta = requests.get("https://the-internet.herokuapp.com/login", timeout=10)
    print(f"Status: {resposta.status_code}")
    try:
        print(resposta.json())
    except requests.exceptions.JSONDecodeError as erro:
        print(f"{type(erro).__name__}: {erro}")
        print(f"E o que voltou de verdade comeca assim: {resposta.text[:15]}")


def erro_2_a_chave_que_nao_existe():
    """O KeyError da Aula 5 de novo, com um motivo novo: o contrato da API pode ter mudado."""
    dados = requests.get(f"{BASE_URL}/usuarios", timeout=10).json()
    try:
        print(dados["quantidadee"])
    except KeyError as erro:
        print(f"{type(erro).__name__}: {erro}")
        print(f"As chaves que existem de verdade: {list(dados.keys())}")


erro_1_json_no_que_nao_e_json()
print()
erro_2_a_chave_que_nao_existe()

# --- fim ---
#
# Saida conferida contra a API real em 08/09/2026. O primeiro erro e o mais importante dos dois,
# porque ele confunde: o status esta otimo e o programa quebrou. Quando essa mensagem aparecer, a
# pergunta certa e "eu pedi para o endereco certo?", e imprimir resposta.text responde.
#
# O segundo erro pode significar duas coisas, e distinguir e o trabalho: erro de digitacao seu, ou
# o contrato da API mudou e ninguem avisou. O segundo e defeito de verdade, e e por isso que o
# degrau dois da ordem canonica existe.
