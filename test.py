#-------------------------------------------------------------------------------
# Name:        Тестовое задание
# Author:      Игонин Сергей
# Created:     11/09/2022
#-------------------------------------------------------------------------------
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

try:
    link1 = 'https://r7-office.ru/request_personal'
    browser = webdriver.Chrome()
    browser.get(link1)
    time.sleep(1)
    
    browser.execute_script("window.scrollTo(0, +350);")
    browser.implicitly_wait(1)
    
    #локаторы сециально разнообразил
    line1 = browser.find_element(By.XPATH, "//input[@name = 'first_name']")
    line1.send_keys("Ivan")
    
    line2 = browser.find_element(By.XPATH, "//input[@name = 'last_name']")
    line2.send_keys("Petrov")
    
    email = browser.find_element(By.XPATH, "//input[@name = 'email']")
    email.send_keys("petrov_vanya@gmail.com")

    phone = browser.find_element(By.CSS_SELECTOR, "div input.t-input-phonemask")
    phone.send_keys("1234567890")
    
    checkbox1 = browser.find_element(By.XPATH, "//label//following-sibling::div")
    checkbox1.click()
    
    checkbox2 = browser.find_element(By.CSS_SELECTOR, "form>*>:nth-child(6)>*>*>div")
    checkbox2.click()
    
    button = browser.find_element(By.XPATH, "//button[contains(text(), 'Отправить')]")
    button.click()
    time.sleep(1)

    link2 = 'https://r7-office.ru/downloads#1_2'
    browser.get(link2)
    time.sleep(1)

    OS1 = browser.find_element(By.XPATH, "//a[contains(text(), 'Альт Линукс')]")
    OS2 = browser.find_element(By.XPATH, "//a[contains(text(), 'РОСА Линукс')]")  
    OS3 = browser.find_element(By.XPATH, "//a[contains(text(), 'Astra Linux')]")   
    OS4 = browser.find_element(By.XPATH, "//a[contains(text(), 'РЕД ОС')]")
    
    OS_list = [OS1.text, OS2.text, OS3.text, OS4.text]
    print (str(OS_list))

finally:
    time.sleep(1)
    browser.quit()
