from pages.login_po import LoginPage

def test_login_success(page):
    login_page = LoginPage(page)
    
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    
    assert page.url == "https://www.saucedemo.com/inventory.html", "Не удалось перейти на страницу инвентаря после входа"
