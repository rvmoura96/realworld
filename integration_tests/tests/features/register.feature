Feature: User register

  Scenario: Adding an user
    Given an user data
    When the user access the platform
    And click on sign up
    And the user form is filled with user data and submit
    Then the user name should be visible at the page
  
  Scenario: Adding an user already registred
    Given an user data
    When the user access the platform
    And click on sign up
    And the user form is filled with user data and submit
    And the user click on settings
    And click on Logout
    And click on sign up
    And the user form is filled with user data and submit
    Then an error message should be showed