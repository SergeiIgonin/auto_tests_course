""" Проверка соответствия ожидаемого текста сообщения с фактическим """
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/wait1.html"
    browser.get(link)
    time.sleep(1)#если это убрать,то выдаст ошибку NoSuchElementException
    button = browser.find_element(By.ID, "verify")
    button.click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text
    
finally:
    time.sleep(3)
    browser.quit()

#ВАЖНО!
#Почему без вставки ожидания(time) selenium выдаст ошибку?
#Потому что в момент выполнения команды find_element(By.ID, "verify")
#элемент с id="verify"(кнопка) еще не успевает прогрузиться на странице.
#Метод find_element() сделает только одну попытку найти элемент
#и в случае неудачи уронит наш тест.
