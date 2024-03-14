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

# Login steps
## When step for entering username input on login page
@when(u'I enter {username} in the username input on the login page')
def step_impl(context, username):
    context.login_poms.enter_username_input(username)

## When step for entering password input on login page
@when(u'I enter {password} in the password input on the login page')
def step_impl(context, password):
    context.login_poms.enter_password_input(password)

## When step for clicking login button on login page
@when(u'I click the login button')
def step_impl(context):
    context.login_poms.click_login_button()

# Update user steps
## When step for entering username input on update user page
@when(u'I enter {new_username} in the username input on the update user page')
def step_impl(context, new_username):
    context.update_user_poms.enter_username_input(new_username)

## When step for entering first name input on update user page
@when(u'I enter {first_name} in the first name input on the update user page')
def step_impl(context, first_name):
    context.update_user_poms.enter_first_name_input(first_name)

## When step for entering last name input on update user page
@when(u'I enter {last_name} in the last name input on the update user page')
def step_impl(context, last_name):
    context.update_user_poms.enter_last_name_input(last_name)

## When step for entering email input on update user page
@when(u'I enter {email} in the email input on the update user page')
def step_impl(context, email):
    context.update_user_poms.enter_email_input(email)

## When step for entering phone number input on update user page
@when(u'I enter {phone_number} in the phone number inpupt on the update user page')
def step_impl(context, phone_number):
    context.update_user_poms.enter_phone_number_input(phone_number)

## When step for clicking update user page
@when(u'I click the update user button')
def step_impl(context):
    context.update_user_poms.click_update_user_button()

# Change password steps
## When step for entering first password input on change password page
@when(u'I enter <new_password1> in the first password input on the change password page')
def step_impl(context, new_password1):
    context.change_password_poms.enter_password1_input(new_password1)

### When step for entering second password input on change password page
@when(u'I enter <new_password2> in the second password input on the change password page')
def step_impl(context, new_password2):
    context.change_password_poms.enter_password2_input(new_password2)

### When step for clicking change password button on change password page
@when(u'I click the change password button')
def step_impl(context):
    context.change_password_poms.click_change_password_button()

# Delete user steps
## When step for clicking delete user link on update user page
@when(u'I click the delete user link')
def step_impl(context):
    context.update_user_poms.click_delete_user_link()

## When step for clicking delete user button on delete user page
@when(u'I click the delete user button')
def step_impl(context):
    context.delete_user_poms.click_delete_user_button()
