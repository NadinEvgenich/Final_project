import allure
from locators.offerdetail_page_locators import OfferdetailPageLocators as Locators
from pages.BasePage import BasePage


class OfferDetailPage(BasePage):
    @allure.step('Получить tracking url')
    def get_tracking_url(self):
        return self.get_element(Locators.TRACKINGURL)

    @allure.step('Кликнуть по кнопке "Request approval"')
    def click_request_btn(self):
        self.find_element(Locators.REQUESTBTN).click()

    @allure.step('Ввести сообщение')
    def enter_value_into_message_field(self, value: str):
        self.fill_edit_field(Locators.TEXTAREA, value=value)

    @allure.step('Кликнуть по кнопке "Send request"')
    def click_send_btn(self):
        self.find_element(Locators.SENDBTN).click()

    @allure.step('Отправить запрос с сообщением')
    def send_request(self, message: str):
        self.enter_value_into_message_field(value=message)
        self.click_send_btn()
