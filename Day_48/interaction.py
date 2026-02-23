from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("http://en.wikipedia.org/wiki/Main_Page")

active_editors_wiki = driver.find_element(By.CSS_SELECTOR, '[title="Special:Statistics"]')
print(active_editors_wiki.text)
# active_editors_wiki.click()
search_btn = driver.find_element(By.CLASS_NAME, "search-toggle")
search_btn.click()
searchbar = driver.find_element(By.NAME, "search")
searchbar.send_keys("Greninja", Keys.ENTER)

# driver.quit()