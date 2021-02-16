import time
from selenium import webdriver
import os

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/file_input.html')

    browser.find_element_by_name('firstname').send_keys('aaa')
    browser.find_element_by_name('lastname').send_keys('aaa')
    browser.find_element_by_name('email').send_keys('aaa')

    path = os.path.abspath(os.path.dirname(__file__))
    print(path)
    path = os.path.join(path, 'file.txt')
    print(path)
    browser.find_element_by_css_selector('#file').send_keys(path)
    
    browser.find_element_by_css_selector('button').click()

finally:
    time.sleep(5)
    browser.quit()