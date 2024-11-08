class InventoryPage:
    def __init__(self, page):
        self.page = page

        self.add_to_cart_button_prefix = "[data-test='add-to-cart-"
        self.add_to_cart_button_id_prefix = "button[id='add-to-cart-"
        self.open_cart_button = "[data-test='shopping-cart-link']"
        self.sort_container = "select.product_sort_container"

        self.item_price_locator = "[data-test='inventory-item-price']"
        self.add_all_buttons_locator = "button.btn_inventory"
        self.cart_badge_locator = ".shopping_cart_badge"
        self.inventory_item_locator = ".inventory_item"

    def add_to_cart_by_name(self, product_name: str) -> None:
        locator = f"{self.add_to_cart_button_prefix}{product_name}']"
        self.page.click(locator)

    def add_to_cart_by_id(self, item_id: str) -> None:
        locator = f"{self.add_to_cart_button_id_prefix}{item_id}']"
        self.page.click(locator)

    def add_all_items_to_cart(self) -> None:
        add_buttons = self.page.locator(self.add_all_buttons_locator).all()
        for button in add_buttons:
            button.click()

    def open_cart(self) -> None:
        self.page.click(self.open_cart_button)

    def sort_items(self, sort_type: str) -> None:
        self.page.select_option(self.sort_container, sort_type)

    def get_item_prices(self) -> list[float]:
        prices = self.page.locator(self.item_price_locator).all_text_contents()
        return [float(price.replace('$', '')) for price in prices]

    def get_cart_count(self) -> int:
        cart_count_text = self.page.locator(self.cart_badge_locator).text_content()
        return int(cart_count_text) if cart_count_text else 0

    def get_total_item_count(self) -> int:
        return len(self.page.locator(self.inventory_item_locator).all())

    def get_total_items_names(self) -> list[str]:
        items = self.page.locator(self.inventory_item_locator).all()
        return [item.inner_text() for item in items]
