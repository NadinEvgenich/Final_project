import allure

from data.data import WEB
from faker import Faker
from pages.BasePage import BasePage
from pages.DashboardPage import DashboardPage
from pages.LoginPage import LoginPage
from pages.SettingsPage import SettingsPage

f = Faker()
skype = f.words(1)
telegram = f.words(1)


@allure.suite('[Pytest][UI]')
@allure.title('Редактирование контактов')
def test_edit_contacts(driver):
    login_page = LoginPage(driver)
    login_page._open(path='/login')

    login_page._login(
        email=WEB['email'],
        password=WEB['password'],
    )
    dashboard = DashboardPage(driver)
    dashboard._open(path='/dashboard')
    dashboard.user_settings()
    settings = SettingsPage(driver)
    settings._open(path='/settings')
    settings.go_to_general()
    settings.enter_value_into_skype_field(skype)
    settings.enter_value_into_telegram_field(telegram)
    settings.save()
    toast = settings.find_element(BasePage.TOASTSUCCES)
    assert toast.is_displayed()
