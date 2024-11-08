from pages.login_po import LoginPage
from pages.inventory_po import InventoryPage

def test_sort_items_by_price(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    page.goto("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")

    inventory_page.sort_items("lohi")
    prices = inventory_page.get_item_prices()
    
    assert prices == sorted(prices), "Цены не отсортированы по возрастанию"

    inventory_page.sort_items("hilo")
    prices = inventory_page.get_item_prices()

    assert prices == sorted(prices, reverse=True), "Цены не отсортированы по убыванию"