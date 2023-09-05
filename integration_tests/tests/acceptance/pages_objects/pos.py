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
    error = PageElement(xpath="/html/body/div/main/div/div/div/div/ul")

class Logged(PageObject):
    user_link = PageElement(xpath="/html/body/div/nav/div/ul/li[4]/a")
    new_post = PageElement(xpath="/html/body/div/nav/div/ul/li[2]/a")
    settings_link = PageElement(xpath="/html/body/div/nav/div/ul/li[3]/a")
    conduit = PageElement(xpath="/html/body/div/nav/div/a")
    home = PageElement(xpath="/html/body/div/nav/div/ul/li[1]/a")


class Settings(Logged):
    profile_foto_url = PageElement(xpath="/html/body/div/main/div/div/div/div/form[1]/fieldset/fieldset[1]/input")
    username = PageElement(xpath="/html/body/div/main/div/div/div/div/form[1]/fieldset/fieldset[2]/input")
    bio = PageElement(xpath="/html/body/div/main/div/div/div/div/form[1]/fieldset/fieldset[3]/textarea")
    email = PageElement(xpath="/html/body/div/main/div/div/div/div/form[1]/fieldset/fieldset[4]/input")
    password = PageElement(xpath="/html/body/div/main/div/div/div/div/form[1]/fieldset/fieldset[5]/input")
    update_button = PageElement(xpath="/html/body/div/main/div/div/div/div/form[1]/fieldset/button")
    logout = PageElement(xpath="/html/body/div/main/div/div/div/div/form[2]/button")


class CreateArticle(Logged):
    title = PageElement(xpath="/html/body/div/main/div/div/div/div/form/fieldset[1]/input")
    description = PageElement(xpath="/html/body/div/main/div/div/div/div/form/fieldset[2]/input")
    article = PageElement(xpath="/html/body/div/main/div/div/div/div/form/fieldset[3]/textarea")
    tags = PageElement(xpath="/html/body/div/main/div/div/div/div/form/fieldset[4]/input")
    publish = PageElement(xpath="/html/body/div/main/div/div/div/div/form/button")


class ArticleDetails(Logged):
    edit_button = PageElement(xpath="/html/body/div/main/div/div[1]/div/div/span/a")
    delete_button = PageElement(xpath="/html/body/div/main/div/div[1]/div/div/span/form/button")
    comment_area = PageElement(xpath="/html/body/div/main/div/div[2]/div[3]/div/div/form/div[1]/textarea")
    comment_submit = PageElement(xpath="/html/body/div/main/div/div[2]/div[3]/div/div/form/div[2]/button")
    delete_comment = PageElement(xpath="/html/body/div/main/div/div[2]/div[3]/div/div[2]/div[2]/form/button")