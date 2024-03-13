from behave import when

# Register steps
## When step for entering username input on register page
@when(u'I enter {username} in the username input on the register page')
def step_impl(context, username):
    context.register_poms.enter_username_input(username)

## When step for entering first name input on register page
@when(u'I enter {first_name} in the first name input on the register page')
def step_impl(context, first_name):
    context.register_poms.enter_first_name_input(first_name)

## When step for entering last name input on register page
@when(u'I enter {last_name} in the last name input on the register page')
def step_impl(context, last_name):
    context.register_poms.enter_last_name_input(last_name)

## When step for entering email input on register page
@when(u'I enter {email} in the email input on the register page')
def step_impl(context, email):
    context.register_poms.enter_email_input(email)

## When step for entering phone number input on register page
@when(u'I enter {phone_number} in the phone number input on the register page')
def step_impl(context, phone_number):
    context.register_poms.enter_phone_number_input(phone_number)

## When step for entering password 1 input on register page
@when(u'I enter {password1} in the first password input on the register page')
def step_impl(context, password1):
    context.register_poms.enter_password1_input(password1)

## When step for entering password 2 input on register page
@when(u'I enter {password2} in the second password input on the register page')
def step_impl(context, password2):
    context.register_poms.enter_password2_input(password2)

## When step for clicking register button on register page
@when(u'I click the register button')
def step_impl(context):
    context.register_poms.click_register_button()
