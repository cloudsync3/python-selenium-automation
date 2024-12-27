from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import BasePage


class Header(BasePage):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
    CLICK_CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    ClK_SIGNIN_BTN = (By.XPATH, "//a[@data-test='@web/AccountLink']")
    CLK_SIDE_SIGNIN_BTN = (By.XPATH, "//button[@data-test='accountNav-signIn']")


    def search_product(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(10)

    def click_cart_icon(self):
        self.click(*self.CLICK_CART_ICON)

    def click_cart(self):
        self.wait_and_click(*self.CLICK_CART_ICON)

    def click_signin_button(self):
        self.click(*self.ClK_SIGNIN_BTN)

    def click_signin_right_side_button(self):
        self.click(*self.CLK_SIDE_SIGNIN_BTN)



