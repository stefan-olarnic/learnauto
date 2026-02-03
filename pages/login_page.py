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
        self.driver.get(self.context.base_url + "/web/index.php/auth/login")

    def login(self, username=None, password=None):
      # Dacă nu dai parametri, folosește userul din context
      user = username or self.context.validuser.username
      pwd = password or self.context.validuser.password

      self.driver.find_element(*self.username).send_keys(user)
      self.driver.find_element(*self.password).send_keys(pwd)
      self.driver.find_element(*self.login_button).click()

    def get_message(self):
        return self.driver.find_element(*self.message).text