from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()

options.add_experimental_option("detach", True)

options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=options)
driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
driver.implicitly_wait(30)
parent_element = driver.find_element("id", "start")
child_element = parent_element.find_element(By.TAG_NAME, "button")
child_element.click()

WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#finish > h4"), "Hello World!")
)
