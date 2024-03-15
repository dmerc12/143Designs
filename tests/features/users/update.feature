Feature: Users need to be able to update their information so it is the most up to date

    Scenario Outline: As a user I should not be able to update my information with invalid information
      Given I am on the home page
      When  I click the nav bar drop down
      When  I click the login button in the nav bar
      When  I enter <username> in the username input on the login page
      When  I enter <password> in the password input on the login page
      When  I click the login button
      When  I click the navbar drop down
      When  I click update account in the navbar drop down
      When  I enter <new_username> in the username input on the update user page
      When  I enter <first_name> in the first name input on the update user page
      When  I enter <last_name> in the last name input on the update user page
      When  I enter <email> in the email input on the update user page
      When  I enter <phone_number> in the phone number inpupt on the update user page
      When  I click the update user button
      Then  I should be on a page with the title <title>

    Examples:
    |username  |password   |new_username  |first_name    |last_name     |email                   |phone_number      |title           |
    |'testuser'|'pass12345'|''            |''            |''            |''                      |''                |'Update Account'|
    |'testuser'|'pass12345'|'updated' * 40|'updated' * 40|'updated' * 40|'updated@email.com' * 40|'11111111111' * 30|'Update Account'|
    |'testuser'|'pass12345'|'updated'     |'updated'     |'updated'     |'incorrect format'      |'11111111111'     |'Update Account'|

  Scenario Outline: As a user I should be able to update my information with valid information
    Given I am on the home page
    When  I click the nav bar drop down
    When  I click the login button in the nav bar
    When  I enter <username> in the username input on the login page
    When  I enter <password> in the password input on the login page
    When  I click the login button
    When  I click the nav bar drop down
    When  I click update account in the nav bar drop down
    When  I enter <new_username> in the username input on the update user page
    When  I enter <first_name> in the first name input on the update user page
    When  I enter <last_name> in the last name input on the update user page
    When  I enter <email> in the email input on the update user page
    When  I enter <phone_number> in the phone number inpupt on the update user page
    When  I click the update user button
    Then  I should be on a page with the title <title>

    Examples:
    |username  |password   |new_username|first_name|last_name|email              |phone_number |title |
    |'testuser'|'pass12345'|'updated'   |'updated' |'updated'|'updated@email.com'|'11111111111'|'Home'|
