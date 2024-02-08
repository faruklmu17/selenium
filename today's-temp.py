
#this code searches and finds the current temperature of a day 

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
# find the Google searchbox
search_box = driver.find_element(By.NAME, "q")
search_box.click()
# search and find the current temperature 
search_box.send_keys("weather")
search_box.send_keys(Keys.ENTER)
current_temp = driver.find_element(By.ID, "wob_tm")
# print the temperature
print(f"Current Temperature: {current_temp.text} degrees")
time.sleep(5)
