import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class LocationChart:

    def __init__(self,driver):
        self.driver = driver
        self.location_dismiss_button = "//input[@class='a-button-input'][1]"
        self.location_change_address_button = "//input[@class='a-button-input'][2]"

    def location_dismiss_button_click(self):
        location_dismiss_button = self.driver.find_element(By.XPATH, self.location_dismiss_button)
        location_dismiss_button.click()

    def location_change_address_click(self):
        location_change_address_button = self.driver.find_element(By.XPATH, self.location_change_address_button)
        location_change_address_button.click()


class AddPostalCodeLocation:

    def __init__(self,driver):
        self.driver = driver
        self.postal_code_input = "//input[@class='GLUX_Full_Width a-declarative']"
        self.postal_code_apply_button = "//span[@id='GLUXZipUpdate']//input"
        self.postal_code_continue = "//div[@class='a-popover-footer']//input[@id='GLUXConfirmClose']]"


    def postal_code_eu_input(self, postal_code):
        postal_code_input = self.driver.find_element(By.XPATH, self.postal_code_input)
        postal_code_input.send_keys(postal_code)

    def postal_code_apply_button_click(self):
        postal_code_apply_button = self.driver.find_element(By.XPATH, self.postal_code_apply_button)
        postal_code_apply_button.click()

    def postal_code_continue_button_click(self):
        postal_code_continue_button = self.driver.find_element(By.XPATH, self.country_location_button)
        postal_code_continue_button.click()


class CountryLocation:

    def __init__(self,driver):
        self.driver = driver
        self.country_location_button = "//div[@class=' a-declarative']//span[@class='a-button-text a-declarative']"

    def country_location_option_click(self):
        country_location_button = self.driver.find_element(By.XPATH, self.country_location_button)
        country_location_button.click()

    def choose_country_click(self,country_name):
        country_option = self.driver.find_element(By.XPATH, f"//input[contains(@value, '{country_name}')]")
        country_option.click()

    def postal_code_continue_button_click(self):
        postal_code_continue_button = self.driver.find_element(By.XPATH, self.country_location_button)
        postal_code_continue_button.click()





