Feature: Users need to be able to login to access the site

  Scenario Outline: As a user I should not be able to login with invalid credentials
    Given I am on the home page
    When  I click the login button in the nav bar
    When  I enter <username> in the username input on the login page
    When  I enter <password> in the password input on the login page
    When  I click the login button
    Then  I should be on a page with the title <title>

    Examples:
    |username  |password      |title  |
    |'incorrect'|'credentials'|'Login'|
    |''|''|'Login'|

  Scenario Outline: As a user I should be able to login with valid credentials
    Given I am on the home page
    When  I click the login button in the nav bar
    When  I enter <username> in the username input on the login page
    When  I enter <password> in the password input on the login page
    When  I click the login button
    Then  I should be on a page with the title <title>

    Examples:
    |username  |password   |title |
    |'testuser'|'pass12345'|'Home'|

  Scenario Outline: As an admin I should be able to login with valid credentials
    Given I am on the home page
    When  I click the login button in the nav bar
    When  I enter <username> in the username input on the login page
    When  I enter <password> in the password input on the login page
    When  I click the login button
    Then  I should be on a page with the title <title>

    Examples:
    |username   |password   |title       |
    |'testadmin'|'pass12345'|'Admin Home'|
