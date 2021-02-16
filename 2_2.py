import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/execute_script.html")

    # answer = str(int(browser.find_element_by_css_selector('#num1').text)
    #             + int(browser.find_element_by_css_selector("#num2").text))
    
    x = browser.find_element_by_css_selector('#input_value').text
    answer = str(math.log(abs(12*math.sin(int(x)))))
    
    # browser.find_element_by_css_selector("#dropdown").click()
    # browser.find_element_by_css_selector("[value='" + answer +"']").click()

    # select = Select(browser.find_element_by_css_selector("#dropdown"))
    # select.select_by_value(answer)

    browser.find_element_by_css_selector('#answer').send_keys(answer)
    
    button = browser.find_element_by_css_selector('button')
    browser.execute_script("return arguments[0].scrollIntoView(true, alignToTop=false);", button)
    
    browser.find_element_by_css_selector('#robotCheckbox').click()

    browser.find_element_by_css_selector('#robotsRule').click()

    button = browser.find_element_by_css_selector('button')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(10)
    browser.quit()

