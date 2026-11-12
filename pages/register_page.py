from pages.base_page import BasePage
from locators.register_page_locators import RegisterPageLocators
from utils import Utils

class RegisterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def register(self):
        generated_name = Utils.generate_name()
        generated_email = Utils.generate_email()

        self.find_element_with_wait(RegisterPageLocators.NAME_FIELD).send_keys(generated_name)
        self.find_element_with_wait(RegisterPageLocators.EMAIL_FIELD).send_keys(generated_email)
        self.find_element_with_wait(RegisterPageLocators.PASSWORD_FIELD).send_keys("123456")
        self.click_element_with_wait(RegisterPageLocators.REGISTER_BUTTON)
        