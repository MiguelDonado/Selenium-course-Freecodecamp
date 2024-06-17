from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()

options.add_experimental_option("detach", True)

options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=options)
driver.get("https://the-internet.herokuapp.com/login")
driver.implicitly_wait(5)
username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")

username.send_keys("tomsmith")
password.send_keys("SuperSecretPassword!")

btn = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
btn.click()
