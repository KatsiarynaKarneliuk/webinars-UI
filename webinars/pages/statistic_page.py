from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import StatisticPageLocators


class StatisticPage(BasePage):
    def should_be_chart_block(self):
        assert self.is_element_present(*StatisticPageLocators.CHART_BLOCK), \
            'CHART_BLOCK is not presented, but should  be'

    def should_be_countViewLanding(self):
        assert self.is_element_present(*StatisticPageLocators.CHART_COUNT), \
            'CHART_COUNT is not presented, but should  be'

    def should_be_nameViewLanding(self):
        assert self.is_element_present(*StatisticPageLocators.CHART_NAME), \
            'CHART_NAME is not presented, but should  be'

    def should_be_percentViewLanding(self):
        assert self.is_element_present(*StatisticPageLocators.CHART_PERCENT), \
            'CHART_PERCENT is not presented, but should  be'
