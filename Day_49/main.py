import os
import time
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime as dt, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

ACCOUNT_EMAIL = "dominik@test2.com"  # The email you registered with
GYM_URL = "https://appbrewery.github.io/gym/"
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)

driver.get(GYM_URL)

login_btn = WebDriverWait(driver,100).until(EC.presence_of_element_located(
  (By.ID, "login-button")))
login_btn.click()
email_input = WebDriverWait(driver,100).until(EC.presence_of_element_located(
  (By.ID, "email-input")))
email_input.send_keys(ACCOUNT_EMAIL)
password_input = WebDriverWait(driver,100).until(EC.presence_of_element_located(
  (By.ID, "password-input")))
password_input.send_keys(ACCOUNT_PASSWORD)
submit_btn = WebDriverWait(driver,100).until(EC.presence_of_element_located(
  (By.ID, "submit-button")))
submit_btn.click()

class_containers = WebDriverWait(driver, 10).until(
  EC.presence_of_all_elements_located((By.XPATH, "//p[starts-with(@id, 'class-time-')]/ancestor::div[4]"))
)

for container in class_containers:
  if container.text.startswith("Tue"):
    time_elements = container.find_elements(By.CSS_SELECTOR, "p[id^='class-time-']")
    print(f"Class Time: {time_elements[0].text}")
    for time_el in time_elements:
      if time_el.text == "Time: 6:00 PM":
        parent = time_el.find_element(By.XPATH, "ancestor::div[2]")
        btn = parent.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")
        btn.click()
        print(parent.text)

    print("-" * 20)
# driver.quit()