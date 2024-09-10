from selenium.webdriver.common.by import By
class MainPageLocators:
    login_button=(By.XPATH,'//div/ul/li/a[@href="/login"]')
class SignUpLogin:
    login_title = (By.XPATH, "//h2[contains(text(), 'New User Signup!')]")
    name_box = (By.XPATH, '//input[@type="text"]')
    email_box = (By.XPATH, '//input[@type="email"]')
    sign_up_button = (By.XPATH, '// button[@data-qa="login-button"]')
    radio_button = (By.ID,"id_gender1")
    password_box = (By.ID, 'password')
    dropdown1 = (By.ID, 'days')
    dropdown2 = (By.ID, 'months')
    dropdown3 = (By.ID, 'years')
    check_box1 = (By.XPATH, '//label[@for="newsletter"]')
    check_box2 = (By.XPATH, '//label[@for="optin"]')