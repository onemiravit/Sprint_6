from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_on_account_button(self):
        self.click_element_with_wait(HomePageLocators.ACCOUNT_BUTTON)
