from pytest_bdd import scenarios, given, when, then, parsers
from core import BasePage
from pages.dashboard import DashboardPage
from pages.time import TimePage

# Încarcă toate scenariile din time.feature
scenarios('../features/time.feature')

PAGE_MAP = {
      "Dashboard": DashboardPage,
      "Time": TimePage,
  }

@given('User is logged in')
def user_is_logged_in(logged_context):
    dashboard = DashboardPage(logged_context)
    dashboard.verify_page()

@when(parsers.parse('User clicks on "{menu_item}" menu item'))
def click_menu_item(logged_context, menu_item):
    BasePage(logged_context).click_menu(menu_item)

@then(parsers.parse('"{page_name}" page is displayed'))
def verify_page_displayed(logged_context, page_name):
    page = PAGE_MAP[page_name](logged_context)
    page.verify_page()      