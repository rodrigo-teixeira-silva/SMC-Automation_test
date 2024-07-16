from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome() 
browser.implicitly_wait(10)
browser.maximize_window()
browser.get("https://app.kodigos.com.br/scm/front/")


browser.find_element(By.XPATH,'//*[@id="app"]/div/div/div/div/div/div/div[1]/aside/div/div/div[1]/div/div/a[3]').click()
time.sleep(3)

browser.find_element(By.XPATH,'//*[@id="app"]/div/div/div/div/div/div/div[2]/main/div/div[4]/div/div/div[1]/table/tbody/tr[1]/td[6]').click()
time.sleep(4)

browser.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div/div[3]/button[2]/span[2]').click()
time.sleep(4)

browser.find_element(By.XPATH,'/html/body/div[4]/div/div[2]/div/div[4]/button[2]/span[2]').click()
time.sleep(5)
