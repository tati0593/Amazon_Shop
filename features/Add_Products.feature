Feature: Amazon - Add Product To Cart

  Scenario Outline: Amazon Add Products - I add to the cart the products

    Given Amazon Search Bar - Type "<Product Name>" in search bar
    Then  Wait for <Wait Time> seconds
    When  Add products in the cart
    Then  Go to Cart page
    And   Close browser

  Examples:
    | Product Name | Wait Time |
    | laptop       | 5         |