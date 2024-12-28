from selenium.webdriver.common.by import By


from pages.base_page import BasePage

class TermsConditionsPage(BasePage):

    def verify_tc_opened(self):
        self.verify_partial_url('/c/terms-conditions/')
