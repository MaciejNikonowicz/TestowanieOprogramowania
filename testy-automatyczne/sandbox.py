from selenium import webdriver
import time
import os

driver = webdriver.Chrome(os.getcwd()+'\drivers\chromedriver.exe')


# test your code here
driver.set_page_load_timeout(30)
driver.get("http://vol4-capybara.herokuapp.com/ingredients")
assert "Vol4Capybara" in driver.title
driver.find_element_by_id("user_email").send_keys("admin@admin.com")
driver.find_element_by_id("user_password").send_keys("password")
driver.find_element_by_name("commit").click()
driver.find_element_by_id("selected_ingredients_onions").click()
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/form/select[2]/option[2]").click()
driver.find_element_by_name("commit").click()
assert "Recommended Recipes" in driver.page_source
time.sleep(3)
driver.quit()
