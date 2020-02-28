from selenium import webdriver
import unittest
import time
class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
       cls.driver = webdriver.Chrome("C:/Users/nvemula/Downloads/chromedriver_win32/chromedriver.exe")
       cls.driver.maximize_window()
    def test_registration(self):
        driver = self.driver
# opening the website
        driver.get(
            "https://idp.nature.com/register/natureuser?redirect_uri=https%3A%2F%2Fwww.nature.com%2Fmy-account")
        titleOfWebPage = driver.title
#using assertion method
        self.assertEqual("Nature Registration", titleOfWebPage, "webpage title is not matching")
        #printing the web page title
        print((driver.title))
        #locating elements using find_element method
        first_name = driver.find_element_by_id("registration-first-name").send_keys("nithya")
        last_Name = driver.find_element_by_name("lastName").send_keys("naidu")
        e_mail=driver.find_element_by_name("email").send_keys("vemulanithya@gmail.com")
        password=driver.find_element_by_name("password").send_keys("23456@78p")
        confirmPassword=driver.find_element_by_id("registration-password-confirm").send_keys("23456@78p")
        agree=driver.find_element_by_name("acceptedTermsAndConditions").click()
        register=driver.find_element_by_id("registration-submit").click()
        time.sleep(10)
        Thanks_page=driver.find_element_by_id("content-heading").text
        print (Thanks_page)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("test completed")

if __name__ == '__main__':
    unittest.main()