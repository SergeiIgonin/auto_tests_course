""" Уникальные селекторы """

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link1 = "http://suninjuly.github.io/registration1.html"
    link2 = "http://suninjuly.github.io/registration2.html"    
    browser = webdriver.Chrome()
    browser.get(link1)

    firstname = browser.find_element(By.CSS_SELECTOR, 'div.first_block input.form-control.first')
    #способ 1:
    #firstname = browser.find_element(By.CSS_SELECTOR, '.first_block .first')
    #способ 2:                                
    #firstname = browser.find_element(By.XPATH, '//div[@class="first_block"]//input[@class ="form-control first"]')    
    #способ 3:
    #firstname = browser.find_element(By.XPATH, '//label[contains(text(), "First")]//following-sibling::input')
    #способ 4:
    #firstname = browser.find_element(By.CSS_SELECTOR, ".first_block div:nth-child(1) input")
    firstname.send_keys("Вася")

  
    lastname = browser.find_element(By.CSS_SELECTOR, 'div.first_block input.form-control.second')
    #способ 1:
    #lastname = browser.find_element(By.CSS_SELECTOR, '.first_block .second')
    #способ 2: 
    #lastname = browser.find_element(By.XPATH, '//div[@class="first_block"]//input[@class ="form-control second"]')  
    #способ 3:
    #lastname = browser.find_element(By.XPATH, '//label[contains(text(), "Last")]//following-sibling::input')
    #способ 4:
    #firstname = browser.find_element(By.CSS_SELECTOR, ".first_block div:nth-child(2) input")
    lastname.send_keys("Рогов")

    
    email = browser.find_element(By.CSS_SELECTOR, 'div.first_block input.form-control.third')
    #способ 1:
    #email = browser.find_element(By.CSS_SELECTOR, '.first_block .third')
    #способ 2:                                     
    #email = browser.find_element(By.XPATH, '//div[@class="first_block"]//input[@class ="form-control third"]')
    #способ 3:    
    #email = browser.find_element(By.XPATH, '//label[contains(text(), "Email")]//following-sibling::input')
    #способ 4:
    #firstname = browser.find_element(By.CSS_SELECTOR, ".first_block div:nth-child(3) input")
    email.send_keys("vasya@rogov")

    
    time.sleep(1)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(3)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(1)
    browser.quit()

