import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

class LocationChart:

    def __init__(self,driver):
        self.driver = driver
        self.location_dismiss_button_xpath = "//input[@class='a-button-input'][1]"
        self.location_change_address_button_xpath = "//input[@data-action-type='SELECT_LOCATION']"

    def location_dismiss_button_click(self):
        location_dismiss_button = self.driver.find_element(By.XPATH, self.location_dismiss_button_xpath)
        location_dismiss_button.click()

    def location_change_address_click(self):
        location_change_address_button = self.driver.find_element(By.XPATH, self.location_change_address_button_xpath)
        location_change_address_button.click()


class AddPostalCodeLocation:

    def __init__(self,driver):
        self.driver = driver
        self.postal_code_input_xpath = "//input[@class='GLUX_Full_Width a-declarative']"
        self.postal_code_apply_button_xpath = "//span[@id='GLUXZipUpdate']//input"
        self.postal_code_continue_xpath = "//div[@class='a-popover-footer']//input[@id='GLUXConfirmClose']"

    def postal_code_eu_input(self, postal_code):
        postal_code_input = self.driver.find_element(By.XPATH, self.postal_code_input_xpath)
        postal_code_input.send_keys(postal_code)

    def postal_code_apply_button_click(self):
        postal_code_apply_button = self.driver.find_element(By.XPATH, self.postal_code_apply_button_xpath)
        postal_code_apply_button.click()

    def postal_code_continue_button_click(self):
        postal_code_continue_button = self.driver.find_element(By.XPATH, self.postal_code_continue_xpath)
        postal_code_continue_button.click()


class CountryLocation:

    def __init__(self,driver):
        self.driver = driver
        self.country_location_button_xpath = "//div[@class=' a-declarative']//span[@class='a-button-text a-declarative']"
        self.done_button_xpath = "//div[@class='a-popover-footer']//input[@id='GLUXConfirmClose']]"

    def country_location_option_click(self):
        country_location_button = self.driver.find_element(By.XPATH, self.country_location_button_xpath)
        country_location_button.click()

    def choose_country_click(self,country_name):
        #self.driver.execute_script("window.scrollTo(0, 300)")
        country_option = self.driver.find_element(By.XPATH, f"//option[contains(@value, '{country_name}')]")
        time.sleep(2)
        country_option.click()

    def done_button_click(self):
        done_button = self.driver.find_element(By.XPATH, self.done_button_xpath)
        done_button.click()


class ProductSearcher:

    def __init__(self,driver):
        self.driver = driver
        self.searcher_box_xpath = "//div//input[@id='twotabsearchtextbox']"
        self.searcher_icon_xpath = "//div//input[@id='nav-search-submit-button']"

    def input_product_to_search(self, name_product):
        searcher_box = self.driver.find_element(By.XPATH, self.searcher_box_xpath)
        searcher_box.send_keys(name_product)

    def searcher_icon_click(self):
        searcher_icon = self.driver.find_element(By.XPATH, self.searcher_icon_xpath)
        searcher_icon.click()


class ChooseProducts:

    def __init__(self,driver):
        self.driver = driver
        self.products_xpath = "//a[@class='a-link-normal s-no-outline']"
        self.chart_icon_xpath = "//input[@id='add-to-cart-button']"

    def add_products_cart(self, number):
        list_products = self.driver.find_elements(By.XPATH, self.products_xpath)[0:number]
        print(len(list_products))
        for products in list_products:
            products.send_keys(Keys.CONTROL + Keys.ENTER)
            time.sleep(5)
            each_product_cart = self.driver.find_element(By.XPATH, self.chart_icon_xpath )
            each_product_cart.click()

    def add_products_click(self):
        add_cart = self.driver.find_element(By.XPATH, self.chart_icon_xpath )
        add_cart.click()







