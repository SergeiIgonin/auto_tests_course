""" Настройка неявных ожиданий """

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    link1 = "http://suninjuly.github.io/wait1.html" #задержка загрузки
    link2 = "http://suninjuly.github.io/wait2.html" #задержка кликабельности
    
    browser.get(link1)
    browser.implicitly_wait(5)
    
    button = browser.find_element(By.ID, "verify")
    button.click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text
    
finally:
    time.sleep(3)
    browser.quit()

#задержка прогрузки кнопки - можно решить с пом. implicitly_wait(5)
#задержка кликаб.(активности) кнопки - можно решить только с пом. импорта
#библиотеки WebDriverWait, модуля expected_conditions и настройки метода until.
