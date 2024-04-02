from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

x = "Antony"
y = "Freeman"
e = "some.email@mail.com"

class TestInput(unittest.TestCase):
    def test_fill_form1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your first name"]').send_keys(x)
        browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your last name"]').send_keys(y)
        browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your email"]').send_keys(e)

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, msg="Test not pass")

        time.sleep(3)
        browser.quit()
    def test_fill_form2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your first name"]').send_keys(x)
        browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your last name"]').send_keys(y)
        browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your email"]').send_keys(e)

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, msg="Test not pass")

        time.sleep(3)
        browser.quit()

if __name__ == "__main__":
    unittest.main()
