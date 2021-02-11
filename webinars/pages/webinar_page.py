from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import WebinarPageLocators

class WebinarPage(BasePage):
    def should_go_to_statistic_page(self):
        statistic_page_link = self.browser.find_element(*WebinarPageLocators.TAB_STATISTIC)
        statistic_page_link.click()
        assert "statistics" in self.browser.current_url, "word \"statistics\" not in url"
