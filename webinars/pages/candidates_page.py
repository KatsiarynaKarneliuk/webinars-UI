from .base_page import BasePage
from .locators import CandidatesPageLocators

class CandidatesPage(BasePage):
    def should_be_candidates_page(self):
        assert "candidates" in self.browser.current_url, "word \"candidates\" not in url"

    def check_previous_amount_candidates(self):
        previous_value = self.browser.find_element(*CandidatesPageLocators.TOTAL)
        previous_value = previous_value.text
        return previous_value

    def should_be_button_create_candidate(self):
        button_create_candidate = self.browser.find_element(*CandidatesPageLocators.CANDIDATE_CREATE_LINK)
        button=button_create_candidate.text
        assert button == "Создать кандидата", "Нет такой кнопки"

    def should_go_to_candidate_create_page(self):
        button_create_candidate = self.browser.find_element(*CandidatesPageLocators.CANDIDATE_CREATE_LINK)
        button_create_candidate.click()
        assert "candidates/create" in self.browser.current_url, "words \"candidates/create\" not in url"

    def should_message_appeares(self):
        succses_message = self.browser.find_element(*CandidatesPageLocators.SUCСES_MESSAGE)
        assert succses_message == "Данные сохранены", "there is not any succses_message"

    def check_next_amount_candidates(self):
        next_value = self.browser.find_element(*CandidatesPageLocators.TOTAL)
        next_value = next_value.text
        return next_value

    def compare_previous_next_amount_candidates(self,previous_value,next_value):
        assert previous_value != next_value, "the value didn't change"