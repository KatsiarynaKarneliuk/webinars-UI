from selenium.webdriver.common.by import By

class BasePageLocators():
   pass

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#auth__form")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#mat-input-0")
    PHONE_FIELD = (By.CSS_SELECTOR, "#phone")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#mat-input-1")
    LOGIN_SUBMIT = (By.NAME, ".btn btn-yellow")

class WebinarPageLocators():
    TAB_STATISTIC = (By.CSS_SELECTOR, ".tabs  .tab-header__item span ")
    CHART = (By.CSS_SELECTOR, ".legend")
    CHART_BLOCK = (By.CSS_SELECTOR, "#legend__item-0")
    CHART_PERCENT = (By.CSS_SELECTOR, ".legend__item--value")
    CHART_NAME = (By.CSS_SELECTOR, ".legend__item--name")
    GO_TO_STATISTIC = (By.CSS_SELECTOR, ".vebinar__aside--menu--item active   a ")

class StatisticPageLocators():
    CHART_BLOCK = (By.CSS_SELECTOR, "#id-179")
    CHART_NAME = (By.CSS_SELECTOR, "#legends__item-0 .legend__item--name")
    CHART_COUNT = (By.CSS_SELECTOR, "#legends__item-0 .legends__item - -value")
    CHART_PERCENT = (By.CSS_SELECTOR, "#legends__item-0 .legends__item - -value span")
