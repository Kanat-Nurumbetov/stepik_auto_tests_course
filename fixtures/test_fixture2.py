import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
from function import login



@pytest.mark.parametrize('link', [
'https://stepik.org/lesson/236895/step/1',
'https://stepik.org/lesson/236896/step/1',
'https://stepik.org/lesson/236897/step/1',
'https://stepik.org/lesson/236898/step/1',
'https://stepik.org/lesson/236899/step/1',
'https://stepik.org/lesson/236903/step/1',
'https://stepik.org/lesson/236904/step/1',
'https://stepik.org/lesson/236905/step/1',
])
def test_login_to_site(browser, link):
    browser.get(link)
    WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.LINK_TEXT, "Войти"))).click()
    login(browser)
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "navbar__profile-img")))
    time.sleep(3)
    
    text_area = browser.find_element(By.CSS_SELECTOR, '[placeholder="Напишите ваш ответ здесь..."]')

    answer = math.log(int(time.time()))
    text_area.clear()
    text_area.send_keys(str(answer))
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, 'submit-submission'))).click()
    # browser.find_element(By.LINK_TEXT, 'Отправить').click()
    time.sleep(3)

    result = browser.find_element(By.CLASS_NAME, "attempt__message").text
    assert 'Correct!' in result, "Тест не прошел"
    
    browser.quit()
    print(f"Тест не прошел, фидбек: {result}")
    
