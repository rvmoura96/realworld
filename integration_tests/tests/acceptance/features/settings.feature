Feature: User Settings
  Background: User registered
    Given a user data
    When the user access the platform
    And click on sign up
    And the user form is filled with user data and submit

  Scenario: Access user's settings checking Data
    When the user click on settings
    Then the user name should be visible at the name input
    And the user email should be visible at the email input

  Scenario: Logout through the settings
    When the user click on settings
    And click on Logout
    Then the sign up button should be visible.

  Scenario: Update bio
    When the user click on settings
    And add "This is my awesome Bio" on bio field
    And click in update settings
    And click on home
    And the user click on settings
    Then the bio value should be "This is my awesome Bio"