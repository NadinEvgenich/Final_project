import allure
from locators.payment_settings_page_locators import PaymentSettingPageLocators as Locators
from pages.BasePage import BasePage


class PaymentSettingsPage(BasePage):
    @allure.step('Перейти на вкладку USDT TRON')
    def go_to_tron(self):
        self.find_element(Locators.TRON).click()

    @allure.step('Ввести номер кошелька')
    def enter_value_into_wallet_field(self, value: str):
        self.fill_edit_field(locator=Locators.USDTADDRESS, value=value)

    @allure.step('Ввести комментарий')
    def enter_value_into_comment_field(self, value: str):
        self.fill_edit_field(locator=Locators.COMMENT, value=value)

    @allure.step('Кликнуть на кнопку "Save payment account"')
    def click_save(self):
        self.clickwait_element(Locators.SAVEBTN).click()
