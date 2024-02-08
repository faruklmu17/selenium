from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import sys
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com/")
time.sleep(2)
# find the google searchbox
search_box = driver.find_element(By.NAME, "q")
search_box.click()
search_box.send_keys("weather")
search_box.send_keys(Keys.ENTER)
time.sleep(5)
locate_python = sys.exec_prefix
print(locate_python) 
