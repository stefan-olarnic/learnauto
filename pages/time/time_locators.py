from selenium.webdriver.common.by import By

TIME_LOCATORS = {

}

def menu_tab_by_text(text):
    """Returnează locator pentru tab din navbar după text"""
    return (
        By.XPATH,
        f"//span[contains(@class, 'oxd-topbar-body-nav-tab-item') and normalize-space()='{text}']"
    )

def dropdown_option_by_text(text):
    """Returnează locator pentru item din dropdown după text"""
    return (
        By.XPATH,
        f"//a[contains(@class, 'oxd-topbar-body-nav-tab-link') and normalize-space()='{text}']"
    )