from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")


name = driver.find_element(By.NAME, "fName")
name.send_keys("Dominik")
last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("TEST")
email = driver.find_element(By.NAME, "email")
email.send_keys("dominik@test.com")
btn = driver.find_element(By.CLASS_NAME, "btn")
btn.click()

# driver.quit()