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
driver.maximize_window()
driver.implicitly_wait(5)

# open the url
driver.get('https://www.target.com')

# Search
driver.find_element(By.ID, 'search').send_keys('basket')
driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
sleep(6)

#Verification
expected_result = 'basket'
actual_result = driver.find_element(By.XPATH, "//span[@class='h-text-bs h-display-flex h-flex-align-center h-text-grayDark h-margin-l-x2']").text
assert expected_result in actual_result, f'Expected test {expected_result} not in actual {actual_result}'

print('Test case passed')

driver.quit()



