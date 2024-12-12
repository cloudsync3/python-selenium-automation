Feature: Add product to Target cart

  Scenario: Add product to cart and verify it
    Given Open target main page
    When search for laptop
    And Add product to the cart
    Then Product should be added to the cart
