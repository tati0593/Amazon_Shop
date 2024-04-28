
Feature: Amazon - Search Products Page

  Background:
    Given Go to Home page

  Scenario Outline: Amazon Search Page - I search products
    Then  Wait for <Wait Time> seconds
    Then  Wait for <Wait Time> seconds
    When  Amazon Search Bar - Type "<Product Name>" in search bar
    Then  Wait for <Wait Time> seconds
    And   Close browser

  Examples:
    | Product Name | Wait Time |
    | laptop       | 5         |
    #| camera       | 3         |
    #| play station | 7         |





