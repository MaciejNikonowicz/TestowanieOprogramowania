from selenium import webdriver
import csv
import time
import os

driver = webdriver.Chrome(os.getcwd()+'\drivers\chromedriver.exe')

with open("csv/logins.csv", encoding="utf8") as csvDataFile:
    csvReader = csv.DictReader(csvDataFile)
    for row in csvReader:
        email = row['email']
        password = row['password']
        driver.set_page_load_timeout(30)
        driver.get("http://vol4-capybara.herokuapp.com/users/sign_in")
        driver.find_element_by_id("user_email").send_keys(email)
        driver.find_element_by_id("user_password").send_keys(password)
        driver.find_element_by_name("commit").click()
        if email == 'admin@admin.com':
            assert 'Available Products' in driver.page_source
            driver.save_screenshot("screenshots/admin-login.png")
        assert "Check your fridge" in driver.page_source
        driver.save_screenshot("screenshots/login/user-login" + email.upper() + ".png")
        driver.find_element_by_id("navbar-wagon-menu").click()
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/ul/li[2]/a").click()
        driver.find_element_by_xpath("/html/body/div[1]/div/a[1]").click()
        time.sleep(3)

driver.quit()
