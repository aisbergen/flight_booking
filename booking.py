import time
from selenium.webdriver.common.by import By
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

options=Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

driver.get("https://www.kiwi.com/ru/search/results/%D0%B0%D1%81%D1%82%D0%B0%D0%BD%D0%B0-%D0%BA%D0%B0%D0%B7%D0%B0%D1%85%D1%81%D1%82%D0%B0%D0%BD/%D0%B0%D0%BB%D0%BC%D0%B0-%D0%B0%D1%82%D0%B0-%D0%BA%D0%B0%D0%B7%D0%B0%D1%85%D1%81%D1%82%D0%B0%D0%BD/2023-11-08/2023-12-29")
driver.maximize_window()
driver.find_element(By.XPATH, '//*[@id="cookies_accept"]/div/div').click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, '#react-view > div.MainViewstyled__Container-sc-16mbl87-0.gipdqx > div.Box__StyledBox-sc-bvm5o6-0.dndrbh > div > div > div > div > div > div.min-w-0.flex-grow.p-md.de\:p-0.de\:pb-lg.de\:ps-lg.de\:pt-lg > div > div > div.Box__StyledBox-sc-bvm5o6-0.kceqXj > div > div > div:nth-child(1) > div > div > div > div.box-border.flex.relative.flex-col.rounded-largest.bg-card.px-md.py-sm.lm\:flex-1.lm\:pe-sm.lm\:pt-md > div.flex.flex-col-reverse.gap-xs.lm\:flex-col > div.flex-1 > span > a > div > div' ).click()
time.sleep(3)
driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/section/div[3]/a').click()
time.sleep(2)
driver.execute_script('scrollBy(0,500)')

email='aisulukakharova@gmail.com'
mail = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/main/div[1]/div[3]/div[2]/div/div/div[1]/div/div/label/div[1]/input')
mail.click()
mail.send_keys(email)
phone='7082265274'
number = driver.find_element(By.XPATH, '//*[@id="1-17"]')
number.click()
number.send_keys(phone)