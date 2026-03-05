import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
URL = "https://appbrewery.github.io/Zillow-Clone/"
FORM_URL = "https://forms.gle/u18BX2NASCEdQ42w7"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
response = requests.get(URL)
response.raise_for_status()
soup = BeautifulSoup(response.content, "html.parser")

list_of_properties = [el for el in soup.select(".ListItem-c11n-8-84-3-StyledListCardWrapper")]
list_of_links = [el.find("a", {"class": "property-card-link"}).get('href') for el in list_of_properties]

list_of_prices = [el.find("span", {"class": "PropertyCardWrapper__StyledPriceLine"}).text.split("+")[0] for el in list_of_properties]
list_of_prices_formatted = [el.split("/")[0] for el in list_of_prices]
list_of_addresses = [el.find("address").text.strip() for el in list_of_properties]


for index in range(len(list_of_properties)):
    driver.get(FORM_URL)
    address_input = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
        (By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")))
    address_input.clear()
    address_input.send_keys(list_of_addresses[index])
    price_input = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
        (By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")))
    price_input.clear()
    price_input.send_keys(list_of_prices_formatted[index])
    link_input = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
        (By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")))
    link_input.clear()
    link_input.send_keys(list_of_links[index])

    submit_btn = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
        (By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div/span")))
    submit_btn.click()