""" Переход в новое окно """

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "button.trollface")
    button.click()

    first_window = browser.window_handles[0]
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    #confirm = browser.switch_to.alert
    #confirm.accept()

    y = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = y.text
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    total = calc(x)

    input_line = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_line.send_keys(total)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
       
finally:
    time.sleep(8)
    browser.quit()
    
