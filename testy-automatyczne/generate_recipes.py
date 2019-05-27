from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from login_func import logging
import time
import os


driver = webdriver.Chrome(os.getcwd()+'\drivers\chromedriver.exe')

driver.set_page_load_timeout(30)
logging("admin@admin.com", "password", driver)
driver.get("http://vol4-capybara.herokuapp.com/ingredients")
assert "What would you like to eat?" in driver.page_source

# find all the checkboxes and save as a list
ingredients = driver.find_elements_by_name('selected_ingredients[]')
counter = 0
x = 0
# loop through checkboxes, check, generate recipe, uncheck, check next , repeat
while counter < len(ingredients):
        ingredients[x].click()
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/form/input[2]').click()
        time.sleep(2)
        assert "Recommended Recipes" in driver.page_source
        print("Recipes for position " + str((counter + 1)) + " generated")
        element = driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/div[1]/div/a')
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        time.sleep(2)
        driver.save_screenshot("screenshots/API/recipes" + str(counter) + ".png")
        # find all checkboxes again, cause otherwise they will unattach from DOM
        ingredients = driver.find_elements_by_name('selected_ingredients[]')
        ingredients[x].click()
        counter += 1
        x += 1


driver.quit()


