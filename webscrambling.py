from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "/Users/salihkocatrk/Downloads/chromedriver-mac-arm64/chromedriver"

# Tarayıcı ayarları
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
# options.add_argument("--headless")
# WebDriver başlatma
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

try:
    url = "https://thispersondoesnotexist.com/"
    for i in range(1, 5):
        driver.get(url)
        screenshot_path_after = f"screenshot{i}.png"
        driver.save_screenshot(screenshot_path_after)
        print(f"ekran görüntüsü alındı: {screenshot_path_after}")
        time.sleep(2)


finally:
    driver.quit()
#https://youtu.be/-80SQSVRBw4?si=-bBnLWWP_CoVdsl9
