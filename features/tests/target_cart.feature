Feature: Cart functionality on Target's website

  Scenario: User can verify "Your cart is empty" message
    Given Open target main page
    When Click on the Cart icon
    Then Verify cart is empty message