from pytest_bdd import scenarios, given, when, then, parsers
from pages.login import LoginPage

# Încarcă toate scenariile din login.feature
scenarios('../features/login.feature')

# Step: Given I am on the login page
@given('User is on login page')
def open_login_page(context):
    page = LoginPage(context)
    page.open()
    context.login_page = page

# Step: When I login with username "..." and password "..."
@when(parsers.parse('User login with username "{username}" and password "{password}"'))
def login_with_credentials(context, username, password):
    context.login_page.login(username, password)

# Step: Then I should see the message "..."
@then(parsers.parse('"{expected_message}" is displayed'))
def verify_message(context, expected_message):
    actual_message = context.login_page.get_message()
    assert expected_message in actual_message, \
        f"Expected '{expected_message}' but got '{actual_message}'"