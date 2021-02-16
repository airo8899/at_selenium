import time
import math
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/explicit_wait2.html')

    # browser.implicitly_wait(5)
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element ((By.ID, 'price'), '$100'))
    browser.find_element_by_css_selector('#book').click()

    x = browser.find_element_by_css_selector('#input_value').text
    answer = str(math.log(abs(12*math.sin(int(x)))))
    browser.find_element_by_css_selector('#answer').send_keys(answer)
    browser.find_element_by_css_selector('#solve').click()
    
    # message = browser.find_element_by_css_selector('#verify_message').text

    assert 'successful' in message

finally:
    time.sleep(8)
    browser.quit()