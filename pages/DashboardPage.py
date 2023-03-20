import allure
from locators.dashboard_page_locators import DashboardPageLocators as Locators
from pages.BasePage import BasePage


class DashboardPage(BasePage):
    @allure.step('Выход из личного кабинета')
    def _logout(self):
        self.clickwait_element(Locators.LOGOUT).click()

    @allure.step('Получить имя пользователя')
    def get_username(self):
        return self.get_element(Locators.USERDROPDOWN)

    @allure.step('Перейти в настройки пользователя')
    def user_settings(self):
        self.clickwait_element(Locators.USERDROPDOWN).click()
        self.clickwait_element(Locators.ACCOUNTSETTINGS).click()

    @allure.step('Перейти в настройки платёжек')
    def user_payment_settings(self):
        self.clickwait_element(Locators.USERDROPDOWN).click()
        self.clickwait_element(Locators.PAYMENTSETTINGS).click()
