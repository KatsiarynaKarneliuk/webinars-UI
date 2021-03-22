from selenium.webdriver.common.by import By

class BasePageLocators():
   pass

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, ".auth__form")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#mat-input-0")
    PHONE_FIELD = (By.CSS_SELECTOR, "#phone")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#mat-input-1")
    LOGIN_SUBMIT = (By.CSS_SELECTOR, ".btn-yellow")

class RegByVideoLocators():
    REG_FORM = (By.CSS_SELECTOR, ".sign-in__form")
    NAME = (By.CSS_SELECTOR, "#mat-input-0")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#mat-input-1")
    PHONE_FIELD = (By.CSS_SELECTOR, "#phone")
    LOGIN_SUBMIT = (By.CSS_SELECTOR, ".btn-yellow")

class WebinarPageLocators():
    NAME=(By.CSS_SELECTOR,".mat-menu-trigger.vebinar__header--user--name")
    GO_TO_STATISTIC = (By.XPATH, "/html/body/app-root/app-wrapper/div/div[1]/div[2]/a[3]/span[2]")


class StatisticPageLocators():
    CHART_BLOCK = (By.CSS_SELECTOR, "#id-179")
    CHART_NAME = (By.CSS_SELECTOR, "#legends__item-1 .legend__item--name")
    CHART_COUNT = (By.XPATH, '//div[@id="legends__item-1"]/descendant::span')
    CHART_PERCENT = (By.XPATH, '//div[@id="legends__item-1"]/child')