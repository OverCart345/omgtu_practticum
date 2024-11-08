from pages.login_po import LoginPage
from pages.inventory_po import InventoryPage
from pages.cart_po import CartPage

def test_add_to_cart(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    inventory_page.add_to_cart_by_id("sauce-labs-backpack")
    inventory_page.open_cart()
    
    assert page.is_visible("div.inventory_item_name"), "Товар не отображается в корзине"
