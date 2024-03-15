Feature: Users need to be able to submit messages so they can contact the site admins for unique projects

  Scenario Outline: As a user I should not be able to submit a message with invalid information
    Given I am on the home page
    When  I click the contact button in the nav bar
    When  I enter <first_name> in the first name input on the contact page
    When  I enter <last_name> in the last name input on the contact page
    When  I enter <email> in the email input on the contact page
    When  I enter <phone_number> in the phone_number input on the contact page
    When  I enter <message_title> in the title input on the contact page
    When  I enter <message> in the message input on the contact page
    When  I click the submit button on the contact page
    Then  I should be on a page with the title <title>

    Examples:
    |first_name  |last_name  |email               |phone_number     |message_title|message        |title    |
    |''          |''         |''                  |''               |''           |''             |'Contact'|
    |'test' * 100|'user' * 50|'test@user.com' * 50|'11231231234' * 2|'title' * 150|'message' * 600|'Contact'|

  Scenario Outline: As a user I should be able to submit a message with valid information
    Given I am on the home page
    When  I click the contact button in the nav bar
    When  I enter <first_name> in the first name input on the contact page
    When  I enter <last_name> in the last name input on the contact page
    When  I enter <email> in the email input on the contact page
    When  I enter <phone_number> in the phone_number input on the contact page
    When  I enter <title> in the title input on the contact page
    When  I enter <message> in the message input on the contact page
    When  I click the submit button on the contact page
    Then  I should be on a page with the title <title>

    Examples:
    |first_name |last_name|email          |phone_number |title  |message  |title |
    |'test'     |'user'   |'test@user.com'|'11231231234'|'title'|'message'|'Home'|
