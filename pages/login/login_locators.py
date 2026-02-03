from selenium.webdriver.common.by import By

LOCATORS = {
    "username":        (By.NAME, "username"),
    "password":        (By.NAME, "password"),
    "login_button":    (By.CSS_SELECTOR, "button[type='submit']"),
    "error_message":   (By.CSS_SELECTOR, ".oxd-alert-content.oxd-alert-content--error"),
    "dashboard_title": (By.CSS_SELECTOR, ".oxd-topbar-header-breadcrumb h6"),
}