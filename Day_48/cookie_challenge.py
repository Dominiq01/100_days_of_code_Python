import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://ozh.github.io/cookieclicker/")
cookie = None
delay = 3
try:
    lang = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, "langSelect-PL")))
    lang.click()
    time.sleep(2)
    cookie = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, "bigCookie")))
    cookies_banner_btn = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, "cc_btn_accept_all")))
    cookies_banner_btn.click()
    count = 0
    while True:
        cookie.click()
        count+=1
        products = driver.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")
        upgrades = driver.find_elements(By.CSS_SELECTOR, ".crate.upgrade.enabled")
        available_products = driver.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")

        cookies = float(driver.find_element(By.ID, "cookies").text.split(" ")[0])

        if count > 10:
            if available_products:
                try:
                    best_bet = available_products[-1]
                    driver.execute_script("arguments[0].click();", best_bet)
                except StaleElementReferenceException:
                    pass

            count = 0

            if upgrades:
                for upgrade in upgrades:
                    try:
                        driver.execute_script("arguments[0].click();", upgrade)
                    except StaleElementReferenceException:
                        pass
except TimeoutException:
    print("Loading took too much time!")

