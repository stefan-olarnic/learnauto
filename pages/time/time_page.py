from core import BasePage

class TimePage(BasePage):
    PAGE_TITLE = "Time"

    def __init__(self, context):
        super().__init__(context)

    def open(self):
        self.click_menu("Time")

