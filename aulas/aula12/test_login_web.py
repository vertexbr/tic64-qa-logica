# test_login_web.py
#
# REGRA DE NEGÓCIO
# Login com usuário e senha corretos leva à área segura, com a mensagem "You logged into a
# secure area!". Senha errada recusa com "Your password is invalid!", e usuário errado
# recusa com "Your username is invalid!": duas mensagens diferentes para dois problemas
# diferentes.

from playwright.sync_api import Page, expect


def test_login_com_sucesso(page: Page):
    # Preparação: abrir a página de login
    page.goto("https://the-internet.herokuapp.com/login")

    # Ação: preencher e enviar
    campo_usuario = page.get_by_label("Username")
    campo_usuario.fill("tomsmith")
    expect(campo_usuario).to_have_value("tomsmith")
    page.get_by_label("Password").fill("SuperSecretPassword!")
    page.get_by_role("button", name="Login").click()

    # Validação: entrou
    expect(page.get_by_role("heading", name="Secure Area", exact=True)).to_be_visible()
    expect(page.locator("#flash")).to_contain_text("You logged into a secure area")


def test_login_com_senha_errada(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.get_by_label("Username").fill("tomsmith")
    page.get_by_label("Password").fill("senha_errada")
    page.get_by_role("button", name="Login").click()

    expect(page.locator("#flash")).to_contain_text("Your password is invalid!")


def test_login_com_usuario_errado(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.get_by_label("Username").fill("usuario_errado")
    page.get_by_label("Password").fill("SuperSecretPassword!")
    page.get_by_role("button", name="Login").click()

    expect(page.locator("#flash")).to_contain_text("Your username is invalid!")
