from selenium.webdriver.common.by import By


class OffersPageLocators:
    SEARCH = (By.XPATH, r'//*[@name="searchOffer"]')
    SELECTACCESS = (By.XPATH, r'//*[@name="access"]')
    APPLYBTN = (By.XPATH, r'//*[@data-e2e="apply"]')
    OFFERTABLE = (By.XPATH, '//table/tbody/tr/td[1]/div')
