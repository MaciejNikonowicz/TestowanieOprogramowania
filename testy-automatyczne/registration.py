from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import random


driver = webdriver.Chrome(os.getcwd()+'\drivers\chromedriver.exe')


# explicit wait for element to be located
def is_element_exist(xpath):
    try:
        wait = WebDriverWait(driver, 5)
        wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        print("Element Found")
    except TimeoutException:
        return False


driver.get("http://vol4-capybara.herokuapp.com/users/sign_up")
assert "Vol4Capybara" in driver.title
assert "Sign up" in driver.page_source
# register user with random number in email address to prevent duplication of users
driver.find_element_by_id("user_email").send_keys("someuser" + str(random.randrange(100)) + "@user.com")
driver.find_element_by_id("user_password").send_keys("password")
driver.find_element_by_id("user_password_confirmation").send_keys("password")
driver.find_element_by_id("user_avatar").send_keys(os.getcwd()+"/avatar.png")
driver.save_screenshot("screenshots/register/newuser_before.png")
time.sleep(3)
driver.find_element_by_xpath("//*[@id='new_user']/div[5]/input").click()
time.sleep(3)
driver.save_screenshot("screenshots/register/newuser_after.png")
assert "Check your fridge" in driver.page_source
print("User successfully registered")
# going to user edit page after successful register to check if avatar exists there and hence was added properly
driver.get("http://vol4-capybara.herokuapp.com/users/edit")
image = driver.find_element_by_xpath("//*[@id='edit_user']/div[5]/img")
is_element_exist("//*[@id='edit_user']/div[5]/img")
assert "remove the avatar" in driver.page_source
driver.save_screenshot("screenshots/register/edit_user_avatar.png")
print("Avatar added properly")

driver.quit()
