from selenium.webdriver.common.by import By


class DashboardPageLocators:
    USERDROPDOWN = (By.XPATH, r'//*[@data-e2e="userDropdown"]')
    ACCOUNTSETTINGS = (By.XPATH, r'//*[@data-e2e="userDropdown_accountSettings"]')
    LOGOUT = (By.XPATH, r'//*[@data-e2e="logout"]')
    PAYMENTSETTINGS = (By.XPATH, r'//*[@data-e2e="userDropdown_paymentSettings"]')
