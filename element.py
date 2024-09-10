import unittest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from  selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class BasePageElement(object):
    def __init__(self):
        self.path = r"D:\geckodriver-v0.35.0-win64\geckodriver.exe"
        self.service = Service(executable_path=self.path)
        self.driver = webdriver.Firefox(service=self.service)