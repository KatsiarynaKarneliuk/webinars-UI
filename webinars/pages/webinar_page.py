from .base_page import BasePage
from .locators import WebinarPageLocators

class WebinarPage(BasePage):
    def should_be_webinar_page(self):
        assert "webinars" in self.browser.current_url, "word \"webinars\" not in url"

    def should_be_name_in_header(self):
        name_in_header = self.browser.find_element(*WebinarPageLocators.NAME)
        name=name_in_header.text
        assert name =="Имя291946 Фамилия291946", "name is not found"

    def should_go_to_statistic_page(self):
        statistic_page_link = self.browser.find_element(*WebinarPageLocators.GO_TO_STATISTIC)
        statistic_page_link.click()

    def should_go_to_candidates_page(self):
        candidates_page_link = self.browser.find_element(*WebinarPageLocators.GO_TO_CANDIDATES)
        candidates_page_link.click()
