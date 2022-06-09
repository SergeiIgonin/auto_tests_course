""" Поиск атрибута, подставление его в функцию """

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try:
    link = 'http://suninjuly.github.io/get_attribute.html'
    browser = webdriver.Chrome()
    browser.get(link)

    box = browser.find_element(By.CSS_SELECTOR, "#treasure")
    x = box.get_attribute("valuex")
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    total = calc(x)

    input_line = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_line.send_keys(total)

    kryzhik = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    kryzhik.click()
    
    radbtn = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radbtn.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
finally:
    time.sleep(8)
    browser.quit()
    
