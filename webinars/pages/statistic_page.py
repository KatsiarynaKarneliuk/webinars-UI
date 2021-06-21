from .base_page import BasePage
from .locators import StatisticPageLocators


class StatisticPage(BasePage):
    stat_parameter_name=StatisticPageLocators
    def should_be_statistic_page(self):
        assert "statistics" in self.browser.current_url, "word \"statistics\" not in url"

    def get_current_value(self, stat_parameter_name):
        current_value = self.browser.find_elements(stat_parameter_name).text
        return current_value

    def get_next_value(self,stat_parameter_name):
        next_value =self.browser.find_element(stat_parameter_name).text
        return next_value

    def compare(self,current_value,next_value):
        assert self.get_current_value(current_value)<self.get_current_value(next_value)










