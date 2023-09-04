from page_objects import PageObject, PageElement


class Home(PageObject):
    home = PageElement(xpath="/html/body/div/nav/div/ul/li[1]/a")
    sign_in = PageElement(xpath="/html/body/div/nav/div/ul/li[2]/a")
    sign_up = PageElement(xpath="/html/body/div/nav/div/ul/li[3]/a")


class SignUp(Home):
    name = PageElement(xpath="/html/body/div/main/div/div/div/div/form/fieldset[1]/input")
    email = PageElement(xpath="/html/body/div/main/div/div/div/div/form/fieldset[2]/input")
    password = PageElement(xpath="/html/body/div/main/div/div/div/div/form/fieldset[3]/input")
    submit = PageElement(xpath="/html/body/div/main/div/div/div/div/form/button")

class Logged(PageObject):
    user_link = PageElement(xpath="/html/body/div/nav/div/ul/li[4]/a")