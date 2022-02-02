Feature: The user is able to add a product to the bag

  @Regression
  Scenario: 'Add a product to the bag'
    Given the user selects a product
    When tapping add to my bag button
    Then the product is added to the bag