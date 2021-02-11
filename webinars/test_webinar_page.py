import pytest
from .pages.login_page import LoginPage
from .pages.webinar_page import WebinarPage
from .pages.statistic_page import StatisticPage

def test_user_can_go_to_statistic_page_from_webinar_page(browser):
    link = "https://dev.online.vertera.org/cabinet/webinars"
    page = WebinarPage(browser, link)
    page.open()
    page.should_be_statistic_link()
    page.go_to_statistic_page()
    statistic_page = StatisticPage(browser, browser.current_url)
    statistic_page.should_be_statistic_page()