Feature: The user is able to search a product

  @Regression
  Scenario: 'User is able to search a product'
    Given the user is in Home screen
    When  entering a product in the search bar
    Then  the product is displayed