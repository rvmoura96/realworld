Feature: Articles
  Background: User registered
    Given a user data
    When the user access the platform
    And click on sign up
    And the user form is filled with user data and submit

  Scenario: Create an article
    Given an article data
      | title                          | description                 | article                | tags       |
      | An awesome title to my article | This is one awesome article | One incredible article | incredible |
    When the user click on new post
    And fill article fields with the given data and submit
    Then the current url should contains "An-awesome-title-to-my-article"

  Scenario: Update an article
    Given an article data
      | title                          | description                 | article                | tags       |
      | An awesome title to my article | This is one awesome article | One incredible article | incredible |
    When the user click on new post
    And fill article fields with the given data and submit
    And click on edit
    And update the title to "Another gorgeous article" and submit
    Then the current url should contains "Another-gorgeous-article"

  Scenario: Delete an article
    Given an article data
      | title                          | description                 | article                | tags       |
      | An awesome title to my article | This is one awesome article | One incredible article | incredible |
    When the user click on new post
    And fill article fields with the given data and submit
    And click on delete
    Then the current url should not contains "An-awesome-title-to-my-article"

  Scenario: Comment an article
    Given an article data
      | title                          | description                 | article                | tags       |
      | An awesome title to my article | This is one awesome article | One incredible article | incredible |
    When the user click on new post
    And fill article fields with the given data and submit
    And comment "Awesome article" and submit
    Then the delete comment button should be visible

  Scenario: Delete an article comment
    Given an article data
      | title                          | description                 | article                | tags       |
      | An awesome title to my article | This is one awesome article | One incredible article | incredible |
    When the user click on new post
    And fill article fields with the given data and submit
    And comment "Awesome article" and submit
    And click on delete comment
    Then the delete comment button should not be visible