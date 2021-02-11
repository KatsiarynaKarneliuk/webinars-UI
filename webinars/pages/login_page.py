from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_login_by_email()
        self.should_go_webinar_page()

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented" # символ *, он указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать.

    def should_login_by_email(self,email, password):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        password_field.send_keys(password)
        button =self.browser.find_element(*LoginPageLocators.LOGIN_SUBMIT)
        button.click()

    def should_go_webinar_page(self):
        assert "webinars" in self.browser.current_url, "word \"webinars\" not in url"

