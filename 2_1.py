import math
import time
from selenium import webdriver

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/get_attribute.html')

    # x = browser.find_element_by_css_selector("#input_value").text

    x = browser.find_element_by_css_selector("#treasure").get_attribute('valuex')
    answer = str(math.log(abs(12 * math.sin(int(x)))))
    browser.find_element_by_css_selector("#answer").send_keys(answer)
    time.sleep(1)

    browser.find_element_by_css_selector("#robotCheckbox").click()
    time.sleep(1)

    browser.find_element_by_css_selector("#robotsRule").click()
    time.sleep(1)

    browser.find_element_by_css_selector('button').click()

finally:
    time.sleep(5)
    browser.quit()