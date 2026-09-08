# Aula 10 - os tres degraus da asserção virando código
#
# Rodar de dentro da pasta: pytest test_api_consulta.py -v
# Rodar da raiz do repositorio: pytest aulas/aula10/test_api_consulta.py -v
import requests

BASE_URL = "https://serverest.dev"


def test_listar_usuarios_respeita_os_tres_degraus():
    resposta = requests.get(f"{BASE_URL}/usuarios", timeout=10)

    # degrau 1: o status
    assert resposta.status_code == 200, f"status inesperado: {resposta.status_code}"

    corpo = resposta.json()

    # degrau 2: a existencia dos campos
    assert "quantidade" in corpo
    assert "usuarios" in corpo

    # degrau 3: o valor, e aqui so o que e regra
    assert corpo["quantidade"] == len(corpo["usuarios"])
