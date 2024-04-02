from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from function import input_text
import math
from time import sleep

# current_dir = os.path.abspath(os.path.dirname(__file__))   
# file_path = os.path.join(current_dir, 'example.txt')           
# first = 'John'
# last = 'andersen'
# email = 'exmple@mail.com'


browser = webdriver.Chrome()

browser.get('http://suninjuly.github.io/explicit_wait2.html')
# 
# input_text(first, last, email)
condition = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
# browser.find_element(By.ID, 'file').send_keys(file_path)
browser.find_element(By.ID, 'book').click()

x = browser.find_element(By.ID, 'input_value').text
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser.find_element(By.ID, 'answer').send_keys(calc(x))
browser.find_element(By.ID, 'solve').click()
sleep(5)