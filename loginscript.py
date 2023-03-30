from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#Work in progress script for logging into a selenium account, using a chrome profile on a computer
#May allow login errors to be bypassed, but requires a profile to be made for the account, and thus is device specific
#Data dir, and profile name change by operating system, and how many profiles are on a device

options = webdriver.ChromeOptions()
options.add_argument('user-data-dir=/Users/ganeshdanke/Library/Application Support/Google/Chrome')
options.add_argument('profile-directory=Default')
driver = webdriver.Chrome(executable_path=r"/Applications/Google_Chrome.app", options=options)
driver.get('https://google.com')