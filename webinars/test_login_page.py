
from .pages.login_page import LoginPage
from .pages.webinar_page import WebinarPage

def test_user_can_login(browser):
    link = "https://dev.online.vertera.org/sign-in"
    page = LoginPage(browser)
    page.open(link)
    email = "test11@email.com"
    password = "123456"
    page.should_be_login_form()
    page.login_by_email(email,password)
    webinar_page = WebinarPage(browser)
    webinar_page.should_be_webinar_page()
