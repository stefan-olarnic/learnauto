from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.login.login_page import LoginPage

def test_valid_login(context):
    page = LoginPage(context)
    page.open()
    page.login()

    assert "You logged into a secure area!" in page.get_message()