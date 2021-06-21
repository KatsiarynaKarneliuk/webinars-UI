import time
from pages.webinar_page import WebinarPage
from pages.statistic_page import StatisticPage
from pages.login_page import LoginPage

class TestLoginWebinar:
    def test_is_it_webinar_page(self,browser,open_login_page):
        open_login_page.login_by_email("tcekrqytb@emlpro.com","123456")
        time.sleep(20)
        WebinarPage(browser).should_be_webinar_page()

    def test_name_in_header(self,browser,open_login_page):
        open_login_page.login_by_email("tcekrqytb@emlpro.com", "123456")
        time.sleep(20)
        WebinarPage(browser).should_be_name_in_header()



    def test_user_can_go_to_statistic_page_from_webinar_page(self,browser,open_login_page):
        open_login_page.login_by_email("tcekrqytb@emlpro.com", "123456")
        WebinarPage(browser).should_go_to_statistic_page()
