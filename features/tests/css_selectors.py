from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)


# open the url
driver.get('https://www.amazon.com')
driver.maximize_window()
sleep(2)

#CSS
driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox")

driver.find_element(By.CSS_SELECTOR, "input.nav-input.nav-progressive-attribute")

#CSS By attributes
driver.find_element(By.CSS_SELECTOR, "a[href='/ref=nav_logo']")

#CSS By attr partial match
driver.find_element(By.CSS_SELECTOR,"a[href*='=nav_cs_customerservice']")