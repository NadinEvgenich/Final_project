from selenium.webdriver.common.by import By


class OfferdetailPageLocators:
    TRACKINGURL = (By.XPATH, r'//*[@data-e2e="inp_tracking_url"]')
    REQUESTBTN = (By.XPATH, r'//*[@data-e2e="btn_requset-approve"]')
    TEXTAREA = (By.XPATH, r'//*[@data-e2e="requestDescription"]')
    SENDBTN = (By.XPATH, r'//*[@data-e2e="btn_send-request"]')
