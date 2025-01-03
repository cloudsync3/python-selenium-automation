from pages.base_page import BasePage
from pages.header import Header
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.cart_page import CartPage
from pages.signin_page import SigninPage
from pages.target_signin_page import TargetSigninPage
from pages.terms_conditions_page import TermsConditionsPage


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.base_page = BasePage(driver)
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.cart_page = CartPage(driver)
        self.signin_page = SigninPage(driver)
        self.target_signin_page = TargetSigninPage(driver)
        self.terms_conditions_page = TermsConditionsPage(driver)


