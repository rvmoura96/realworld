from time import sleep

from behave import given, then, when
from expects import equal, expect

from modules.auxiliar import cast_table_to_dict
from pages_objects.pos import Home, Logged, SignUp


@given("an user data")
def step_impl(context):
    context.user = {
        "first_name": f"{context.faker.name()}{context.faker.name()}",
        "email": context.faker.email(),
        "password": context.faker.password()
    }

@when("the user access the platform")
def step_impl(context):
    context.driver.get(context.server_url)


@when("click on sign up")
def step_impl(context):
    sleep(2)
    home_po = Home(context.driver)
    home_po.sign_up.click()


@when("the user form is filled with user data and submit")
def step_impl(context):
    sleep(2)
    sign_up_po = SignUp(context.driver)
    sign_up_po.name.send_keys(context.user["first_name"])
    sign_up_po.email.send_keys(context.user["email"])
    sign_up_po.password.send_keys(context.user["password"])
    sign_up_po.submit.click()


@then("the user name should be visible at the page")
def step_impl(context):
    logged_page = Logged(context.driver)
    expected = True
    sleep(5)

    result = logged_page.user_link.is_displayed()
    expect(expected).to(equal(result))

@then(u'an error message should be showed')
def step_impl(context):
    sleep(5)
    sign_up_po = SignUp(context.driver)
    result = sign_up_po.error.is_displayed()
    expected = True
    expect(expected).to(equal(result))
