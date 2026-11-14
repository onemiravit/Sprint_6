from urllib.parse import urlparse

import allure
from selenium.webdriver.support import expected_conditions as EC

from urls import URL
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from pages.order_page import OrderPage


class MainPage(BasePage):
    @allure.step("Открыть главную страницу Самоката")
    def open(self):
        self.driver.get(URL)
        return self.wait_until_home()

    @staticmethod
    def is_homepage_url(url):
        current_url = urlparse(url)
        expected_url = urlparse(URL)

        return (
            current_url.hostname == expected_url.hostname
            and current_url.path.rstrip("/") == ""
        )

    @allure.step("Дождаться главной страницы")
    def wait_until_home(self):
        self.wait.until(
            lambda driver: self.is_homepage_url(driver.current_url)
        )
        self.wait.until(
            EC.visibility_of_element_located(
                MainPageLocators.TOP_ORDER_BUTTON
            )
        )
        return self

    @allure.step("Нажать кнопку заказа: {entry_point}")
    def click_order_button(self, entry_point):
        locator = MainPageLocators.ORDER_BUTTONS.get(entry_point)
        if locator is None:
            raise ValueError(f"Неизвестная точка входа: {entry_point}")

        self.click(locator)
        return OrderPage(self.driver).wait_until_ready()

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

        question_text = self.wait_visible(question_locator).text.strip()
        self.click(question_locator)

        self.wait_visible(answer_locator)
        self.wait.until(
            lambda driver: bool(
                driver.find_element(*answer_locator).text.strip()
            )
        )

        answer_text = self.driver.find_element(*answer_locator).text.strip()
        return question_text, answer_text