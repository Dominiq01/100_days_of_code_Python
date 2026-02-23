from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.rebel.pl/pokemon/ultra-pro-pokemon-9-pocket-zippered-binder-elite-series-arceus-2029212.html")

# By.ID
# By.CSS_SELECTOR
# By.NAME
# By.XPATH
# add_to_cart_btn = driver.find_element(By.CLASS_NAME, "add-to-cart__btn")

# .tag_name
# .get_attribute
# print(add_to_cart_btn.text)
driver.get("https://www.python.org/")
names = [el.text for el in driver.find_elements(By.CSS_SELECTOR, ".event-widget ul.menu li a")]
dates = [el.text for el in driver.find_elements(By.CSS_SELECTOR, ".event-widget ul.menu li time")]
print(names)
print(dates)
new_dict = {}

for i in range(0, len(names)):
    new_dict[i] = {"time": dates[i], "name": names[i] }

print(new_dict)

driver.quit()