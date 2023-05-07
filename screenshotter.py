"""screener.py: Το παρακάτω script τραβάει screenshot αυτόματα απο το windy για τα 4 νησιά."""

__author__      = "Alex Perrakis"
__copyright__   = "Research and Informatics Corps,  95th National Guard Higher Command, 2023, Rhodes"
__date__        = "26-04-2023"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from PIL import Image
from io import BytesIO
import datetime
import os

def open_chrome_and_capture_screenshot(driver, url, island_name):
    # Navigate to the website and wait for it to load
    driver.get(url)

    # Wait for 10 seconds to ensure the website is fully loaded
    sleep(10)  


    # We need to change knots to Bft only the first time because it keeps it cached
    if island_name == "ΡΟΔΟΣ":
        # Find the button element by its class names
        buttons = driver.find_elements(By.CLASS_NAME, 'metric-clickable')
        # Click the 3rd found element to change knots to Bft
        buttons[2].click()

        # Wait for 5 seconds for graphics to load
        sleep(5)  

    # Take a screenshot and save it
    screenshot = driver.get_screenshot_as_png()

    directory_name = 'ΚΑΙΡΟΣ ' + date_str

    if not os.path.exists(directory_name):
        os.makedirs(directory_name)

    Image.open(BytesIO(screenshot)).save(directory_name + '\\' + island_name + '.png')


# Get tomorrow date's formatted string
date_str = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")

# Island Windy.com urls
rhodes_url = 'https://www.windy.com/36.438/28.223?' + date_str + '-09,36.186,28.224,9'
megisti_url = 'https://www.windy.com/36.143/29.583?' + date_str + '-09,36.079,29.583,11'
karpathos_url = 'https://www.windy.com/35.507/27.213?' + date_str + '-09,35.253,27.213,9'
sumi_url = 'https://www.windy.com/36.613/27.838?' + date_str + '-09,36.487,27.838,10'

# Set up the Chrome driver with headless mode
driver = webdriver.Chrome()

open_chrome_and_capture_screenshot(driver, rhodes_url, 'ΡΟΔΟΣ')
open_chrome_and_capture_screenshot(driver, megisti_url, 'ΜΕΓΙΣΤΗ')
open_chrome_and_capture_screenshot(driver, karpathos_url, 'ΚΑΡΠΑΘΟΣ')
open_chrome_and_capture_screenshot(driver, sumi_url, 'ΣΥΜΗ')

# Quit the driver
driver.quit()




