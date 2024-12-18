from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    EMPTY_CART_MSG = (By.XPATH, "//div[@data-test='boxEmptyMsg']")


    def step_verify_cart_message(self):
        expected = 'Your cart is empty'
        actual = self.driver.find_element(*self.EMPTY_CART_MSG).text
        assert expected == actual, f'Expected {expected} did not match actual {actual}'



