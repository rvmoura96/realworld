Feature: User register

  Scenario: Adding a user
    Given a user data
      | first_name    | last_name | email                         |
      | Kleber12345     | Waters    | sokka.Kleber1245@mail.com |

    When the user access the platform
    And click on sign up
    And the user form is filled with user data
    Then the user name should be visible at the page
