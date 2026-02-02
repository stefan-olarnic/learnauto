import pytest
from selenium import webdriver
from core.context import Context
from config.config import ENVIRONMENTS
from core.user import User

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
