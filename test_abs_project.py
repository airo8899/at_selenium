import unittest
from selenium import webdriver

# class TestAbs(unittest.TestCase):
#     def test_abs(self):
#         self.assertEqual(abs(-42), 42, "Should be absolute value of a number")

#     def test_abs2(self):
#         self.assertEqual(abs(-42), -42, "Should be absolute value of a number")


def reg(link):
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector('.first_block .first').send_keys('a')
    browser.find_element_by_css_selector('.first_block .second').send_keys('a')
    browser.find_element_by_css_selector('.first_block .third').send_keys('a')

    browser.find_element_by_class_name('btn').click()

    welcome_text = browser.find_element_by_css_selector('h1').text

    browser.quit()
    return welcome_text


class TestReg(unittest.TestCase):
    def test_reg1(self):
        self.assertEqual(reg("http://suninjuly.github.io/registration1.html"), 
                            "Congratulations! You have successfully registered!", 
                            "fail")
    
    def test_reg2(self):
        self.assertEqual(reg("http://suninjuly.github.io/registration2.html"), 
                            "Congratulations! You have successfully registered!", 
                            "fail")

if __name__ == "__main__":
    unittest.main()
