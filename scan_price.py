from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
options.add_argument("--headless=new")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

url = "https://dropstab.com/coins/monad"
driver.get(url)

print("Scanning price...")

while True:
    try:
        price_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h2[contains(@class,'text-2xl')]"))
        )

        price = price_element.text.strip()
        print(f"[{time.strftime('%H:%M:%S')}] MON Price: {price}")

    except Exception as e:
        print(f"[{time.strftime('%H:%M:%S')}] Price not found (DOM changed or slow JS)")

    time.sleep(1)
