# Created by 15712 at 7/17/2023
Feature:Search results are displayed

  Scenario: When cure is entered in textbox 19 products are displayed
    Given Cureskin Search page is open
    When cure is entered in textbox
    When search is clicked
    Then User gets 19
