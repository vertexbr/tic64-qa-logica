from playwright.sync_api import Page, expect


def test_compra_um_produto(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    page.get_by_role("button", name="Add to cart").first.click()
    page.locator(".shopping_cart_link").click()

    expect(page.locator(".cart_item")).to_have_count(1)
