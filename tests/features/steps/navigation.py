from behave import when

# Navbar steps
## When step for clicking navbar dropdown toggle
@when(u'I click the navbar drop down')
def step_impl(context):
    context.navbar_poms.click_navbar_dropdown_toggle()

## When step for clicking register button in nav bar
@when(u'I click the register button in the nav bar')
def step_impl(context):
    context.navbar_poms.click_register()

## When step for clicking login button in nav bar
@when(u'I click the login button in the nav bar')
def step_impl(context):
    context.navbar_poms.click_login()

## When step for clicking update account in navbar dropdown
@when(u'I click update account in the navbar drop down')
def step_impl(context):
    context.navbar_poms.click_update_account()

## When step for clicking change password in navbar dropdown
@when(u'I click change password in the nav bar drop down')
def step_impl(context):
    context.navbar_poms.click_change_password()

## When step for clicking logout in navbar dropdown
@when(u'')
def step_impl(context):
    context.navbar_poms.click_logout()

## When step for clicking contact button
@when(u'I click the contact button in the nav bar')
def step_impl(context):
    context.navbar_poms.click_contact_button()

## When step for entering search criteria
@when(u'')
def step_impl(context, criteria):
    context.navbar_poms.enter_search_input(criteria)

## When step for clicking search button
@when(u'')
def step_impl(context):
    context.navbar_poms.click_search_button()

## When step for clicking side navbar toggle
@when(u'')
def step_impl(context):
    context.navbar_poms.click_side_navbar_toggle()

# Basic site navigation
## When step for clicking register link on login page
@when(u'')
def step_impl(context):
    context.login_poms.click_register_link()

## When step for clicking login link on register page
@when(u'')
def step_impl(context):
    context.register_poms.click_login_link()
