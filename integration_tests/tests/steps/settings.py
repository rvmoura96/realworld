from time import sleep

from behave import given, then, when
from expects import equal, expect

from modules.auxiliar import cast_table_to_dict
from pages_objects.pos import Home, Logged, Settings, SignUp


@when("the user click on settings")
def step_impl(context):
    sleep(5)
    logged_po = Logged(context.driver)
    logged_po.settings_link.click()


@then("the user name should be visible at the name input")
def step_impl(context):
    sleep(5)
    settings_po = Settings(context.driver)
    result = settings_po.username.get_attribute("value")
    expected = context.user["first_name"]
    expect(expected).to(equal(result))


@then("the user email should be visible at the email input")
def step_impl(context):
    sleep(5)
    settings_po = Settings(context.driver)
    result = settings_po.email.get_attribute("value")
    expected = context.user["email"]
    expect(expected).to(equal(result))


@when("click on Logout")
def step_impl(context):
    sleep(5)
    settings_po = Settings(context.driver)
    settings_po.logout.click()


@then("the sign up button should be visible.")
def step_impl(context):
    sleep(5)
    home_po = Home(context.driver)
    expected = True
    result = home_po.sign_up.is_displayed()
    expect(expected).to(equal(result))


@when('add "{bio_content}" on bio field')
def step_impl(context, bio_content):
    sleep(5)
    settings_po = Settings(context.driver)
    settings_po.bio.send_keys(bio_content)


@when("click in update settings")
def step_impl(context):
    sleep(5)
    settings_po = Settings(context.driver)
    settings_po.update_button.click()


@when("click on home")
def step_impl(context):
    sleep(5)
    settings_po = Settings(context.driver)
    settings_po.home.click()


@then('the bio value should be "{bio_content}"')
def step_impl(context, bio_content):
    sleep(5)
    settings_po = Settings(context.driver)
    expected = bio_content
    result = settings_po.bio.get_attribute("value")
    expect(expected).to(equal(result))
