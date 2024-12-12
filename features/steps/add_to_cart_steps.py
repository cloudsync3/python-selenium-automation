from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

# @given('Open target main page')
# def open_main(context):
#     context.driver.get('https://www.target.com')


# @when('Search for {product}')
# def search_product(context, product):
#     context.driver.find_element(By.ID, 'search').send_keys(product)
#     context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']").click()
#     sleep(10)


@when('Add product to the cart')
def add_to_cart(context):
    context.driver.find_element(By.ID, "addToCartButtonOrTextIdFor91188095").click()
    sleep(2)
    context.driver.find_element(By.CSS_SELECTOR, "button[data-test='shippingButton']").click()
    sleep(4)

@then('Product should be added to the cart')
def added_product(context):
    cart_button = context.driver.find_element(By.CSS_SELECTOR, '.h-text-grayDarkest.h-text-bold.h-text-lg')
    context.driver.quit()

