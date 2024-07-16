from asyncio import wait
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome() 
browser.implicitly_wait(10)
browser.maximize_window()
browser.get("https://app.kodigos.com.br/scm/front/")

browser.find_element(By.XPATH,'//*[@id="app"]/div/div/div/div/div/div/div[1]/aside/div/div/div[1]/div/div/a[2]').click()

browser.find_element(By.XPATH,'//*[@id="app"]/div/div/div/div/div/div/div[2]/main/div/div[3]/div[2]/label/div[2]/a/span[2]').click()
time.sleep(5)

browser.find_element(By.XPATH,'//*[@id="app"]/div/div/div/div/div/div/div[2]/main/div/div[3]/div[2]/label/div/div/div[2]/i').click()
time.sleep(3)


#Esperar até que o campo "Filial" esteja disponível e clicar nele
# wait = WebDriverWait(driver, 10)
# filial_field = wait.until(EC.element_to_be_clickable((By.ID, 'f_952a7000-e715-4da7-8949-35d2f9056cf9')))
# filial_field.click()
# time.sleep(10)
# Esperar até que o menu dropdown esteja disponível e selecionar "01/01 - Instituto Kodigos"
#browser = wait.Select(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div/div/div/div/div[2]/main/div/div[3]/div[2]/label/div/div/div[1]'))).select_by_visible_text('01/01 - Instituto Kodigos')
# browser.click()
time.sleep(10)

