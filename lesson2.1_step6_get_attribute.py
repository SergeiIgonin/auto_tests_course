""" Проверка атрибута "checked" по умолчанию """

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = 'http://suninjuly.github.io/math.html'  
    browser = webdriver.Chrome()
    browser.get(link)

    people_radio = browser.find_element(By.ID, "peopleRule") #ответ будет true
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked) 
    assert people_checked == "true" #>>> value of people radio: true
    #assert people_checked is None  #>>> value of people radio: true/AssertionError

    #Для другого варианта:
    #robots_radio = browser.find_element(By.ID, "robotsRule") #отв будет None
    #robots_checked = robots_radio.get_attribute("checked")
    #print("value of robots radio: ", robots_checked)
    #assert robots_checked is None    #>>> value of robots radio: None
    ##assert robots_checked == "true" #>>> value of robots radio: None/AssertionError
    
finally:
    browser.quit()
    
