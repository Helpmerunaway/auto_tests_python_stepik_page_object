from .base_page import BasePage
from code.pages.locators import LoginPageLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Wrong url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL_INPUT), "Login input form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL_INPUT), "Register input form is not presented"

    """  
    def should_be_login_form2(self):
        login_input = self.browser.find_element(By.ID, "id_login-username").text
        assert login_input in self.browser.current_url, "No login email input"
    """