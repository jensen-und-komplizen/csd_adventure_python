Feature: Loo
  The adventure starts on the loo. From here I want to find my way out.

  Scenario: Waking up on the loo
    When I start the game
    Then I see "You wake up on the loo"

  Scenario: Help on the loo
    Given I am on the loo
    When I ask for help
    Then I see "look around"
    And I see "look at magazines"
    And I see "use door to washroom"

  Scenario: Look around on the loo
    Given I am on the loo
    When I look around
    Then I see hints for interactable objects

  Scenario: Look at the magazines
    Given I am on the loo
    When I say "look at magazines"
    Then I see "scrum guide 2009"

  Scenario: Leave the loo to the washroom
    Given I am on the loo
    When I say "use door to washroom"
    Then I see "looks like a washroom"
