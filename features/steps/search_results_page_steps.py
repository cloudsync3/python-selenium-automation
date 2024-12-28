from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


ADD_TO_CART = (By.CSS_SELECTOR, "[id*='addToCartButton']")
CONFIRM_ADD_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
ADDED_PROD = (By.CSS_SELECTOR, '.h-text-grayDarkest.h-text-bold.h-text-lg')

# @given('Open target main page')
# def open_main(context):
#     context.driver.get('https://www.target.com')


# @when('Search for {product}')
# def search_product(context, product):
#     context.driver.find_element(By.ID, 'search').send_keys(product)
#     context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']").click()
#     sleep(10)

@then('Verify results for {product} are displayed')
def search_results(context, product):
    context.app.search_results_page.search_results_page(product)


@then('Verify search term {product} in URL')
def search_url(context, product):
    context.app.search_results_page.search_url(product)


@when('Click on add to cart button')
def click_add_to_cart(context):
    context.app.search_results_page.click_add_to_cart()
    # context.driver.wait.until(EC.visibility_of_element_located(CONFIRM_ADD_BTN))


@when('Confirm add to cart button side navigation')
def add_to_cart(context):
    context.app.search_results_page.add_to_cart()


@then('Product should be added to the cart')
def added_product(context):
    # context.driver.wait.until(EC.element_to_be_clickable(CONFIRM_ADD_BTN))
    context.app.search_results_page.added_product()


