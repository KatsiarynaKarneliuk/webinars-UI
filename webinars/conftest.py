import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from .pages.locators import LoginPageLocators
from .pages.login_page import LoginPage
from .pages.reg_by_video_page import RegByVideoPage


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")

    parser.addoption('--language', action='store', default="None",
                     help="Choose language: ru, en ...(etc.)")

    parser.addoption('--pause', action='store', default=0, help="Включение паузы после загрузки")

@pytest.fixture(scope="session")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    if (browser_name == "chrome"):
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.fixture(scope='module')
def open_login_page(browser):
    login_page = LoginPage(browser)
    link = "https://dev.online.vertera.org/sign-in"
    login_page.open(link)
    return login_page

@pytest.fixture(scope='module')
def open_reg_page(browser):
    reg_page = RegByVideoPage(browser)
    link = "https://video.dev.online.vertera.org/ru/sign-in/lending_o_biznese/11"
    reg_page.open(link)
    return reg_page




"""@pytest.fixture(scope='module')
def login():
    d = webdriver.Chrome()
    d.get("https://dev.online.vertera.org/sign-in")
    email = d.find_element_by_css_selector("#mat-input-0")
    password = d.find_element_by_css_selector("#mat-input-1")
    email.send_keys("test11@email.com")
    password.send_keys("123456")
    d.find_element_by_css_selector(".btn-yellow").click()
    yield d
    d.quit()"""




