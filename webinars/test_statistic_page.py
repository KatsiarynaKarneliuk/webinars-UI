import pytest
from .pages.statistic_page import StatisticPage

def test_user_can_see_chart_on_statistic_page(browser):
    link = "link=https://dev.online.vertera.org/statistics"
    page = StatisticPage(browser, link)
    page.open()
    page.should_be_chart_block()

def test_user_can_see_nameViewLanding(browser):
    link = "link=https://dev.online.vertera.org/statistics"
    page = StatisticPage(browser, link)
    page.open()
    page.should_be_nameViewLanding()

def test_user_can_see_countViewLanding(browser):
    link = "link=https://dev.online.vertera.org/statistics"
    page = StatisticPage(browser, link)
    page.open()
    page.should_be_countViewLanding()

def user_can_see_percentViewLanding(browser):
    link = "link=https://dev.online.vertera.org/statistics"
    page = StatisticPage(browser, link)
    page.open()
    page.should_be_percentViewLanding()


