from core import BasePage
from core.base_locators import LOCATORS as BASE_LOCATORS
from pages.login import LOCATORS

class LoginPage(BasePage):

    def __init__(self, context):
        super().__init__(context)

    def open(self):
        self.driver.get(self.context.base_url + "/web/index.php/auth/login")

    def login(self, username=None, password=None):
        user = username or self.context.validuser.username
        pwd = password or self.context.validuser.password

        self.type(LOCATORS["username"], user)
        self.type(LOCATORS["password"], pwd)
        self.click(LOCATORS["login_button"])

    def get_message(self):
        try:
            return self.find(BASE_LOCATORS["page_title"]).text
        except:
            return self.find(LOCATORS["error_message"]).text