import random
import time

from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SIMILAR_ACCOUNT = "pokemontcg"
PASSWORD = ""
EMAIL = ""

class InstaFollower():
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)

        self.chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        self.chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.chrome_options.add_experimental_option('useAutomationExtension', False)

        self.driver = webdriver.Chrome(options=self.chrome_options)

        stealth(self.driver,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
                )

    def login(self):
        self.driver.get("https://www.instagram.com")
        time.sleep(2)
        cookies_btn = self.driver.find_element(By.XPATH,
                                               "/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]")
        cookies_btn.click()

        email_input = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
            (By.NAME, "email")))

        pass_input = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
            (By.NAME, "pass")))

        email_input.clear()
        email_input.send_keys(EMAIL)
        pass_input.clear()
        pass_input.send_keys(PASSWORD)

        login_btn = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='login_form']/div/div[1]/div/div[3]/div/div")))
        login_btn.click()
        time.sleep(5)
        self.find_followers()

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")
        time.sleep(2)
        followers = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                        f'//a[contains(@href, "/{SIMILAR_ACCOUNT}/followers")]')))
        followers.click()
        time.sleep(2)
        self.follow()


    def follow(self):
        container = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH,
                                                                                        "/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div")))
        all_follow_btns = container.find_elements(By.CSS_SELECTOR, "._aswp._aswr._aswu._asw_._asx2")

        for btn in all_follow_btns:
            random_sleep = random.randint(2, 5)
            if btn.text == "Follow":
                self.driver.execute_script("arguments[0].click();", btn)
            time.sleep(random_sleep)