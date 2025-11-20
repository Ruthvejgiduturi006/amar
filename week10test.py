from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Create a new Chrome browser instance
driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.com")

# Print the title of the page
print("Page Title:", driver.title)

# Find the search box and type something
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium testing with Python")

# Close the browser after 5 seconds
import time
time.sleep(5)
driver.quit()
