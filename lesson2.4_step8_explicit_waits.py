""" Настройка явных ожиданий """ 

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element
                                             ((By.ID, "price"), "$100"))

    button = browser.find_element(By.CSS_SELECTOR, "#book")
    button.click()

    y = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = y.text
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    total = calc(x)

    input_line = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_line.send_keys(total)

    button = browser.find_element(By.CSS_SELECTOR, "#solve")
    button.click()
    
finally:
    time.sleep(5)
    browser.quit()
