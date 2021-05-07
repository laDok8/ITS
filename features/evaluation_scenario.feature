Feature: Evaluation Scenario

    Background: 
        Given logged in as admin

    Scenario: add Evaluation Scenario
        Given at least one requirement exists
        Given on Add Evaluation Scenario page
        When I specify Title
        * Use Case Id
        * Use Case Evaluation Scenario Textual Description
        * Use Case Evaluation Scenario Requirements List
        And click "Save" button 
        Then I should see Item created
        And I should see reference of requirement in requirements content
        And consumer shouldn't see newly created Evaluation Scenario

    Scenario: Consumer Evaluation Scenario visibility
        Given newly created Evaluation Scenario exists
        When I change state of Evaluation Scenario to published
        Then consumer should see given Evaluation Scenario

    Scenario: add Consumer Evaluation Scenario references
        Given at least two requirements exists
        Given Evaluation Scenario with one requirement exists
        When I add another requirement into existing Evaluation Scenario
        Then I should see references to both requirements in given Evaluation Scenario content

    Scenario: Evaluation Scenario reference edit
        Given Evaluation Scenario with requirement exists
        When I edit given requirement
        Then I should see updated informations in Evaluation Scenario content page

    Scenario: Evaluation Scenario deletion
        Given Evaluation Scenario exists
        When I delete given Evaluation Scenario
        Then I should no longer see it

    Scenario: Evaluation Scenario reference deletion
        Given Evaluation Scenario with a requirement exists
        When I delete given requirement
        Then I should no longer see deleted requirements references in Evaluation Scenario