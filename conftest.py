import pytest
import logging

from data.data import SOURCE
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener

logging.basicConfig(filename="selenium.log",
                    format='%(asctime)s:%(levelname)s:%(name)s - %(message)s',
                    encoding='utf-8',
                    datefmt='%m/%d/%Y %I:%M:%S',
                    level=logging.INFO
                    )


class Listener(AbstractEventListener):
    logger = logging.getLogger('ListenerLoger')


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", choices=["chrome", "firefox", "MicrosoftEdge"],
                     help="Choose browser")
    parser.addoption("--bversion", default="110.0", help="Choose browser version")
    parser.addoption("--headless", action="store_true",
                     help="Enter --headless option if you don\'t want to see browser during a test")
    parser.addoption("--remote", action="store_true", help="Enter --remote if you want to execute remote server")
    parser.addoption("--executor", default="localhost", help="Enter executor url for remote run")
    parser.addoption("--enable_vnc", action="store_true",
                     help="Enter --enable_vnc if you want to see browser during the test")


@pytest.fixture()
def driver(request):
    browser = request.config.getoption("--browser")
    version = request.config.getoption("--bversion")
    headless = request.config.getoption("--headless")
    remote = request.config.getoption("--remote")
    executor = request.config.getoption("--executor")
    vnc = request.config.getoption("--enable_vnc")
    logger = logging.getLogger("BrowserLogger")
    test_name = request.node.name

    if browser not in ["chrome", "firefox", "edge", "MicrosoftEdge"]:
        raise AssertionError('This browser is not supported.')

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
        driver = EventFiringWebDriver(webdriver.Chrome(options=options), Listener())
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        driver = EventFiringWebDriver(webdriver.Firefox(options=options), Listener())
    else:
        options = webdriver.EdgeOptions()
        driver = EventFiringWebDriver(webdriver.Edge(options=options), Listener())

    if remote:
        capabilities = {
            "browserName": browser,
            "browserVersion": version,
            "selenoid:options": {
                "enableVNC": vnc
            },
            "name": "Capricornio"
        }
        driver = EventFiringWebDriver(webdriver.Remote(
            command_executor=f"{executor}:4444/wd/hub",
            desired_capabilities=capabilities,
            options=options
        ), Listener())
        logger.info("Test {} started with {} {}".format(test_name, browser, version))

    def fin():
        driver.quit()
        logger.info("Browser {} closed".format(browser))
        logger.info("Test {} finished".format(test_name))
    request.addfinalizer(fin)

    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.base_url = SOURCE['BASE_URL']
    return driver
