from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def login(browser):
    browser.implicitly_wait(5)
    browser.find_element(By.ID, "id_login_email").send_keys("orklik@gmail.com")
    browser.find_element(By.ID, "id_login_password").send_keys("rfyf1987")
    browser.find_element(By.XPATH, '//*[@id="login_form"]/button').click()
    
def type_answer():
    pass