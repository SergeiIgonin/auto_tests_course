""" Загрузка файла на страницу """

import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    line1 = browser.find_element(By.CSS_SELECTOR, "form div :nth-child(2)")
    line1.send_keys('Ivan')
    line2 = browser.find_element(By.CSS_SELECTOR, "form div :nth-child(4)")
    line2.send_keys('Ivanov')
    line3 = browser.find_element(By.CSS_SELECTOR, "form div :nth-child(6)")
    line3.send_keys('vanya@mail.ru')
    
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file = "example.txt"
    file_path = os.path.join(current_dir, file)
    
    element = browser.find_element(By.CSS_SELECTOR, "#file")
    element.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(4)
    browser.quit()
