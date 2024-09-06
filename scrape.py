import time

import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service

def scrape_website(website):
    print("Launching chrome browser...")

    driver = webdriver.Chrome()

    try:
        driver.get(website)
        print("Page Loaded...")
        html = driver.page_source
        time.sleep(3)

        return html
    finally:
        driver.quit()