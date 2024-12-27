from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    EMPTY_CART_MSG = (By.XPATH, "//div[@data-test='boxEmptyMsg']")


    def step_verify_cart_message(self):
        self.verify_text('Your cart is empty', *self.EMPTY_CART_MSG)



