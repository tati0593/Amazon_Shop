import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

driver.get("https://www.amazon.com/")
driver.maximize_window()
time.sleep(2)


location_button = driver.find_element(By.XPATH, "//input[@class='a-button-input'][1]")
location_button.click()

time.sleep(5)

driver.quit()