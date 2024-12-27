from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
# from time import sleep

ClK_SIGNIN_BTN = (By.XPATH, "//a[@data-test='@web/AccountLink']")
CLK_SIDE_SIGNIN_BTN = (By.XPATH, "//button[@data-test='accountNav-signIn']")
SIGNIN_BTN = (By.ID, 'login')


@when('Click on the Sign in button')
def click_signin_button(context):
    context.app.header.click_signin_button()
    # context.driver.wait.until(EC.element_to_be_clickable(CLK_SIDE_SIGNIN_BTN))


@then('Click Sign in from right navigation')
def click_signin_right_side_button(context):
    context.app.header.click_signin_right_side_button()
    # context.driver.wait.until(EC.presence_of_element_located(SIGNIN_BTN))


@then('Should see the Sign in button')
def signin_button(context):
    context.app.signin_page.signin_button()
    # context.driver.wait.until(EC.presence_of_element_located(SIGNIN_BTN))






