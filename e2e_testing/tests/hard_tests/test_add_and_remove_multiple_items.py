from pages.login_po import LoginPage
from pages.inventory_po import InventoryPage
from pages.cart_po import CartPage

def test_add_and_remove_multiple_items(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)

    page.goto("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_to_cart_by_id("sauce-labs-backpack")
    inventory_page.open_cart()
    cart_items = cart_page.get_cart_items()
    assert len(cart_items) == 1, "Первый товар не добавлен в корзину"
    
    page.goto("https://www.saucedemo.com/inventory.html")
    
    inventory_page.add_to_cart_by_id("sauce-labs-bike-light")
    inventory_page.open_cart()
    cart_items = cart_page.get_cart_items()
    assert len(cart_items) == 2, "Второй товар не добавлен в корзину"

    page.goto("https://www.saucedemo.com/inventory.html")
    
    inventory_page.add_to_cart_by_id("sauce-labs-bolt-t-shirt")
    inventory_page.open_cart()
    cart_items = cart_page.get_cart_items()
    assert len(cart_items) == 3, "Третий товар не добавлен в корзину"

    cart_page.remove_from_cart_by_id("sauce-labs-backpack")
    cart_items = cart_page.get_cart_items()
    assert len(cart_items) == 2, "Первый товар не удалён из корзины"
    
    cart_page.remove_from_cart_by_id("sauce-labs-bike-light")
    cart_items = cart_page.get_cart_items()
    assert len(cart_items) == 1, "Второй товар не удалён из корзины"
    
    cart_page.remove_from_cart_by_id("sauce-labs-bolt-t-shirt")
    cart_items = cart_page.get_cart_items()
    assert len(cart_items) == 0, "Корзина должна быть пуста"