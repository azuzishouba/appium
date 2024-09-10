import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from  selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import pages


class Automation_Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.path = r"D:\chromedriver-win64\chromedriver-win64\chromedriver.exe"
        cls.service = Service(executable_path=cls.path)
        cls.driver = webdriver.Chrome(service=cls.service)
        cls.driver.get('http://automationexercise.com')


    def test_sign_up(self):
        mainpage = pages.MainPage(self.driver)
        self.assertEqual(mainpage.title(),'Automation Exercise')
        mainpage.click_login_button()
        loginpage = pages.LoginPage(self.driver)
        self.assertEqual(loginpage.is_title_matches2(), 'New User Signup!')
        loginpage.input_name()
        loginpage.input_email()
        loginpage.click_sign_up_button()
        loginpage.click_radio_button()
        loginpage.input_password()
        loginpage.select_days()
        loginpage.select_months()
        loginpage.select_years()
        loginpage.click_checkbox1()
        loginpage.click_checkbox2()
        loginpage.input_first_name()
        loginpage.input_last_name()
        loginpage.input_company()
        loginpage.input_address1()
        loginpage.input_address2()
        loginpage.select_country()
        loginpage.input_state()
        loginpage.input_city()
        loginpage.input_zipcode()
        loginpage.input_mobile_number()
        loginpage.click_create_account_button()
        self.assertEqual(loginpage.content_is_match(),'Account Created! ')

    def test_login(self):
        mainpage = pages.MainPage(self.driver)
        self.assertEqual(mainpage.title(), 'Automation Exercise')
        mainpage.click_login_button()
        loginpage = pages.LoginPage(self.driver)
        self.assertEqual(loginpage.is_title_matches1(), 'Login to your account')
        loginpage.input_email1()
        loginpage.input_password1()
        loginpage.submit_form()
        time.sleep(10)

    def test_contact_us_form(self):
        mainpage = pages.MainPage(self.driver)
        self.assertEqual(mainpage.title(), 'Automation Exercise')
        contactuspage=pages.ContactUsPage(self.driver)
        mainpage.click_contact_us_button()
        self.assertEqual(contactuspage.is_title_matches1(), 'Automation Exercise - Contact Us')
        contactuspage.input_name()
        contactuspage.input_email()
        contactuspage.input_subject()
        contactuspage.input_message()
        contactuspage.up_load_file()
        contactuspage.click_submit_button()
        contactuspage.click_ok_button()
        self.assertEqual(contactuspage.success_title_is_match(),'Success! Your details have been submitted successfully.')
        contactuspage.click_home_button()

    def test_scroll_up_using_arrow(self):
        mainpage = pages.MainPage(self.driver)
        self.assertEqual(mainpage.title(),'Automation Exercise')
        mainpage.scroll_down_to_bottom()
        time.sleep(3)
        mainpage.click_back_to_top_button()
        time.sleep(3)
        self.driver.get_screenshot_as_file('homepage.png')

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

