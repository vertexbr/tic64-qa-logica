# Aula 10 - os dois erros propositais da aula, cada um numa função que roda de verdade
#
# Os dois erros deste arquivo acontecem de propósito. Eles estão embrulhados em try/except
# para o arquivo seguir até o fim e mostrar os dois na mesma execução. AVISO, e ele vale como
# conteúdo: engolir erro assim serve para DEMONSTRAR o erro, e é o oposto do que se faz num
# teste de verdade. Numa suíte, a falha interrompe, e é isso que faz o relatório significar
# alguma coisa.
#
# REGRA DE NEGÓCIO (o que o slide projeta e o professor lê no início):
#   O método .json() só abre corpo que é JSON. Uma página HTML derruba com JSONDecodeError
#   mesmo com status 200, porque status bom não garante corpo certo. Chave que não existe no
#   corpo derruba com KeyError, e num teste de API isso pode significar contrato alterado.

import requests

BASE_URL = "https://serverest.dev"


def erro_1_json_no_que_nao_e_json():
    """Status 200 e o programa estoura: o que voltou foi HTML, e .json() só abre JSON."""
    resposta = requests.get("https://the-internet.herokuapp.com/login", timeout=10)
    print(f"Status: {resposta.status_code}")
    try:
        print(resposta.json())
    except requests.exceptions.JSONDecodeError as erro:
        print(f"{type(erro).__name__}: {erro}")
        print(f"E o que voltou de verdade começa assim: {resposta.text[:15]}")


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
# Saída conferida contra a API real em 08/09/2026. O primeiro erro é o mais importante dos dois,
# porque ele confunde: o status está ótimo e o programa quebrou. Quando essa mensagem aparecer, a
# pergunta certa é "eu pedi para o endereço certo?", e imprimir resposta.text responde.
#
# O segundo erro pode significar duas coisas, e distinguir é o trabalho: erro de digitação seu, ou
# o contrato da API mudou e ninguém avisou. O segundo é defeito de verdade, e é por isso que o
# degrau dois da ordem canônica existe.
