import time
from .base_page import BasePage
from .locators import RegByVideoLocators

class RegByVideoPage(BasePage):
    def should_be_reg_form(self):
        assert self.is_element_present(*RegByVideoLocators.REG_FORM)

    def reg_by_video(self, name, phone, email):
        name_field = self.browser.find_element(*RegByVideoLocators.NAME)
        name_field.send_keys(name)
        email_field = self.browser.find_element(*RegByVideoLocators.EMAIL_FIELD)
        email_field.send_keys(email)
        phone_field = self.browser.find_element(*RegByVideoLocators.PHONE_FIELD)
        phone_field.send_keys(phone)
        button = self.browser.find_element(*RegByVideoLocators.LOGIN_SUBMIT)
        button.click()
        time.sleep(15)