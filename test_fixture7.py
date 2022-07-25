import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

@pytest.mark.parametrize('adress', ["236895","236896","236897","236898","236899","236903","236904","236905"])
class TestParam:
    @pytest.fixture(scope="function")
    def browser(self):
        print("\nstart browser for test..")
        browser = webdriver.Chrome()
        yield browser
        print("\nquit browser..")
        browser.quit()
    def test_right_answer(self,browser,adress):
        link = f"https://stepik.org/lesson/{adress}/step/1"
        browser.get(link)
        time.sleep(5)
        textarea = browser.find_element(By.CSS_SELECTOR, ".textarea")
        answer = math.log(int(time.time()))
        textarea.send_keys(answer)
        submit_button = browser.find_element(By.CSS_SELECTOR, ".submit-submission")
        submit_button.click()
        time.sleep(2)
        correct = browser.find_element(By.CLASS_NAME, "smart-hints__hint")
        ezz = correct.text
        assert ezz == "Correct!", "Неправильный ответ"

