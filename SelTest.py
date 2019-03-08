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

wait = WebDriverWait(driver, 10)
add_values = ['S','M','L','XL']

# Fill in and submit login credentials
elem = driver.find_element_by_class_name("form-control")
elem.send_keys(login)
elem = driver.find_element_by_id("password")
elem.send_keys(password)
elem.send_keys(Keys.RETURN)

# Waits for page to load
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "More information")))

# Click into Showroom link
driver.find_element_by_xpath("//ul[@id='side-menu']/li[3]/a").click()
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "More information")))
driver.find_element_by_xpath("//a[contains(text(), 'Showrooms')]").click()

# Waits for page to load
wait.until(EC.frame_to_be_available_and_switch_to_it('ContentFrame'))

# Go to products list
products = driver.find_elements_by_name("Products")[1]
products.click()

# Waits for page to load
driver.implicitly_wait(5)

# Grabbing number of products in showroom
products = driver.find_elements_by_xpath('//tbody/tr')
products_length = len(products)

# Loops through list of products
for i in range(products_length):
    # Click to edit product
    driver.implicitly_wait(5)
    driver.find_elements_by_name('Edit')[i].click()
    driver.implicitly_wait(5)

    # Adds name to custom options
    driver.find_element(By.XPATH, '//a[text()="Item Options"]').click()
    driver.implicitly_wait(1)
    name_field = driver.find_element_by_name('CustomFld1Name')
    value_field = driver.find_element_by_name('CF1NameAdd')
    name_field.send_keys('Size')

    # Loops to add values for drop downs
    for value in add_values:
        value_field.send_keys(value)
        driver.find_element(By.XPATH, '//input[@value="Add"]').click()

    # Saves
    value_field.send_keys(Keys.RETURN)
