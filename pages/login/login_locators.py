from selenium.webdriver.common.by import By

LOGIN_LOCATORS = {
    "username":        (By.NAME, "username"),
    "password":        (By.NAME, "password"),
    "login_button":    (By.CSS_SELECTOR, "button[type='submit']"),
    "error_message":   (By.CSS_SELECTOR, ".oxd-alert-content.oxd-alert-content--error"),
}