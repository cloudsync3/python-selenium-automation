from selenium.webdriver.common.by import By


from pages.base_page import BasePage

class TargetSigninPage(BasePage):
        TC_LINK = (By.XPATH, "//a[text()='Target terms and conditions']")


        def open_target_signin(self):
            self.open_url('https://www.target.com/login')


        def click_tc_link(self):
            self.click(*self.TC_LINK)