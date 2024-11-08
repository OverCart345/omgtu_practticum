from pages.login_po import LoginPage
from pages.inventory_po import InventoryPage
from pages.cart_po import CartPage

def test_cart_persistence_after_logout(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)

    page.goto("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_to_cart_by_id("sauce-labs-backpack")
    cart_count = inventory_page.get_cart_count()
    assert cart_count == 1, f"Ожидался 1 товар в корзине, но их {cart_count}"

    inventory_page.add_to_cart_by_id("sauce-labs-bike-light")
    cart_count = inventory_page.get_cart_count()
    assert cart_count == 2, f"Ожидалось 2 товара в корзине, но их {cart_count}"

    inventory_page.page.click("button#react-burger-menu-btn")
    inventory_page.page.click("a#logout_sidebar_link")

    assert page.url == "https://www.saucedemo.com/", "Ожидался переход на страницу логина после выхода"

    login_page.login("standard_user", "secret_sauce")

    inventory_page.open_cart()
    cart_items = cart_page.get_cart_items()

    print(f"Товары в корзине после повторного входа: {cart_items}")

    assert any("Sauce Labs Backpack" in item for item in cart_items), "Товар 'Sauce Labs Backpack' не найден в корзине после повторного входа"
    assert any("Sauce Labs Bike Light" in item for item in cart_items), "Товар 'Sauce Labs Bike Light' не найден в корзине после повторного входа"

    assert len(cart_items) == 2, f"Ожидалось, что в корзине будет 2 товара после повторного входа, но их {len(cart_items)}"
