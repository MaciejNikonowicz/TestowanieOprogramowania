from selenium import webdriver
from login_func import logging
import time
import os


driver = webdriver.Chrome(os.getcwd()+'\drivers\chromedriver.exe')

driver.set_page_load_timeout(30)

# log in and go to new ingredient page
logging('admin@admin.com', 'password', driver)
driver.get("http://vol4-capybara.herokuapp.com/ingredients/new")
assert "Add new ingredient" in driver.page_source

# select option Avocado for test purposes
selected_product = driver.find_element_by_xpath("//*[@id='ingredient_product_id']/option[text()='avocado']")
selected_product.click()

# get 'Avocado' string from option value
product = selected_product.get_attribute(
            "innerHTML")
time.sleep(1)
driver.find_element_by_id("ingredient_quantity").send_keys(1)
time.sleep(2)
driver.find_element_by_id("ingredient_exp_date").send_keys(27082019)
time.sleep(2)
driver.find_element_by_name("commit").click()
time.sleep(2)
# get ingredient list, check for Avocado, if exists click it and delete
ingredients = driver.find_elements_by_xpath('/html/body/div[2]/div/div[2]/form/table/tbody/tr/td/a')
for x in ingredients:
    if x.get_attribute('innerText') == product:
        print('The product is ' + product)
        driver.save_screenshot("screenshots/ingredients/new_ingredient" + product.upper() + ".png")
        driver.find_element_by_link_text(product).click()
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[2]/div/a[3]').click()
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(2)

print("New ingredient " + product + " added successfully and then deleted")
driver.quit()