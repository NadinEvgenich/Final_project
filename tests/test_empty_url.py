import allure

from data.data import WEB
from pages.LoginPage import LoginPage
from pages.OfferDetailPage import OfferDetailPage
from pages.OffersPage import OffersPage


@allure.suite('[Pytest][UI]')
@allure.title('Проверка, что в оффере не доступен tracking url')
def test_empty_url(driver):
    login_page = LoginPage(driver)
    login_page._open(path='/login')

    login_page._login(
        email=WEB['email'],
        password=WEB['password'],
    )
    offers = OffersPage(driver)
    offers._open(path='/offers')
    offers.search_offer(id=34318)
    offers.wait_loader_not_visible()
    offers.wait_tableloader_not_visible()
    offer_detail = OfferDetailPage(driver)
    offer_detail._open(path='/offers/offer-details?id=34318')
    url = offer_detail.get_tracking_url()
    assert url.text == ''
