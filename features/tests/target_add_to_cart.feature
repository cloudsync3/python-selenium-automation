Feature: Add product to Target cart

  Scenario: Add product to cart and verify it
    Given Open target main page
    When search for laptop
    And Click on add to cart button
    And Confirm add to cart button side navigation
    Then Product should be added to the cart
