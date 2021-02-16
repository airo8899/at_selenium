import time
from selenium import webdriver

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector('.first_block .form-control.first')
    input1.send_keys('a')
    time.sleep(1)

    input2 = browser.find_element_by_css_selector('.first_block .form-control.second')
    input2.send_keys('a')
    time.sleep(1)

    input3 = browser.find_element_by_css_selector('.first_block .form-control.third')
    input3.send_keys('a')
    time.sleep(1)

    browser.find_element_by_class_name('btn').click()

    time.sleep(1)

    welcome_text = browser.find_element_by_css_selector('h1').text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)
    browser.quit()
    