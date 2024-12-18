from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CLICK_CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
EMPTY_CART_MSG = (By.XPATH, "//div[@data-test='boxEmptyMsg']")

@when('Click on the Cart icon')
def click_cart_icon(context):
    context.driver.find_element(*CLICK_CART_ICON).click()
    context.app.header.click_cart_icon()


@then('Verify cart is empty message')
def step_verify_cart_message(context):
    context.app.cart_page.step_verify_cart_message()
