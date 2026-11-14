import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators.base_locators import BaseLocators


class BasePage:
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @allure.step("Кликнуть по элементу")
    def click(self, locator):
        element = self.wait.until(
            EC.presence_of_element_located(locator)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element,
        )
        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()

    @allure.step("Заполнить поле")
    def enter_text(self, locator, value):
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(str(value))

    @allure.step("Дождаться видимости элемента")
    def wait_visible(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    @staticmethod
    def format_locator(locator_template, value):
        return (
            locator_template[0],
            locator_template[1].format(value),
        )

    @allure.step("Нажать на логотип Самоката")
    def click_scooter_logo(self):
        self.click(BaseLocators.SCOOTER_LOGO)

    @allure.step("Нажать на логотип Яндекса")
    def click_yandex_logo(self):
        self.click(BaseLocators.YANDEX_LOGO)