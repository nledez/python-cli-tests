Feature: Say hello
  In order to launch alice with command line

  Scenario: Say hello without parameters
    Given I have no parameter
    When I launch command line with hello command
    Then I see the string 'Hello Alice'

  Scenario: Say hello with a name
    Given I have '--name Bob'
    When I launch command line with hello command
    Then I see the string 'Hello Bob'
