import pytest
from selenium import webdriver
from config.config import ENVIRONMENTS
from core import User, Context
from pages.login.login_page import LoginPage

@pytest.fixture
def context():
    env = "qa"
    driver = webdriver.Chrome()

    data = ENVIRONMENTS[env]

    valid_user = User(
        data["valid_user"]["username"],
        data["valid_user"]["password"]
    )

    ctx = Context(driver, data["base_url"], env, valid_user)

    yield ctx

    driver.quit()

# 🔹 Fixture cu autologin
@pytest.fixture
def logged_context(context):
    page = LoginPage(context)
    page.open()
    page.login()  # folosește userul din context
    yield context
    # Nu trebuie să închidem browser aici, se face în context