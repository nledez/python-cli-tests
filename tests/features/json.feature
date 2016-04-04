Feature: Get Json
  In order to get remote json with command line

  Scenario: Get json
    Given I have no parameter
    When I launch command line with json command
    Then I see the string '{"one": "two","key": "value"}'
