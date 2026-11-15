from urllib.parse import urlparse

import allure

from urls import URL
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from pages.order_page import OrderPage


class MainPage(BasePage):
    def open(self):
        self.open_url(URL)
        self.wait_until_home()
        return self

    @staticmethod
    def is_homepage_url(url):
        current = urlparse(url)
        expected = urlparse(URL)

        return (
            current.hostname == expected.hostname
            and current.path.rstrip("/") == ""
        )

    def wait_until_home(self):
        homepage_url = self.wait_for_url(self.is_homepage_url)
        self.wait_visible(MainPageLocators.TOP_ORDER_BUTTON)
        return homepage_url

    def accept_cookie_banner(self):
        self.click(MainPageLocators.COOKIE_ACCEPT_BUTTON)
        self.wait_invisible(MainPageLocators.COOKIE_ACCEPT_BUTTON)

    @allure.step("Открыть ответ FAQ с индексом {index}")
    def expand_faq(self, index):
        question_locator = self.format_locator(
            MainPageLocators.FAQ_QUESTION,
            index,
        )
        answer_locator = self.format_locator(
            MainPageLocators.FAQ_ANSWER,
            index,
        )

        question_text = self.get_text(question_locator)
        self.click(question_locator)
        answer_text = self.wait_for_text(answer_locator)

        return question_text, answer_text

    def click_order_button(self, entry_point):
        locator = MainPageLocators.ORDER_BUTTONS.get(entry_point)
        if locator is None:
            raise ValueError(f"Неизвестная точка входа: {entry_point}")

        self.click(locator)
        return self.create_page(OrderPage).wait_until_ready()