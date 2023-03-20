from selenium.webdriver.common.by import By


class SettingPageLocators:
    GENERAL = (By.CSS_SELECTOR, '#p-tabpanel-2-label')
    SKYPE = (By.XPATH, './/input[@name="skype"]')
    TELEGRAM = (By.XPATH, './/input[@name="telegramm"]')
    SAVEBUTTON = (By.XPATH, r'//*[@data-e2e="btn_save-settings"]')
