Feature: User register

  Scenario: Adding a user
    Given a user data
    When the user access the platform
    And click on sign up
    And the user form is filled with user data and submit
    Then the user name should be visible at the page
