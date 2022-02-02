Feature: User is able to remove a product from the bag

  @Test
  Scenario: 'Remove product from Bag'
    Given the user added a product to the bag
    When tapping the delete button
    Then the product is removed successfully