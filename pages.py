from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement

from element import *
from locators import *
import unittest


class BasePage(object):
    def __init__(self,driver):
        self.driver = driver


class MainPage(BasePage):
    def title(self):
        title = self.driver.title
        return title

    def click_login_button(self):
        login_button = self.driver.find_element(By.XPATH, '//div/ul/li/a[@href="/login"]')
        login_button.click()

    def click_contact_us_button(self):
        contact_us_button = self.driver.find_element(By.XPATH, '//a[contains(text(),"Contact us")]')
        contact_us_button.click()

    def scroll_down_to_bottom(self):
        bottom_button = self.driver.find_element(By.ID,'subscribe')
        action = ActionChains(self.driver)
        action.scroll_to_element(bottom_button).perform()

    def click_back_to_top_button(self):
        back_to_top_button = self.driver.find_element(By.XPATH,'//i[@class="fa fa-angle-up"]')
        back_to_top_button.click()


class LoginPage(BasePage):
    def is_title_matches1(self):
        login_title = self.driver.find_element(By.XPATH, "//h2[contains(text(), 'Login to your account')]")
        login_title_text = login_title.text
        return login_title_text

    def is_title_matches2(self):
        login_title2 = self.driver.find_element(By.XPATH, "//h2[contains(text(), 'New User Signup!')]")
        login_title_text = login_title2.text
        return login_title_text

    def input_name(self):
        name_box = self.driver.find_element(By.XPATH, '//input[@type="text"]')
        name_box.send_keys('Brain')

    def input_email1(self):
        email_box1 = self.driver.find_element(By.XPATH, '//input[@data-qa="login-email"]')
        email_box1.send_keys('123456789@qq.com')

    def input_email2(self):
        email_box2 = self.driver.find_element(By.XPATH, '//input[@data-qa="signup-email"]')
        email_box2.send_keys('2510668237@qq.com')

    def click_sign_up_button(self):
        sign_up_button = self.driver.find_element(By.XPATH, '// button[@data-qa="signup-button"]')
        sign_up_button.click()

    def click_login_button(self):
        login_button=self.driver.find_element(By.XPATH, '// button[@data-qa="login-button"]')
        login_button.click()

    def submit_form(self):
        form_element=self.driver.find_element(By.XPATH,'//form[@action="/login"]')
        form_element.submit()


    def click_radio_button(self):
        radio_button = self.driver.find_element(By.ID, "id_gender1")
        radio_button.click()
    def input_password1(self):
        password_box1 = self.driver.find_element(By.XPATH, '//input[@data-qa="login-password"]')
        password_box1.send_keys('123456789')

    def input_password2(self):
        password_box2 = self.driver.find_element(By.ID, 'password')
        password_box2.send_keys('zhangcwq991314')

    def select_days(self):
        dropdown1 = self.driver.find_element(By.ID, 'days')
        select1 = Select(dropdown1)
        select1.select_by_visible_text('1')

    def select_months(self):
        dropdown2 = self.driver.find_element(By.ID, 'months')
        select2 = Select(dropdown2)
        select2.select_by_visible_text('January')

    def select_years(self):
        dropdown3 = self.driver.find_element(By.ID, 'years')
        select3 = Select(dropdown3)
        select3.select_by_visible_text('2021')

    def click_checkbox1(self):
        check_box1 = self.driver.find_element(By.XPATH, '//label[@for="newsletter"]')
        check_box1.click()

    def click_checkbox2(self):
        check_box2 = self.driver.find_element(By.XPATH, '//label[@for="optin"]')
        check_box2.click()

    def input_first_name(self):
        first_name = self.driver.find_element(By.ID,'first_name')
        first_name.send_keys('zhang')

    def input_last_name(self):
        last_name = self.driver.find_element(By.ID,'last_name')
        last_name.send_keys('brain')

    def input_company(self):
        company = self.driver.find_element(By.ID,'company')
        company.send_keys('KGU')

    def input_address1(self):
        address1 = self.driver.find_element(By.ID,'address1')
        address1.send_keys('suzhou')

    def input_address2(self):
        address2 = self.driver.find_element(By.ID,'address2')
        address2.send_keys('suzhou')

    def select_country(self):
        country_dropdown=self.driver.find_element(By.ID,'country')
        select = Select(country_dropdown)
        select.select_by_visible_text('United States')

    def input_state(self):
        state = self.driver.find_element(By.ID, 'state')
        state.send_keys('jiangsu')

    def input_city(self):
        city = self.driver.find_element(By.ID, 'state')
        city.send_keys('suzhou')

    def input_zipcode(self):
        zipcode = self.driver.find_element(By.ID, 'zipcode')
        zipcode.send_keys('123456')

    def input_mobile_number(self):
        mobile_number = self.driver.find_element(By.ID, 'mobile_number')
        mobile_number.send_keys('123456789')

    def click_create_account_button(self):
        create_account_button = self.driver.find_element(By.XPATH,'//button[@data-qa="create-account"]')
        create_account_button.click()

    def content_is_match(self):
        content=self.driver.find_element(By.TAG_NAME,'b')
        return content


class ContactUsPage(BasePage):

    def is_title_matches1(self):
        title = self.driver.title
        return title

    def input_name(self):
        name_box=self.driver.find_element(By.XPATH,'//input[@name="name"]')
        name_box.send_keys('123456789')

    def input_email(self):
        email_box=self.driver.find_element(By.XPATH,'//input[@name="email"]')
        email_box.send_keys('123456789@qq.com')

    def input_subject(self):
        subject_box = self.driver.find_element(By.XPATH,'//input[@name="subject"]')
        subject_box.send_keys('123456789')

    def input_message(self):
        message_box = self.driver.find_element(By.ID,'message')
        message_box.send_keys('123456789')

    def up_load_file(self):
        up_load_file_box = self.driver.find_element(By.XPATH, '//input[@type="file"]')
        file_path=r'C:\Users\YAN\Desktop\1701912406108.png'
        up_load_file_box.send_keys(file_path)

    def click_submit_button(self):
        submit_button = self.driver.find_element(By.XPATH,'//input[@name="submit"]')
        submit_button.click()

    def click_ok_button(self):
        alert=Alert(self.driver)
        alert.accept()

    def success_title_is_match(self):
        success_title_box=self.driver.find_element(By.XPATH,'//div[@class="status alert alert-success"]')
        success_title=success_title_box.text
        return success_title

    def click_home_button(self):
        home_button=self.driver.find_element(By.XPATH,'//a[@class="btn btn-success"]')
        home_button.click()





