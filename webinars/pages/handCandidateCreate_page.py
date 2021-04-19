from .base_page import BasePage
from .locators import handCandidateCreatePageLocators
from faker import Faker
import time

faker = Faker()


class handCandidateCreatePage(BasePage):

    def should_be_handCandidateCreate_page(self):
        assert "candidates/create" in self.browser.current_url, "word \"candidates/create\" not in url"

    def can_fill_create_form(self):
        lname = self.browser.find_element(*handCandidateCreatePageLocators.LNAME)
        lname.send_keys(faker.name())
        fname = self.browser.find_element(*handCandidateCreatePageLocators.FNAME)
        fname.send_keys(faker.name())
        countryName = self.browser.find_element(*handCandidateCreatePageLocators.COUNTRY)
        countryName.send_keys("Russia")
        cityName = self.browser.find_element(*handCandidateCreatePageLocators.CITY)
        cityName.send_keys("Москва")
        phone = self.browser.find_element(*handCandidateCreatePageLocators.PHONE)
        phone.send_keys("9529526565")
        checkMainPhone = self.browser.find_element(*handCandidateCreatePageLocators.MAINPHONE)
        checkMainPhone.click()
        mainEmail = self.browser.find_element(*handCandidateCreatePageLocators.EMAIL)
        mainEmail.send_keys("dfd@gmail.com")
        comment =self.browser.find_element(*handCandidateCreatePageLocators.COMMENT)
        comment.send_keys("some text")
        reg_web_field =self.browser.find_element(*handCandidateCreatePageLocators.REG_WEB)
        reg_web_field.click()
        selected_webinar =self.browser.find_element(*handCandidateCreatePageLocators.SELECTED_WEBINAR)
        selected_webinar.click()

    def save_hand_candidate(self):
        save_button = self.browser.find_element(*handCandidateCreatePageLocators.SAVE_BUTTON)
        save_button.click()
        time.sleep(3)


