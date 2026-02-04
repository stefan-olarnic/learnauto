from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from core.base_locators import LOCATORS, main_menu_item

class BasePage:
    PAGE_TITLE = None

    def __init__(self, context):
        self.context = context
        self.driver = context.driver
        self.wait = WebDriverWait(self.driver, 10)

    def find(self, locator):
        for i in range(3):
            try:
                return self.wait.until(EC.presence_of_element_located(locator))
            except StaleElementReferenceException:
                if i == 2:
                    raise

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator))
        self.find(locator).click()

    def type(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text

    def verify_page(self):
        actual_title = self.get_text(LOCATORS["page_title"])
        assert actual_title == self.PAGE_TITLE, \
            f"Expected page '{self.PAGE_TITLE}' but got '{actual_title}'"

    def click_menu(self, name):
        self.click(main_menu_item(name))