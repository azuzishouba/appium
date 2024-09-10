# This sample code supports Appium Python client >=2.3.0
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

options = AppiumOptions()
options.load_capabilities({
	"appium:automationName": "UiAutomator2",
	"appium:platformName": "Android",
	"appium:platformVersion": "14",
	"appium:deviceName": "emulator-5554",
	"appium:app": "C:\\Users\\YAN\\Downloads\\ApiDemos-debug.apk",
	"appium:newCommandTimeout": 3600,
	"appium:connectHardwareKeyboard": True
})

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Views")
el1.click()
actions = ActionChains(driver)
actions.w3c_actions=ActionBuilder(driver=driver,mouse=PointerInput(interaction.POINTER_TOUCH,'touch'))
actions.w3c_actions.pointer_action.move_to_location(383,1849)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(396, 264)
actions.w3c_actions.pointer_action.release()
actions.perform()
