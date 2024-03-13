Feature: Customers need to be able to register with the site so that they can use it

  Scenario Outline: As a user I should be able to register with valid information
    Given I am on the home page
    When  I click the register button in the nav bar
    When  I enter <username> in the username input on the register page
    When  I enter <first_name> in the first name input on the register page
    When  I enter <last_name> in the last name input on the register page
    When  I enter <email> in the email input on the register page
    When  I enter <phone_number> in the phone number input on the register page
    When  I enter <password1> in the first password input on the register page
    When  I enter <password2> in the second password input on the register page
    When  I click the register button
    Then  I should be on a page with the title <title>

    Examples:
    |username|first_name|last_name|email           |phone_number|password1  |password2  |title |
    |'test'  |'test'    |'test'   |'test@email.com'|'1234567890'|'pass12345'|'pass12345'|'Home'|
