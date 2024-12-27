Feature: Test for search

Scenario: User can search for a brush
    Given open target main page
    When  search for brush
    Then  verify results for brush are displayed
    Then verify search term brush in URL

  Scenario: User can search for chips
    Given open target main page
    When  search for chips
    Then  verify results for chips are displayed

  Scenario: User can search for gloves
    Given open target main page
    When  search for gloves
    Then  verify results for gloves are displayed

