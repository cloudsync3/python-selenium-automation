from selenium.webdriver.common.by import By
from behave import given, when, then


SEARCH_FIELD = (By.ID, 'search')
SEARCH_BTN = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")


@given('Open target main page')
def open_main(context):
    context.app.main_page.open_main()


@when('Search for {product}')
def search_product(context, product):
    context.app.header.search_product(product)


# @then('Verify results for {product} are displayed')
# def search_results(context, product):
#     context.app.search_results_page.verify_search_results_page()
#     # actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
#     # assert product in actual_result, f'Expected text {product} not in actual {actual_result}'