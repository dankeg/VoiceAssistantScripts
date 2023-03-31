from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
import random,time,os,sys
from selenium.webdriver.common.keys import Keys

mail_address = "cathryce"
password = "KeyboardEgg"


driver = uc.Chrome()

time.sleep(.4)
driver.get("https://accounts.google.com/ServiceLogin?elo=1")
driver.implicitly_wait(0.2)
wait = WebDriverWait(driver, 10)
time.sleep(.4)

x = wait.until(EC.presence_of_element_located(("xpath", "//input[@type='email']")))
x = driver.find_element("xpath", "//input[@type='email']")
for i in mail_address:
    x.send_keys(i)
    time.sleep(.4)
x.send_keys(Keys.ENTER)

time.sleep(3)

x = wait.until(EC.presence_of_element_located(("xpath", "//input[@type='password']")))
x = driver.find_element("xpath", "//input[@type='password']")
for i in password:
    x.send_keys(i)
    time.sleep(.5)
x.send_keys(Keys.ENTER)

time.sleep(3)

driver.implicitly_wait(0.2)
driver.get("https://www.google.com/")
time.sleep(.5)

driver.get("https://myadcenter.google.com/controls?ref=my-account&hl=en")
time.sleep(1)

x = driver.find_element("xpath", "//div[@class='KSSg1d']")
x.click()
time.sleep(1)

x = driver.find_element("xpath", "//span[@class='VfPpkd-DVBDLb-LhBDec-sM5MNb']")
x.click()
time.sleep(2)

x = driver.find_element("xpath", "//span[@class='V5g4xf-RLmnJb']")
action = webdriver.common.action_chains.ActionChains(driver)
action.move_to_element_with_offset(x, 50, 0)
action.click()
action.perform()
time.sleep(10)


driver.get("https://myadcenter.google.com/controls?ref=my-account&hl=en")
time.sleep(20)

x = driver.find_element("xpath", "//div[@class='KSSg1d']")
x.click()
time.sleep(1)

x = driver.find_element("xpath", "//span[@class='VfPpkd-DVBDLb-LhBDec-sM5MNb']")
x.click()
time.sleep(1)

x = driver.find_element("xpath", "//span[@class='V5g4xf-RLmnJb']")
action = webdriver.common.action_chains.ActionChains(driver)
action.move_to_element_with_offset(x, 50, 0)
action.click()
action.perform()
time.sleep(10)
