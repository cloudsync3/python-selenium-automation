from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class SearchResultsPage(BasePage):
    SEARCH_RESULTS = (By.XPATH, "//div[@data-test='resultsHeading']")
    ADD_TO_CART = (By.CSS_SELECTOR, "[id*='addToCartButton']")
    CONFIRM_ADD_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
    ADDED_PROD = (By.CSS_SELECTOR, '.h-text-grayDarkest.h-text-bold.h-text-lg')

    def verify_search_results_page(self, product):
        self.verify_partial_text(product, *self.SEARCH_RESULTS)

    def search_url(self, product):
        url = self.driver.current_url
        assert product in url, f'{product} not in URL'

    def verify_partial_url(self, product):
        self.verify_partial_url(product)

    def click_add_to_cart(self):
        self.wait_and_click(*self.ADD_TO_CART)

    def add_to_cart(self):
        self.find_element(*self.CONFIRM_ADD_BTN)

    def added_product(self):
        self.find_element(*self.ADDED_PROD)



