from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

global driver

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options = chrome_options)

driver.maximize_window()

driver.get("https://www.facebook.com/")

# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# price_value = driver.find_element(By.CLASS_NAME, "a-price-whole").text
# article_count.click()

email = driver.find_element(By.NAME, "email")
email.send_keys("email")

password = driver.find_element(By.NAME, "pass")
password.send_keys("password")

login = driver.find_element(By.NAME, "login")
login.send_keys(Keys.ENTER)


sleep(30)
