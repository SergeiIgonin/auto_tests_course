from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_abs1():
    try:
        link1 = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link1)
        firstname = browser.find_element(By.CSS_SELECTOR, 'div.first_block input.form-control.first')
        firstname.send_keys("Вася")  
        lastname = browser.find_element(By.CSS_SELECTOR, 'div.first_block input.form-control.second')   
        lastname.send_keys("Рогов")    
        email = browser.find_element(By.CSS_SELECTOR, 'div.first_block input.form-control.third')
        email.send_keys("vasya@rogov")    
        time.sleep(1)
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        assert "Congratulations! You have successfully registered!" == welcome_text
    finally:
        browser.quit()
        
def test_abs2():
    try:
        link2 = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link2)
        firstname = browser.find_element(By.CSS_SELECTOR, 'div.first_block input.form-control.first')
        firstname.send_keys("Вася")
        lastname = browser.find_element(By.CSS_SELECTOR, 'div.first_block input.form-control.second')   
        lastname.send_keys("Рогов")
        email = browser.find_element(By.CSS_SELECTOR, 'div.first_block input.form-control.third')
        email.send_keys("vasya@rogov")    
        time.sleep(1)
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        assert "Congratulations! You have successfully registered!" == welcome_text 
    finally:
        browser.quit()
