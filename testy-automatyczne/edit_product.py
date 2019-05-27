from selenium import webdriver
from login_func import logging
import time
import os

driver = webdriver.Chrome(os.getcwd()+'\drivers\chromedriver.exe')

logging("admin@admin.com", "password", driver)

driver.get("http://vol4-capybara.herokuapp.com/products")
assert "List of Products" in driver.page_source

# find first ingredient on the list, get its' name and go to detail page
ingredients = driver.find_elements_by_xpath("/html/body/div[2]/div/div/div/a")
current_ingredient = ingredients[0].get_attribute("innerText")
ingredients[0].click()
time.sleep(3)
# go to edit page
driver.find_element_by_xpath("/html/body/div[2]/div/div/a[2]").click()
time.sleep(2)
# get value of name input
input_name = driver.find_element_by_xpath("//*[@id='product_name']")
input_value = input_name.get_attribute("value")
assert current_ingredient[3:] == input_value
# add string to current value of the input and assign new value to variable and save
input_name.send_keys('test')
new_name = driver.find_element_by_xpath("//*[@id='product_name']").get_attribute("value")
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/div/form/input[4]").click()
time.sleep(2)
assert current_ingredient != new_name
driver.save_screenshot("screenshots/products/edit_product" + current_ingredient[3:].upper() + ".png")
print("Name of " + current_ingredient[3:] + " changed to " + new_name)


driver.quit()
