""" Уникальные селекторы, заполнение обязательных полей """

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    #рабочий сайт:
    link1 = "http://suninjuly.github.io/registration1.html"
    #забагованный сайт:
    #link2 = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link1)
    
    # 1й способ - автозаполнения всех полей по единому образцу при помощи цикла:
    #elements = browser.find_elements(By.CSS_SELECTOR, "input[type]")
    #for element in elements:
    #    element.send_keys("абырвалг")

    # 2й способ - заполнение полей по очереди отдельно:
    # Отправляем заполненную форму1:
    firstname = browser.find_element(By.CSS_SELECTOR, 'div input.form-control.first')
    firstname.send_keys("Nikita")

    # Отправляем заполненную форму2:
    lastname = browser.find_element(By.TAG_NAME, 'div input.form-control.second')
    lastname.send_keys("Petrosyan")

    # Отправляем заполненную форму3:
    phone = browser.find_element(By.TAG_NAME, 'div input.form-control.third')
    phone.send_keys(int("89376594062"))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(2)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(1)
    browser.quit()
