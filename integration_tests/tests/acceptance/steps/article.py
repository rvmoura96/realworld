from time import sleep

from behave import given, then, when
from expects import equal, expect

from modules.auxiliar import cast_table_to_dict
from pages_objects.pos import ArticleDetails, CreateArticle, Home, Logged, Settings, SignUp


@given(u'an article data')
def step_impl(context):
    context.article = cast_table_to_dict(context.table)


@when(u'the user click on new post')
def step_impl(context):
    sleep(5)
    ca_po = CreateArticle(context.driver)
    ca_po.new_post.click()

@when(u'fill article fields with the given data and submit')
def step_impl(context):
    sleep(2)
    ca_po = CreateArticle(context.driver)
    ca_po.title.send_keys(context.article["title"])
    ca_po.description.send_keys(context.article["description"])
    ca_po.article.send_keys(context.article["article"])
    ca_po.tags.send_keys(context.article["tags"])
    ca_po.publish.click()


@then(u'the current url should contains "{slugged_title}"')
def step_impl(context, slugged_title):
    sleep(2)
    ca_po = CreateArticle(context.driver)
    result = slugged_title in ca_po.w.current_url
    expected = True

    expect(expected).to(equal(result))


@then(u'the current url should not contains "{slugged_title}"')
def step_impl(context, slugged_title):
    sleep(5)
    ca_po = CreateArticle(context.driver)
    result = slugged_title not in ca_po.w.current_url
    expected = True

    expect(expected).to(equal(result))

@when(u'click on edit')
def step_impl(context):
    sleep(5)
    ad_po = ArticleDetails(context.driver)
    ad_po.edit_button.click()


@when(u'update the title to "{new_article_title}" and submit')
def step_impl(context, new_article_title):
    sleep(5)
    ca_po = CreateArticle(context.driver)
    ca_po.title.clear()
    ca_po.title.send_keys(new_article_title)
    ca_po.publish.click()


@when(u'click on delete')
def step_impl(context):
    sleep(5)
    ad_po = ArticleDetails(context.driver)
    ad_po.delete_button.click()


@when(u'comment "{comment_content}" and submit')
def step_impl(context, comment_content):
    sleep(5)
    ad_po = ArticleDetails(context.driver)
    ad_po.comment_area.send_keys(comment_content)
    ad_po.comment_submit.click()


@then(u'the delete comment button should be visible')
def step_impl(context):
    sleep(5)
    ad_po = ArticleDetails(context.driver)
    result = ad_po.delete_comment.is_displayed()
    expected = True
    expect(expected).to(equal(result))


@when(u'click on delete comment')
def step_impl(context):
    sleep(5)
    ad_po = ArticleDetails(context.driver)
    ad_po.delete_comment.click()


@then(u'the delete comment button should not be visible')
def step_impl(context):
    sleep(5)
    ad_po = ArticleDetails(context.driver)
    result = bool(ad_po.delete_comment)
    expected = False
    expect(expected).to(equal(result))
