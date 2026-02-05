from core import BasePage
from pages.time.time_locators import menu_tab_by_text, dropdown_option_by_text

class TimePage(BasePage):
    PAGE_TITLE = "Time"

    MENU_TIMESHEETS = "Timesheets"
    DROPDOWN_MY_TIMESHEETS = "My Timesheets"

    def __init__(self, context):
        super().__init__(context)

    def open(self):
        self.click_menu("Time")

    def select_element_from_dropdown(self, menu_tab, dropdown_option):
        # Click pe tab-ul din navbar (ex: "Timesheets")
        self.click(menu_tab_by_text(menu_tab))

        # Click pe opțiunea din dropdown (ex: "My Timesheets")
        self.click(dropdown_option_by_text(dropdown_option))

