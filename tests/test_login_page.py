import allure

from data.data import WEB
from pages.DashboardPage import DashboardPage
from pages.LoginPage import LoginPage


@allure.suite('[Pytest][UI]')
@allure.title('Проверка корректной авторизации')
def test_login(driver):
    login_page = LoginPage(driver)
    login_page._open(path='/login')

    login_page._login(
        email=WEB['email'],
        password=WEB['password'],
    )
    dashboard = DashboardPage(driver)
    dashboard._open(path='/dashboard')
    assert 'dashboard' in driver.current_url, 'Ошибка авторизации!'

    dashboard._open(path='/dashboard')
    user = dashboard.get_username()
    assert user.text.strip() == 'TestTestov'


@allure.suite('[Pytest][UI]')
@allure.title('Проверка ошибки авторизации пользователя')
def test_login_wrong(driver):
    login_page = LoginPage(driver)
    login_page._open(path='/login')

    login_page._login(
        email=WEB['email'],
        password=WEB['wrong_password'],
    )
    error = login_page.error_login()
    assert error.text == 'Invalid login/password'


@allure.suite('[Pytest][UI]')
@allure.title('Проверка выхода из личного кабинета')
def test_logout(driver):
    login_page = LoginPage(driver)
    login_page._open(path='/login')

    login_page._login(
        email=WEB['email'],
        password=WEB['password'],
    )
    dashboard = DashboardPage(driver)
    dashboard._open(path='/dashboard')
    dashboard._logout()
    logout_page = LoginPage(driver)
    logout_page._open(path='/login')
    assert 'login' in driver.current_url, 'Ошибка выхода из аккаунта!'
