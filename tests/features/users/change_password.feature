Feature: Users need to be able to change their password so their account doesn't become compromised

    Scenario Outline: As a user I should not be able to change my password with when not meeting password requirements
      Given I am on the home page
      When  I click the nav bar drop down
      When  I click the login button in the nav bar
      When  I enter <username> in the username input on the login page
      When  I enter <password> in the password input on the login page
      When  I click the login button
      When  I click the nav bar drop down
      When  I click change password in the nav bar drop down
      When  I enter <new_password1> in the first password input on the change password page
      When  I enter <new_password2> in the second password input on the change password page
      When  I click the change password button
      Then  I should be on a page with the title <title>

    Examples:
    |username  |password   |new_password1|new_password2|title            |
    |'testuser'|'pass12345'|'testuser'   |'testuser'   |'Change Password'|
    |'testuser'|'pass12345'|'new12345'   |'new12345'   |'Change Password'|

  Scenario Outline: As a user I should be able to change my password with when meeting password requirements
    Given I am on the home page
    When  I click the nav bar drop down
    When  I click the login button in the nav bar
    When  I enter <username> in the username input on the login page
    When  I enter <password> in the password input on the login page
    When  I click the login button
    When  I click the nav bar drop down
    When  I click change password in the nav bar drop down
    When  I enter <new_password1> in the first password input on the change password page
    When  I enter <new_password2> in the second password input on the change password page
    When  I click the change password button
    Then  I should be on a page with the title <title>

    Examples:
    |username  |password   |new_password1|new_password2|title |
    |'testuser'|'pass12345'|'new12345'   |'new12345'   |'Home'|
