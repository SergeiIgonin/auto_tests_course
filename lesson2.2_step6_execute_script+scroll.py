""" Добавление JavaScript при скролле """

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try:
    link = 'http://SunInJuly.github.io/execute_script.html'
    browser = webdriver.Chrome()
    browser.get(link)

    x0 = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = int(x0.text)

    def calc (x):
        return str (math.log(abs(12*math.sin(int(x)))))
    z = calc(x)  

    line = browser.find_element(By.CSS_SELECTOR, "#answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", line)
    line.send_keys(z)

    k = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    k.click()

    r = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    r.click()
                             
    b = browser.find_element(By.CSS_SELECTOR, "button.btn.btn")
    b.click()
    
finally:
    time.sleep(7)
    browser.quit()

    
