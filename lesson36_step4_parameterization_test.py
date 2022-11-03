import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize("links", ["https://stepik.org/lesson/236895/step/1",
                                 "https://stepik.org/lesson/236896/step/1",
                                 "https://stepik.org/lesson/236897/step/1",
                                 "https://stepik.org/lesson/236898/step/1",
                                 "https://stepik.org/lesson/236899/step/1",
                                 "https://stepik.org/lesson/236903/step/1",
                                 "https://stepik.org/lesson/236904/step/1",
                                 "https://stepik.org/lesson/236905/step/1"])
class TestUFO:
    def test_links(self, browser, links):
        answer = str(math.log(int(time.time())))
        link = f"{links}"
        browser.get(link)
        browser.implicitly_wait(10)
        input_area = browser.find_element(By.CSS_SELECTOR, "div textarea")
        input_area.send_keys(f"{answer}")
        
        #button = WebDriverWait(browser, 5).until
        #(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=submit-submission]")))
        
        button = browser.find_element(By.CSS_SELECTOR, "button[class=submit-submission]")
        button.click()
        message = browser.find_element(By.CSS_SELECTOR, "div p[class=smart-hints__hint]")
        assert "Correct!" in message.text

if __name__ == "__main__":
    pytest.main()
