import logging
import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = driver.base_url
        self.logger = logging.getLogger(type(self).__name__)

    page_loader_css_class: str = None
    table_loader_css_class: str = None
    TOASTSUCCES = (By.CSS_SELECTOR,
                   '.ng-tns-c104-0.ng-trigger.ng-trigger-toastState.adc-toast.adc-toast-success.ng-star-inserted')
    TOASTERROR = (By.CSS_SELECTOR,
                  '.ng-tns-c104-0.ng-trigger.ng-trigger-toastState.adc-toast.adc-toast-error.ng-star-inserted')

    @allure.step("Открыть страницу {path}")
    def _open(self, path=''):
        self.logger.info("Открыта страница: {self.base_url} + path")
        try:
            self.driver.get(self.base_url + path)
        except Exception:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                'Screenshot',
                attachment_type=allure.attachment_type.PNG,
            )
            assert False, f"Не удалось открыть страницу {self.base_url + path}"

    @allure.step("Найти элемент с локатором {locator}")
    def find_element(self, locator):
        self.logger.info(f"Найден элемент с {locator}")
        try:
            return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                'Screenshot',
                attachment_type=allure.attachment_type.PNG,
            )
            assert False, f"Элемент с локатором {locator} не был найден."

    @allure.step("Получаю элемент с локатором {locator}")
    def get_element(self, locator):
        self.logger.info(f"Получен элемент с {locator}")
        return self.find_element(locator)

    @allure.step("Заполнить поле с локатором {locator} значением {value}")
    def fill_edit_field(self, locator, value):
        try:
            _input = self.find_element(locator)
            _input.click()
            _input.clear()
            _input.send_keys(value)
        except Exception as ex:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                'Screenshot',
                attachment_type=allure.attachment_type.PNG,
            )
            assert False, f"Во время ввода значения '{value}' в поле с локатором '{locator}' возникла ошибка: '{ex}'"

    @allure.step("Ожидание для клика по элементу с {locator}")
    def clickwait_element(self, locator):
        self.logger.info(f"По элементу с {locator} можно кликнуть")
        try:
            return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                'Screenshot',
                attachment_type=allure.attachment_type.PNG,
            )
            assert False, f"По элементу с локатором {locator} нельзя кликнуть."

    @allure.step("Ожидание для исчезновения лоадэра")
    def wait_loader_not_visible(self) -> None:
        if self.page_loader_css_class:
            WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located(
                (By.CLASS_NAME, self.page_loader_css_class)
            )
            )

    @allure.step("Ожидание для исчезновения лоадэра таблицы")
    def wait_tableloader_not_visible(self) -> None:
        if self.table_loader_css_class:
            WebDriverWait(self.driver, 20).until(
                EC.invisibility_of_element_located(
                    (By.CLASS_NAME, self.table_loader_css_class)
                )
            )
