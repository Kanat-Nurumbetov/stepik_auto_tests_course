import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
from function import login

answer = math.log(int(time.time()))

@pytest.mark.parametrize('link', [
'https://stepik.org/lesson/236895/step/1',
# 'https://stepik.org/lesson/236896/step/1',
# 'https://stepik.org/lesson/236897/step/1',
# 'https://stepik.org/lesson/236898/step/1',
# 'https://stepik.org/lesson/236899/step/1',
# 'https://stepik.org/lesson/236903/step/1',
# 'https://stepik.org/lesson/236904/step/1',
# 'https://stepik.org/lesson/236905/step/1',
])
def test_login_to_site(browser, link):
    browser.get(link)
    WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.LINK_TEXT, "Войти")))
    browser.find_element(By.LINK_TEXT, "Войти").click()
    login(browser)
    WebDriverWait(browser, 5).until(EC.invisibility_of_element_located((By.ID, "id_login_password")))
    browser.find_element(By.CLASS_NAME, 'placeholder="Напишите ваш ответ здесь..."').send_keys(answer)
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Отправить')))
    browser.find_element(By.LINK_TEXT, 'Отправить').click()

    result = browser.find_element(By.CLASS_NAME, "attempt__message")
    assert 'Correct!' in result
