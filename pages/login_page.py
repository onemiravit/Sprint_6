from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_on_registration_button(self):
        self.click_element_with_wait(LoginPageLocators.REGISTRATION_BUTTON)
