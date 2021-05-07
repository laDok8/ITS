Feature: Use Case

    Background: 
        Given logged in as admin

    Scenario: User adds Use Case without information
        Given on Add Use Case page
        When I specify Title
        And click "Save" button
        Then I should see Error message

    Scenario: User adds Use Case
        Given on Add Use Case page
        Given Evaluation Scenario exist
        Given Organization exist
        When I specify Title
        * Use Case Number
        * Use Case Domain
        * Use Case Description
        * Evaluation Scenario Requirement
        And click "Save" button 
        Then I should see Item created
        And I should see reference to Evaluation Scenario and its requirements and test cases in use case content
        And consumer shouldn't see newly created use case

    Scenario: Consumer Use Case visibility
        Given newly created use case exists
        When I change state of use case to published
        Then consumer should see given use case

    Scenario: add Use Case references
        Given at least two Evaluation Scenarios exists
        Given use case with one Evaluation Scenario exists
        When I add another Evaluation Scenarios into existing use case
        Then I should see references to both Evaluation Scenarios and its requirements and test cases in given use case content

    Scenario: Use Case reference edit
        Given use case with Evaluation Scenario exists
        When I edit Evaluation Scenario
        Then I should see updated informations in use case content page

    Scenario: Use Case deletion
        Given use case exists
        When I delete given use case
        Then I should no longer see given use case in Use cases menu

    Scenario: Use Case reference deletion
        Given use case with Evaluation Scenario exists
        When I delete given Evaluation Scenario
        Then I should no longer see deleted Evaluation Scenarios references from use case
