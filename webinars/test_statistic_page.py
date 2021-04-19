import time
from .pages.statistic_page import StatisticPage
from .pages.webinar_page import WebinarPage
from .pages.reg_by_video_page import RegByVideoPage

class TestLoginStatistic:
    def test_is_statistic_page(self,browser,open_login_page):
        open_login_page.login_by_email("tcekrqytb@emlpro.com", "123456")
        WebinarPage(browser).should_go_to_statistic_page()
        time.sleep(20)
        StatisticPage(browser).should_be_statistic_page()


    def test(self, browser,open_login_page):
        open_login_page.login_by_email("tcekrqytb@emlpro.com", "123456")
        WebinarPage(browser).should_go_to_statistic_page()
        time.sleep(3)
        StatisticPage(browser).save_previous_value()
        browser.execute_script("window.open()")
        window_after = browser.window_handles[1]
        browser.switch_to_window(window_after)
        time.sleep(3)
        reg_page = RegByVideoPage(browser)
        link = "https://video.dev.online.vertera.org/ru/sign-in/lending_o_biznese/11"
        reg_page.open(link)
        RegByVideoPage(browser).reg_by_video("test", "+79523215485", "dfg@gmail.com")
        time.sleep(3)
        window_before = browser.window_handles[0]
        browser.switch_to_window(window_before)
        browser.refresh()
        time.sleep(3)
        StatisticPage(browser).save_next_value()
        StatisticPage(browser).compare_prevoius_next_value('previous_value','next_value')





