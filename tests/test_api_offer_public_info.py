import allure
import requests

from data.data import SOURCE


@allure.suite('[Pytest][API]')
@allure.title('Проверка, что пользователь получает публичную информацию об оффере')
def test_api_offer_public_info():
    response = requests.get(url=SOURCE['API_URL'] + '/offer/public_info')
    res_json = response.json()
    assert response.status_code == 200
    assert res_json['offers'][0]['id'] == 36067
