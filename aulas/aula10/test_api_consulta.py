# Aula 10 - os três degraus da asserção virando código
#
# Rodar de dentro da pasta: pytest test_api_consulta.py -v
# Rodar da raiz do repositório: pytest aulas/aula10/test_api_consulta.py -v
#
# REGRA DE NEGÓCIO (o que o slide projeta e o professor lê no início):
#   A ordem canônica de asserção é status, existência do campo e valor do campo. O status
#   esperado de GET /usuarios é 200, e o corpo tem que trazer quantidade e usuarios. O valor
#   só se afirma quando é regra: a quantidade declarada é igual ao tamanho da lista devolvida.

import requests

BASE_URL = "https://serverest.dev"


def test_listar_usuarios_respeita_os_tres_degraus():
    resposta = requests.get(f"{BASE_URL}/usuarios", timeout=10)

    # degrau 1: o status
    assert resposta.status_code == 200, f"status inesperado: {resposta.status_code}"

    corpo = resposta.json()

    # degrau 2: a existência dos campos
    assert "quantidade" in corpo
    assert "usuarios" in corpo

    # degrau 3: o valor, e aqui só o que é regra
    assert corpo["quantidade"] == len(corpo["usuarios"])
