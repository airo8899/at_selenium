
import time
import math
from selenium import webdriver

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/redirect_accept.html')

    browser.find_element_by_css_selector('button').click()
    
    # browser.switch_to.alert.accept()

    browser.switch_to.window(browser.window_handles[1])

    x = browser.find_element_by_css_selector('#input_value').text
    answer = str(math.log(abs(12*math.sin(int(x)))))

    browser.find_element_by_css_selector('#answer').send_keys(answer)

    browser.find_element_by_css_selector('button').click()

finally:
    time.sleep(8)
    browser.quit()