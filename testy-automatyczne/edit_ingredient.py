from selenium import webdriver
from login_func import logging
import time
import os

driver = webdriver.Chrome(os.getcwd()+'\drivers\chromedriver.exe')

logging("user@user.com", "password", driver)

driver.get("http://vol4-capybara.herokuapp.com/ingredients")
assert "My ingredients" in driver.page_source

# get current values(name, exp date, quantity, unit) of first ingredient in the table
ingredients = driver.find_elements_by_xpath("/html/body/div[2]/div/div[2]/form/table/tbody/tr/td/a")
current_ingredient = ingredients[0].get_attribute("innerText")
exp_dates = driver.find_elements_by_xpath("/html/body/div[2]/div/div[2]/form/table/tbody/tr/td[2]")
current_exp = exp_dates[0].get_attribute("innerText")
quantities = driver.find_elements_by_xpath("/html/body/div[2]/div/div[2]/form/table/tbody/tr/td[3]")
current_quantities = quantities[0].get_attribute("innerText")
units = driver.find_elements_by_xpath("/html/body/div[2]/div/div[2]/form/table/tbody/tr/td[4]")
current_units = units[0].get_attribute("innerText")

# go to ingredient details page
ingredients[0].click()
time.sleep(2)

# go to edit page
driver.find_element_by_xpath("/html/body/div[2]/div/a[2]").click()
time.sleep(2)

# find and assign current values of inputs to variables
product = driver.find_element_by_xpath("//*[@id='ingredient_product_id']/option")
product_value = product.get_attribute("innerText")

quantity = driver.find_element_by_xpath("//*[@id='ingredient_quantity']")
quantity_value = quantity.get_attribute('value')

unit = driver.find_element_by_xpath("//*[@id='ingredient_unit']/option")
unit_value = unit.get_attribute("innerText")

expiration = driver.find_element_by_xpath("//*[@id='ingredient_exp_date']")
expiration_value = expiration.get_attribute("value")

# change values of inputs to new ones and assign new values to variables
new_product = driver.find_element_by_xpath("//*[@id='ingredient_product_id']/option[text()='apple']")
new_product.click()
new_product_value = new_product.get_attribute("innerText")

new_quantity = driver.find_element_by_xpath("//*[@id='ingredient_quantity']")
new_quantity.send_keys(3)
new_quantity_value = quantity.get_attribute('value')

new_unit = driver.find_element_by_xpath("//*[@id='ingredient_unit']/option[text()='Litre']")
new_unit.click()
new_unit_value = new_unit.get_attribute("innerText")

new_expiration = driver.find_element_by_xpath("//*[@id='ingredient_exp_date']")
new_expiration.send_keys('02022019')
new_expiration_value = expiration.get_attribute("value")

driver.find_element_by_xpath("/html/body/div[2]/div/form/input[6]").click()
time.sleep(2)
driver.save_screenshot("screenshots/ingredients/edited_ingredient" + current_ingredient.upper() + ".png")

assert current_ingredient != new_product_value
assert current_exp != new_expiration_value
assert current_quantities != new_quantity_value
assert current_units != new_unit_value
print("Ingredient " + current_ingredient + " has been updated.")
print(current_ingredient + " changed to " + new_product_value)
print("Expiration date " + current_exp + " changed to " + new_expiration_value)
print("Quantity " + current_quantities + " changed to " + new_quantity_value)
print("Unit " + current_units + " changed to " + new_unit_value)


driver.quit()
