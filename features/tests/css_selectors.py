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


# Amazon logo
driver.find_element(By.CSS_SELECTOR,"i.a-icon.a-icon-logo")

# Create account
driver.find_element(By.CSS_SELECTOR,"h1.a-spacing-small")

# Name field
driver.find_element(By.CSS_SELECTOR,'#ap_customer_name')

# Email
driver.find_element(By.CSS_SELECTOR,".a-input-text.a-span12.auth-required-field.auth-require-fields-match.auth-require-email-validaton")

# Password field
driver.find_element(By.CSS_SELECTOR,"input.a-input-text.a-form-normal.auth-require-password-validation")

# Re-enter password field
driver.find_element(By.CSS_SELECTOR, "#ap_password_check")

# Create Account
driver.find_element(By.CSS_SELECTOR,"input#continue")

# Sign in link
driver.find_element(By.CSS_SELECTOR,"[href*='/ap/signin?openid.pape.max_auth_age']")

# Conditions of Use
driver.find_element(By.CSS_SELECTOR, "a[href='/ap/lwa/agreement?agreementName=conditionsOfUse']")

# Privacy Notice
driver.find_element(By.CSS_SELECTOR,"a[href*='Name=privacyNotice']")







#CSS
driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox")

driver.find_element(By.CSS_SELECTOR, "input.nav-input.nav-progressive-attribute")

#CSS By attributes
driver.find_element(By.CSS_SELECTOR, "a[href='/ref=nav_logo']")

#CSS By attr partial match
driver.find_element(By.CSS_SELECTOR,"a[href*='=nav_cs_customerservice']")