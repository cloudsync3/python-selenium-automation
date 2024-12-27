from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SigninPage(BasePage):
    SIGNIN_BTN = (By.ID, 'login')

    def signin_button(self, *locator):
        self.driver.find_element(*self.SIGNIN_BTN)






