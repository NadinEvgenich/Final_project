import allure

from data.data import WEB
from faker import Faker
from pages.BasePage import BasePage
from pages.LoginPage import LoginPage
from pages.OfferDetailPage import OfferDetailPage
from pages.OffersPage import OffersPage

f = Faker()
message = f.words(10)


@allure.suite('[Pytest][UI]')
@allure.title('Проверка, что вeб не может запросить доступ к вип-офферу')
def test_request_offer(driver):
    login_page = LoginPage(driver)
    login_page._open(path='/login')

    login_page._login(
        email=WEB['email'],
        password=WEB['password'],
    )
    offers = OffersPage(driver)
    offers._open(path='/offers')
    offers.search_offer(id=31571)
    offers.wait_loader_not_visible()
    offers.wait_tableloader_not_visible()
    offer_detail = OfferDetailPage(driver)
    offer_detail._open(path='/offers/offer-details?id=31571')
    offer_detail.click_request_btn()
    offer_detail.send_request(message=message)
    toast = offer_detail.find_element(BasePage.TOASTERROR)
    assert toast.is_displayed()
