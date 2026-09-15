# test_acoes.py
#
# REGRA DE NEGÓCIO
# Marcar uma caixa de seleção é idempotente: chamar duas vezes deixa marcada. Clicar alterna
# o estado: a segunda caixa desta página já vem marcada, e um clique nela desmarca.

from playwright.sync_api import Page, expect


def test_tres_comportamentos(page: Page):
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    caixas = page.get_by_role("checkbox")
    primeira = caixas.first
    segunda = caixas.last

    # marcar é idempotente: chamar duas vezes deixa marcado
    primeira.check()
    primeira.check()
    expect(primeira).to_be_checked()

    # clicar alterna: a segunda já vinha marcada, e o clique desmarcou
    segunda.click()
    expect(segunda).not_to_be_checked()
