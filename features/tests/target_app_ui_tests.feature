Feature: Tests for Target App page


  Scenario: User is able to open Terms and Conditions
    Given Open Target sign in page
    And Store original window
    When Click on Target terms and conditions link
    And Switch to the new window
    Then Verify Terms and Conditions page opened
    And User can close new window
    And switch window to original



