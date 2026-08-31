"""Verificação de ambiente do curso, a mesma do guia de setup.

Este é o arquivo que o guia de setup manda criar antes da Aula 01, e agora ele
mora no repositório: da Aula 08 em diante o pytest existe para a turma, e não
faz mais sentido cada um digitar o arquivo na mão.

Rode da raiz do repositório, com o `(.venv)` ativo:

    pytest tests/test_setup.py -v

Três testes, e cada um confere uma coisa diferente:

    test_python_funciona ....... o Python e o pytest respondem. Não usa rede.
    test_requests_funciona ..... a biblioteca Requests está instalada e a sua
                                 máquina alcança o serverest. PRECISA DE INTERNET.
    test_playwright_funciona ... o Chromium abre pela automação. PRECISA DO
                                 NAVEGADOR baixado com `playwright install chromium`.

Se aparecer `3 passed`, o ambiente está pronto para as 15 aulas.

Os dois últimos dependem de coisa que não é o seu código: rede fora do ar e
navegador não instalado deixam eles vermelhos sem que exista defeito nenhum. É
o primeiro exemplo real da heurística da Aula 08: o vermelho aqui não acusa o
produto, acusa o ambiente.

Para ver o navegador abrindo, em vez de rodar escondido:

    pytest tests/test_setup.py::test_playwright_funciona --headed --slowmo 1000
"""
import requests
from playwright.sync_api import Page, expect


def test_python_funciona():
    resultado = 2 + 2
    assert resultado == 4


def test_requests_funciona():
    resposta = requests.get("https://serverest.dev/usuarios", timeout=10)
    assert resposta.status_code == 200
    assert "quantidade" in resposta.json()


def test_playwright_funciona(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    expect(page.get_by_role("heading", name="Login Page")).to_be_visible()
