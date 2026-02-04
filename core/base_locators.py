from selenium.webdriver.common.by import By

LOCATORS = {
    "page_title": (By.CSS_SELECTOR, ".oxd-topbar-header-breadcrumb h6"),
}

def main_menu_item(name):
    return (By.XPATH, f"//span[contains(@class, 'oxd-main-menu-item--name') and text()='{name}']/ancestor::a")
