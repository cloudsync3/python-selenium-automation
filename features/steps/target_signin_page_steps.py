from behave import given, when, then
from time import sleep


@given('Open Target sign in page')
def open_target_signin(context):
    context.app.target_signin_page.open_target_signin()


@given('Store original window')
def store_original_window(context):
    context.original_window = context.app.base_page.get_current_window_handle
    print(context.original_window)


@when('Click on Target terms and conditions link')
def click_tc_link(context):
    context.app.target_signin_page.click_tc_link()


@when('Switch to the new window')
def switch_window(context):
    # sleep(2)
    # print('All Windows', context.driver.window_handles)
    # context.driver.switch_to.window(context.driver.window_handles[1])
    context.app.target_signin_page.switch_to_new_window()


@then('Verify Terms and Conditions page opened')
def verify_tc_opened(context):
    context.app.terms_conditions_page.verify_tc_opened()


@then('User can close new window')
def close_page(context):
    context.app.terms_conditions_page.close()


@then('switch window to original')
def return_to_window(context):
    context.app.terms_conditions_page.switch_to_window_by_id(context.original_window)



