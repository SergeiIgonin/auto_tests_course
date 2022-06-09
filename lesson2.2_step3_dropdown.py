""" Выпадающий список """

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try:
    link = 'http://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "#dropdown").click()

    a = browser.find_element(By.CSS_SELECTOR, "#num1")
    a1 = int(a.text)
    
    b = browser.find_element(By.CSS_SELECTOR, "#num2")
    b1 = int(b.text)

    total = str(a1+b1)

    #1й способ:
    #from selenium.webdriver.support.ui import Select
    #select = Select(browser.find_element(By.CSS_SELECTOR, "select"))
    #select.select_by_value(total)
    
    #2й способ:
    browser.find_element_by_css_selector(f'[value="{total}"]').click()
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    
finally:
    time.sleep(3)
    browser.quit()
    
