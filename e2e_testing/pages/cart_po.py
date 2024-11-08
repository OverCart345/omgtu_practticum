class CartPage:
    def __init__(self, page):
        self.page = page

        self.checkout_button = "button#checkout"
        self.first_name_input = "input#first-name"
        self.last_name_input = "input#last-name"
        self.postal_code_input = "input#postal-code"
        self.continue_button = "input#continue"
        self.finish_button = "button#finish"
        self.cart_item_locator = ".cart_item"
        self.remove_button_prefix = "[data-test='remove-"
        self.error_message_locator = "[data-test='error']"
        self.button_cancel = page.locator('[data-test="cancel"]')
        self.button_back_to_products = page.locator('[data-test="back-to-products"]')
        self.remove_buttons = page.locator("button:has-text('Remove')")
        self.cart_items = page.locator(".cart_item")

    def checkout(self) -> None:
        self.page.click(self.checkout_button)

    def fill_checkout_info(self, first_name: str, last_name: str, postal_code: str) -> None:
        self.page.fill(self.first_name_input, first_name)
        self.page.fill(self.last_name_input, last_name)
        self.page.fill(self.postal_code_input, postal_code)
        self.page.click(self.continue_button)

    def finish_checkout(self) -> None:
        self.page.click(self.finish_button)

    def click_button_cancel(self) -> None:
        self.button_cancel.click()

    def click_button_back_to_products(self) -> None:
        self.button_back_to_products.click()

    def get_cart_items(self) -> list[str]:
        return self.page.locator(self.cart_item_locator).all_text_contents()

    def remove_from_cart_by_id(self, item_id: str) -> None:
        locator = f"{self.remove_button_prefix}{item_id}']"
        self.page.click(locator)

    def remove_item_by_name(self, product_name: str) -> None:
        locator = f"{self.remove_button_prefix}{product_name}']"
        self.page.click(locator)

    def remove_all_items(self) -> None:
        total_items = self.cart_items.count()
        for _ in range(total_items):
            self.remove_buttons.nth(0).click()

    def get_cart_list(self) -> list[str]:
        return self.cart_items.all_text_contents()

    def is_error_visible(self) -> bool:
        return self.page.is_visible(self.error_message_locator)
