import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_stealth import stealth

class InternetSpeedTweeterBot():
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
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        accept_cookies_btn = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
        (By.ID, "onetrust-accept-btn-handler")))
        accept_cookies_btn.click()

        go_btn = self.driver.find_element(By.CLASS_NAME, "start-text")
        go_btn.click()
        time.sleep(50)
        download_speed = self.driver.find_element(By.CSS_SELECTOR, ".result-data-value.download-speed").text

        upload_speed = self.driver.find_element(By.CSS_SELECTOR, ".result-data-value.upload-speed").text

        print(f"down: {download_speed}")
        print(f"up: {upload_speed}")




    def tweet_at_provider(self):
        self.driver.get("https://x.com/i/flow/login")
