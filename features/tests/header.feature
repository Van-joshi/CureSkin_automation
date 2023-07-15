# Created by 15712 at 7/13/2023
Feature: Open CureSkin Main Page

  Scenario: Clicking on shop will display all products
    Given Open CureSkin url
    When Click on shop
    Then All products are displayed
    # Enter steps here