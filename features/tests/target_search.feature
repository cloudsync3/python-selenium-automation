Feature: Test for search

Scenario: User can search for a brush
    Given open target main page
    When  search for brush
    Then  search results for brush are displayed

  Scenario: User can search for chips
    Given open target main page
    When  search for chips
    Then  search results for chips are displayed

  Scenario: User can search for gloves
    Given open target main page
    When  search for gloves
    Then  search results for gloves are displayed

