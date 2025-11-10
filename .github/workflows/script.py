from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

# Setup headless Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Create driver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Open a website
    driver.get("https://example.com")
    print(f"Opened: {driver.title}")
    
    time.sleep(5)  # Wait 5 seconds
    
    # You can open more sites
    driver.get("https://github.com")
    print(f"Opened: {driver.title}")
    
    time.sleep(5)
    
finally:
    driver.quit()
    print("Browser closed")
