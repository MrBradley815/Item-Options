from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Get login credentials
login = input("Your Account Number: ")
clientAccount = input("Client's Account Number (Press Enter to skip): ")
if clientAccount:
    login = login + ':' + clientAccount
password = input("Password: ")

# Go to sagemember.com
driver = webdriver.Firefox()
driver.get("https://www.sagemember.com/")
assert "SAGEmember.com" in driver.title

# Fill in and submit login credentials
elem = driver.find_element_by_class_name("form-control")
elem.send_keys(login)
elem = driver.find_element_by_id("password")
elem.send_keys(password)
elem.send_keys(Keys.RETURN)

# Waits for page to load
WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.LINK_TEXT, "More information")))

# Click into Showroom link
driver.find_element_by_xpath("//ul[@id='side-menu']/li[3]/a").click()
WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.LINK_TEXT, "More information")))
driver.find_element_by_xpath("//a[contains(text(), 'Showrooms')]").click()


