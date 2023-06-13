import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1 opening browser
driver = webdriver.Chrome()
# 2 going to url
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
# hard time
time.sleep(2)
# Enter UserName
driver.find_element(By.NAME, "username").send_keys('Admin')

# Enter Password
driver.find_element(By.NAME, "password").send_keys('admin123')

# Click on login button
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(2)
# Click on menu button
driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']").click()
# Click on logout button
driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()


# parallel run
# reports
# Data driven
# hardcode value
# grouping \ selection test cases
# multiple time write same type of code
# time consuming
