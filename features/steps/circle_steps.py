from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target Circle page')
def open_main(context):
    context.driver.get('https://www.target.com/circle')


@then('Verify at least 10 benefit cells')
def verify_benefit_cells_amount(context):
    benefit_cells = context.driver.find_elements(By.CSS_SELECTOR, ".cell-item-content")
    print('\nFind cells:')
    print(benefit_cells)
    print(type(benefit_cells))

    assert len(benefit_cells) > 10, f'Expected 10 links but found {len(benefit_cells)}'
