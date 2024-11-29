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
driver.get('https://www.target.com')
driver.maximize_window()
sleep(2)

# # Click SignIn button
driver.find_element(By.XPATH, "//span[@class='sc-58ad44c0-3 kwbrXj h-margin-r-x3']").click()
sleep(3)

# Click SignIn from side navigation
driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()
sleep(3)

# “Sign into your Target account” text is shown
expected = 'Sign into your Target account'
actual = driver.find_element(By.XPATH, "//h1/span").text
assert expected == actual, f'Expected {expected} did not match actual {actual}'

# SignIn button is shown
driver.find_element(By.ID, 'login')

sleep(6)


driver.quit()



