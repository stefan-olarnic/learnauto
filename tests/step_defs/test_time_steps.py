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

@given(parsers.parse('User is on "{page_name}" page'))
def user_on_page(logged_context, page_name):
    page = PAGE_MAP[page_name](logged_context)
    page.click_menu(page_name)
    page.verify_page()

@when('Select personal timesheets')
def selecting_my_timesheet(logged_context):
      time_page = TimePage(logged_context)
      time_page.select_element_from_dropdown(
          TimePage.MENU_TIMESHEETS,           
          TimePage.DROPDOWN_MY_TIMESHEETS
      )
