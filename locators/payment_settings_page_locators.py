from selenium.webdriver.common.by import By


class PaymentSettingPageLocators:
    TRON = (By.XPATH, './/span[@class="p-tabview-title ng-star-inserted" and text()="USDT TRON"]')
    USDTADDRESS = (By.XPATH, r'//*[@data-e2e="usdt-tron-adderess_0"]')
    COMMENT = (By.XPATH, r'//*[@data-e2e="usdt-tron-comment_0"]')
    SAVEBTN =(By.XPATH, r'//*[@data-e2e="btn_usdt-tron-save_0"]')
