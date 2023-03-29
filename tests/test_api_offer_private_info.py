import allure
import requests

from data.data import SOURCE


@allure.suite('[Pytest][API]')
@allure.title('Проверка, что пользователь не получает приватную информацию об оффере')
def test_api_offer_private_info():
    response = requests.get(url=SOURCE['API_URL'] + '/offer/info',
                            params={'api_key': 'dd5c335b9c756e371e3b31b9af14cec0', 'offer_id': '36067'})
    jsonData = response.json()
    assert response.status_code == 401
    assert jsonData['code'] == "error"
    assert jsonData['error'] == "Wrong api key, go away stranger!"
