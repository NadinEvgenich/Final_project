import allure
from locators.offers_page_locators import OffersPageLocators as Locators
from pages.BasePage import BasePage


class OffersPage(BasePage):
    @allure.step('Ввести айди оффера')
    def enter_value_into_offer_field(self, value: int):
        self.fill_edit_field(Locators.SEARCH, value=value)

    @allure.step('Кликнуть по кнопке "Apply"')
    def click_apply_btn(self):
        self.find_element(Locators.APPLYBTN).click()

    @allure.step('Поиск оффера')
    def search_offer(self, id: int):
        self.enter_value_into_offer_field(value=id)
        self.click_apply_btn()

    @allure.step('Кликнуть по строке с оффером в таблице')
    def click_offer(self):
        self.driver.implicitly_wait(90)
        self.clickwait_element(Locators.OFFERTABLE).click()
