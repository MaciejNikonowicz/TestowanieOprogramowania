def logging(email, password, driver):
    driver.get("http://vol4-capybara.herokuapp.com/users/sign_in")
    driver.find_element_by_id("user_email").send_keys(email)
    driver.find_element_by_id("user_password").send_keys(password)
    driver.find_element_by_name("commit").click()