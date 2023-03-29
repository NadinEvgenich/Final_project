import allure
from locators.login_page_locators import LoginPageLocators as Locators
from pages.BasePage import BasePage


class LoginPage(BasePage):

    @allure.step('Ввести значение в поле ввода "Email"')
    def enter_value_into_email_field(self, value: str):
        self.fill_edit_field(locator=Locators.EMAIL_INPUT, value=value)

    @allure.step('Ввести значение в поле ввода "Password"')
    def enter_value_into_password_field(self, value: str):
        self.fill_edit_field(locator=Locators.PASSWORD_INPUT, value=value)

    @allure.step('Кликнуть по кнопке "Login"')
    def click_login_btn(self):
        self.find_element(Locators.LOGIN_BTN).click()

    @allure.step('Авторизоваться в админ панели с email {email} и паролем {password}')
    def _login(self, email: str, password: str):
        self.enter_value_into_email_field(value=email)
        self.enter_value_into_password_field(value=password)
        self.click_login_btn()

    @allure.step('Ошибка при авторизации')
    def error_login(self):
        return self.get_element(Locators.ERROR)
