Feature: Requirement

    Background: 
        Given logged in as admin

    Scenario: User adds requirement without information
        Given on Add Requirement page
        When I leave Title field empty
        And click "Save" button
        Then I should see Error message

    Scenario: User adds requirement
        Given at least one test case exists
        Given on Add Requirement page
        When I specify requirement Title
        * Requirement Test Case
        And click "Save" button
        Then I should see reference of test cases in requirements content
        And consumer shouldn't see newly created requirement

    Scenario: Consumer requirement visibility
        Given newly created requirement exists
        When I change state of requirement to published
        Then consumer should see given requirement

    Scenario: add requirement references
        Given at least two Test cases exists
        Given requirement with one test case exists
        When I add another test case into existing requirement
        Then I should see references to both test cases and its requirements and test cases in given requirement content

    Scenario: requirements reference edit
        Given requirement with test case exists
        When I edit given test case
        Then I should see updated informations in requirements content page

    Scenario: requirement deletion
        Given requirement exists
        When I delete requirement
        Then I should no longer see given requirement

    Scenario: requirements reference deletion
        Given requirement with new test case exists
        When I delete test case
        Then I should no longer see deleted test cases references in requirement
