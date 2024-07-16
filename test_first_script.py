from asyncio import wait
import select
from selenium import webdriver

from selenium.webdriver.support.select import Select

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time

servico = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=servico) 
browser.implicitly_wait(10)
browser.maximize_window()
browser.get("https://app.kodigos.com.br/scm/front/")

browser.find_element(By.XPATH,'//*[@id="app"]/div/div/div/div/div/div/div[1]/aside/div/div/div[1]/div/div/a[2]').click()
time.sleep(3)

browser.find_element(By.XPATH,'//*[@id="app"]/div/div/div/div/div/div/div[2]/main/div/div[3]/div[2]/label/div[2]/a/span[2]').click()
time.sleep(3)


dropdown_filial = Select(browser.find_element(By.XPATH, '//div[@class="dropdown-menu"]')) 
dropdown_filial.select_by_value('01/01 - Instituto Kodigos')
time.sleep(3)


# input de texto
browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div/div/div[2]/main/div/div[4]/div[2]/label').send_keys('Rodrigo_teixeira')
time.sleep(3)


