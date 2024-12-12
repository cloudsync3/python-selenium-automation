from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click on the Sign in button')
def click_signin_button(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']").click()
    sleep(3)


@then('Click Sign in from right navigation')
def click_signin_right_side_button(context):
    context.driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()
    sleep(3)


@then('Should see the Sign in button')
def signin_button(context):
    context.driver.find_element(By.ID, 'login')





