import time
import pytest
from selenium.webdriver.common.keys import Keys
from .pages.statistic_page import StatisticPage
from .pages.webinar_page import WebinarPage
from .pages.reg_by_video_page import RegByVideoPage

class TestLoginStatistic:
    def test_is_statistic_page(self,browser,open_login_page):
        open_login_page.login_by_email("tcekrqytb@emlpro.com", "123456")
        WebinarPage(browser).should_go_to_statistic_page()
        time.sleep(20)
        StatisticPage(browser).should_be_statistic_page()

    @pytest.mark.xfail
    def test_value_changed(self, browser, open_login_page, originalWindow=None):
        open_login_page.login_by_email("tcekrqytb@emlpro.com", "123456")
        WebinarPage(browser).should_go_to_statistic_page()
        time.sleep(10)
        StatisticPage(browser).save_previous_value()
        browser.current_window_handle
        time.sleep(10)
        browser.switch_to.window('tab')
        time.sleep(10)
        reg_page = RegByVideoPage(browser)
        link = "https://video.dev.online.vertera.org/ru/sign-in/lending_o_biznese/11"
        reg_page.open(link)
        RegByVideoPage(browser).reg_by_video("test","+79523215485","dfg@gmail.com")
        time.sleep(20)
        browser.close();
        browser.switchTo().window(originalWindow);
        open_login_page.login_by_email("tcekrqytb@emlpro.com", "123456")
        WebinarPage(browser).should_go_to_statistic_page()
        StatisticPage(browser).save_next_value()
        StatisticPage(browser).compare_prevoius_next_value()






