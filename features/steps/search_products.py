from behave import *
from selenium import webdriver
from class_amazon_page import ProductSearcher
from time import sleep
from class_amazon_page import ChooseProducts

@step('Go to {page_name} page')
def go_to_an_amazon_page(context, page_name):
    """
    This step opens a browser and navigates to the specified page name
    :param context:
    :param page_name: The name of the page I want to go
    :return: None
    """
    driver = webdriver.Chrome()
    #driver.add_arguments("--incognito")

    #driver = webdriver.Edge()
    driver.maximize_window()
    context.driver = driver
    if page_name == "Home":
        driver.get("https://www.amazon.com/")
    elif page_name == "Cart":
        driver.get("https://www.amazon.com/gp/cart/view.html?ref_=nav_cart")
    else:
        print("Sorry, this page doesn't work")
        assert False


@step('Amazon Search Bar - Type "{product_keyword}" in search bar')
def type_on_search_bar(context, product_keyword):
    module = ProductSearcher(context.driver)
    module.input_product_to_search(product_keyword)
    module.searcher_icon_click()


@step('Wait for {time_seconds} seconds')
def wait_for_seconds(context, time_seconds):
    sleep(int(time_seconds))


@step('Close browser')
def close_selenium_browser(context):
    context.driver.quit()


#ADD PRODUCTS TO CART
@step('Add products in the cart')
def add_car_icon_click(context):
    icon_car = ChooseProducts
    icon_car.add_products_click(context)



