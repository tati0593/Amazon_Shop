import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from class_amazon_page import LocationChart
from class_amazon_page import AddPostalCodeLocation
from class_amazon_page import CountryLocation
from class_amazon_page import ProductSearcher
from class_amazon_page import ChooseProducts

driver = webdriver.Chrome()

driver.get("https://www.amazon.com/")
driver.maximize_window()

element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@data-action-type='SELECT_LOCATION']")))


location_chart = LocationChart(driver)

#Dismiss location
location_chart.location_dismiss_button_click()
time.sleep(2)
'''
#Add EEUU postal code
location_chart.location_change_address_click()
time.sleep(5)
add_postal_code = AddPostalCodeLocation(driver)
add_postal_code.postal_code_eu_input("90091")
add_postal_code.postal_code_apply_button_click()
time.sleep(2)
add_postal_code.postal_code_continue_button_click()
'''
'''
#Add a country
location_chart.location_change_address_click()
time.sleep(5)
country_location = CountryLocation(driver)

country_location.country_location_option_click()
time.sleep(2)
country_location.choose_country_click("Dominica")
time.sleep(2)
country_location.done_button_click()
'''
searcher_box = ProductSearcher(driver)
searcher_box.input_product_to_search("woman shoes")
searcher_box.searcher_icon_click()

time.sleep(5)

choose_products = ChooseProducts(driver)
choose_products.add_products_cart(5)

time.sleep(5)

driver.get("https://www.amazon.com/gp/cart/view.html?ref_=nav_cart")
time.sleep(8)


driver.quit()