import allure

from data.data import WEB
from pages.BasePage import BasePage
from pages.DashboardPage import DashboardPage
from pages.LoginPage import LoginPage
from pages.PaymentSettingsPage import PaymentSettingsPage


@allure.suite('[Pytest][UI]')
@allure.title('Создание платёжного аккаунта')
def test_edit_contacts(driver):
    login_page = LoginPage(driver)
    login_page._open(path='/login')

    login_page._login(
        email=WEB['email'],
        password=WEB['password'],
    )
    dashboard = DashboardPage(driver)
    dashboard._open(path='/dashboard')
    dashboard.user_payment_settings()
    payment_settings = PaymentSettingsPage(driver)
    payment_settings._open(path='/settings/payment-settings')
    payment_settings.go_to_tron()
    payment_settings.enter_value_into_wallet_field('TUxqbqzUDUF4kC3ruxDUiKDMWcEEp8rne9')
    payment_settings.enter_value_into_comment_field('trc')
    payment_settings.click_save()
    toast = payment_settings.find_element(BasePage.TOASTSUCCES)
    assert toast.is_displayed()
