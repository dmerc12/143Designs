from behave import given, then

# Given step to home page
@given(u'I am on the home page')
def step_impl(context):
    context.driver.get('http://127.0.0.1:8000/')

# Then step for comparing the current page title
@then(u'I should be on a page with the title {title}')
def step_impl(context, title):
    assert context.driver.title == title
