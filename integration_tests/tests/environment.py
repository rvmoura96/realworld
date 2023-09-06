"""Hooks file."""
from behave.tag_matcher import ActiveTagMatcher
from faker import Faker
from ipdb import post_mortem


from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


active_tag_value_provider = {"config_0": False}

active_tag_matcher = ActiveTagMatcher(active_tag_value_provider)


def before_all(context):
    context.userdata = context.config.userdata
    context.config_0 = context.userdata.get("config_0", "False")
    context.server_url = context.userdata.get(
        "server_url", "https://realworld.svelte.dev/"
    )
    context.debug = context.userdata.get("debug", "False")


def before_feature(context, feature):
    ...


def before_scenario(context, scenario):
    context.faker = Faker()

    browser_name = context.userdata.get("browser", "chrome")
    local_machine_ip = context.userdata.get('local_machine_ip', '192.168.15.19')
    selenium_port =  context.userdata.get('selenium_hub_port', '4444')
    command_executor = f"{local_machine_ip}:{selenium_port}/wd/hub"
    context.options = {"addr": local_machine_ip}

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
    else:
        options = webdriver.FirefoxOptions()

    context.driver = webdriver.Remote(
        command_executor=command_executor,
        options=options,
    )
    


def before_tag(context, tag):
    pass


def after_step(context, step):
    if context.debug and step.status == "failed":
        post_mortem(step.exc_traceback)


def after_tag(context, tag):
    ...


def after_scenario(context, scenario):
    context.driver.quit()


def after_feature(context, feature):
    ...


def after_all(context):
    ...
