from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify cart is empty message')
def step_verify_cart_message(context):
    expected = 'Your cart is empty'
    actual = context.driver.find_element(By.XPATH, "//div[@data-test='boxEmptyMsg']").text
    assert expected == actual, f'Expected {expected} did not match actual {actual}'

