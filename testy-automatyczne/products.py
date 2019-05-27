from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from login_func import logging
import csv
import time
import os


driver = webdriver.Chrome(os.getcwd()+'\drivers\chromedriver.exe')

logging('admin@admin.com', 'password', driver)

with open("products.csv", encoding="utf8") as csvDataFile:
    csvReader = csv.DictReader(csvDataFile)
    for row in csvReader:
        name = row['name']
        driver.set_page_load_timeout(30)
        # navigate to new product page and add product
        driver.get("http://vol4-capybara.herokuapp.com/products/new")
        assert "Add a new product" in driver.page_source
        driver.find_element_by_id("product_name").send_keys(name)
        driver.find_element_by_name("commit").click()
        assert name in driver.page_source
        # find new product on the list and take screenshot
        element = driver.find_element_by_partial_link_text(name)
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        driver.save_screenshot("screenshots/products/new_product" + name.upper() + ".png")
        time.sleep(3)
        # navigate to new ingredient and find new product on the list of available ingredients
        driver.get("http://vol4-capybara.herokuapp.com/ingredients/new")
        products = driver.find_elements_by_xpath("//select[@name='ingredient[product_id]']")[0].get_attribute(
            "innerHTML")
        assert name in products
        print(name + " in ingredient list")
        # navigate back to products and delete newly added product
        driver.get("http://vol4-capybara.herokuapp.com/products")
        element = driver.find_element_by_partial_link_text(name)
        element.click()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[2]/div/div/a[3]").click()
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(2)
        print(name + " has been deleted")

driver.quit()

