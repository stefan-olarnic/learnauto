from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, context):
        self.context = context
        self.driver = context.driver

    username = (By.ID, "username")
    password = (By.ID, "password")
    login_button = (By.CSS_SELECTOR, "button[type='submit']")
    message = (By.ID, "flash")

    def open(self):
        self.driver.get(self.context.base_url + "/login")

    def login(self):
        self.driver.find_element(*self.username).send_keys(self.context.validuser.username)
        self.driver.find_element(*self.password).send_keys(self.context.validuser.password)
        self.driver.find_element(*self.login_button).click()

    def get_message(self):
        return self.driver.find_element(*self.message).text