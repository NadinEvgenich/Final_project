from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, r'//*[@data-e2e="form_email"]')
    PASSWORD_INPUT = (By.XPATH, r'//*[@data-e2e="form_password"]')
    LOGIN_BTN = (By.XPATH, r'//*[@data-e2e="login"]')
    ERROR = (By.CSS_SELECTOR, '.error_label.input_label.text-center.orangeText.ng-star-inserted')