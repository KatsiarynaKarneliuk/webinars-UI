import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage

def test_user_can_login(browser):
    link = "https://dev.online.vertera.org/sign-in"
    page = LoginPage(browser, link)
    page.open()
    email="test11@email.com"
    password = "123456"
    page.should_be_login(email,password)