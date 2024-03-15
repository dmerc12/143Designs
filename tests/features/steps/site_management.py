from behave import when

# Contact steps
## When step for entering first name input on contact page
@when(u'I enter {first_name} in the first name input on the contact page')
def step_impl(context, first_name):
    context.contact_poms.enter_first_name_input(first_name)

## When step for entering last name input on contact page
@when(u'I enter {last_name} in the last name input on the contact page')
def step_impl(context, last_name):
    context.contact_poms.enter_last_name_input(last_name)

## When step for entering email input on contact page
@when(u'I enter {email} in the email input on the contact page')
def step_impl(context, email):
    context.contact_poms.enter_email_input(email)

## When step for entering phone number input on contact page
@when(u'I enter {phone_number} in the phone_number input on the contact page')
def step_impl(context, phone_number):
    context.contact_poms.enter_phone_number_input(phone_number)

## When step for entering title input on contact page
@when(u'I enter {message_title} in the title input on the contact page')
def step_impl(context, message_title):
    context.contact_poms.enter_title_input(message_title)

## When step for entering message input on contact page
@when(u'I enter {message} in the message input on the contact page')
def step_impl(context, message):
    context.contact_poms.enter_message_input(message)

## When step for clicking submit button on contact page
@when(u'I click the submit button on the contact page')
def step_impl(context):
    context.contact_poms.click_submit_button()
