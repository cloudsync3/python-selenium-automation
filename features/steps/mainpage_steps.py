from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
# from time import sleep

SEARCH_FIELD = (By.ID, 'search')
SEARCH_BTN = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")

@given('Open target main page')
def open_main(context):
    context.driver.get('https://www.target.com')


@when('Search for {product}')
def search_product(context, product):
    context.driver.find_element(*SEARCH_FIELD).send_keys(product)
    context.driver.wait.until(EC.visibility_of_element_located(SEARCH_BTN))
    context.driver.find_element(*SEARCH_BTN).click()
    # sleep(10)


@then('Search results for {product} are displayed')
def search_results(context, product):
    actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert product in actual_result, f'Expected text {product} not in actual {actual_result}'