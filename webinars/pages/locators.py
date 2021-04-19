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
    GO_TO_CANDIDATES = (By.XPATH, '//a[contains(@href, "/ru/cabinet/candidates")]')

class StatisticPageLocators():
    CHART_BLOCK = (By.CSS_SELECTOR, "#id-179")
    CHART_NAME = (By.CSS_SELECTOR, "#legends__item-1 .legend__item--name")
    CHART_COUNT = (By.XPATH, '//div[@id="legends__item-1"]/descendant::span')
    CHART_PERCENT = (By.XPATH, '//div[@id="legends__item-1"]/child')

class CandidatesPageLocators():
    CANDIDATE_CREATE_LINK = (By.XPATH,'//span[text() = "Создать кандидата"]')
    SUCСES_MESSAGE = (By.XPATH,'//span[text() = "Данные сохранены"]')
    TOTAL = (By.XPATH,'//*[@class="statistics_container"]/div[1]/span[2]')

class handCandidateCreatePageLocators():
    LNAME = (By.XPATH,'//input[@formcontrolname="lname"]')
    FNAME = (By.XPATH,'//input[@formcontrolname="fname"]')
    COUNTRY = (By.XPATH,'//input[@formcontrolname="countryName"]')
    CITY = (By.XPATH,'//input[@formcontrolname="cityName"]')
    PHONE = (By.CSS_SELECTOR,"#phone")
    MAINPHONE = (By.XPATH,'//span[text()="Основной"]')
    EMAIL = (By.XPATH,'//input[@type="email"]')
    COMMENT = (By.XPATH,'//textarea[@formcontrolname="comment"]')
    REG_WEB =(By.CSS_SELECTOR,'.registration__select')
    SELECTED_WEBINAR = (By.XPATH,'//span[contains(text(),"Как начать бизнес на Эко-продуктах")]')
    SAVE_BUTTON = (By.XPATH, '//button[text()="Сохранить"]')

