from .base_page import BasePage
from .locators import StatisticPageLocators


class StatisticPage(BasePage):
    def should_be_statistic_page(self):
        assert "statistics" in self.browser.current_url, "word \"statistics\" not in url"

    def save_previous_value(self):
        previous_chart_count = self.browser.find_element(*StatisticPageLocators.CHART_COUNT)
        previous_value = previous_chart_count.text
        return previous_value

    def save_next_value(self):
        next_chart_count = self.browser.find_element(*StatisticPageLocators.CHART_COUNT)
        next_value = next_chart_count.text
        return next_value

    def compare_prevoius_next_value(self,previous_value,next_value):
        assert previous_value != next_value, "the value didn't change"





