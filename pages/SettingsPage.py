import allure
from locators.settings_page_locators import SettingPageLocators as Locators
from pages.BasePage import BasePage


class SettingsPage(BasePage):
    @allure.step('Перейти на вкладку general')
    def go_to_general(self):
        self.clickwait_element(Locators.GENERAL).click()

    @allure.step('Ввести новый скайп')
    def enter_value_into_skype_field(self, value: str):
        self.fill_edit_field(locator=Locators.SKYPE, value=value)

    @allure.step('Ввести новый телеграм')
    def enter_value_into_telegram_field(self, value: str):
        self.fill_edit_field(locator=Locators.TELEGRAM, value=value)

    @allure.step('Нажать сохранить')
    def save(self):
        self.clickwait_element(Locators.SAVEBUTTON).click()
