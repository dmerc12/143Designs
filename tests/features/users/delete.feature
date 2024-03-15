Feature: Customers need to be able to delete their account so they can leave the site entirely

  Scenario Outline: As a user I should be able to update my information with valid information
    Given I am on the home page
    When  I click the nav bar drop down
    When  I click the login button in the nav bar
    When  I enter <username> in the username input on the login page
    When  I enter <password> in the password input on the login page
    When  I click the login button
    When  I click the nav bar drop down
    When  I click update account in the nav bar drop down
    When  I click the delete user link
    When  I click the delete user button
    Then  I should be on a page with the title <title>

    Examples:
    |username  |password   |title |
    |'testuser'|'pass12345'|'Home'|
