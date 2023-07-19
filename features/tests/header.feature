# Created by 15712 at 7/13/2023
Feature: Open CureSkin Main Page

  Scenario: All header links are clickable
    Given Open CureSkin url
    When locate home tab
    When locate shop tab
    When locate CureSkin app tab
    When locate About Us tab
    When locate our expertise tab
    When locate our Testimonials tab
    When locate Skin&Hair tab
    When locate FAQ
    When locate Contact us tab

    #When About us page is open

    # Enter steps here