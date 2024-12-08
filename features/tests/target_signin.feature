Feature: Sign in on Target's website

  Scenario: Verify a logged-out user can navigate to Sign in
    Given Open target main page
    When Click on the Sign in button
    Then Click Sign in from right navigation
    Then Should see the Sign in button