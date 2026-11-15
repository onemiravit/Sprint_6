import allure

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators.base_locators import BaseLocators


class BasePage:
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.timeout = timeout

    def _wait(self, condition, timeout=None):
        actual_timeout = (
            timeout if timeout is not None else self.timeout
        )
        return WebDriverWait(self.driver, actual_timeout).until(condition)

    def open_url(self, url):
        self.driver.get(url)

    def refresh_page(self):
        self.driver.refresh()

    def delete_all_cookies(self):
        self.driver.delete_all_cookies()

    def create_page(self, page_class):
        return page_class(self.driver)

    def get_current_url(self):
        return self.driver.current_url

    def get_window_handles(self):
        return self.driver.window_handles

    def switch_to_window(self, handle):
        self.driver.switch_to.window(handle)

    def wait_for_new_window(self, previous_handles, timeout=15):
        previous_handles = set(previous_handles)

        def find_new_handle(browser):
            new_handles = set(browser.window_handles) - previous_handles
            return next(iter(new_handles), False)

        return self._wait(find_new_handle, timeout)

    def wait_for_url(self, url_condition, timeout=30):
        def matching_url(browser):
            current_url = browser.current_url
            return current_url if url_condition(current_url) else False

        return self._wait(matching_url, timeout)

    def wait_visible(self, locator, timeout=None):
        return self._wait(
            EC.visibility_of_element_located(locator),
            timeout,
        )

    def wait_invisible(self, locator, timeout=None):
        return self._wait(
            EC.invisibility_of_element_located(locator),
            timeout,
        )

    def wait_for_text(self, locator, timeout=None):
        def get_visible_text(browser):
            element = browser.find_element(*locator)
            text = element.text.strip()

            if element.is_displayed() and text:
                return text

            return False

        return self._wait(get_visible_text, timeout)

    def wait_for_attribute_value(
        self,
        locator,
        attribute,
        expected_value,
        timeout=None,
    ):
        return self._wait(
            lambda browser: (
                browser.find_element(*locator)
                .get_attribute(attribute) == expected_value
            ),
            timeout,
        )

    @allure.step("Кликнуть по элементу")
    def click(self, locator):
        element = self._wait(
            EC.presence_of_element_located(locator)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element,
        )
        self._wait(
            EC.element_to_be_clickable(locator)
        ).click()

    @allure.step("Ввести текст в поле")
    def enter_text(self, locator, value):
        element = self.wait_visible(locator)
        element.clear()
        element.send_keys(str(value))

    def send_keys(self, locator, value):
        self.wait_visible(locator).send_keys(value)

    def get_text(self, locator):
        return self.wait_visible(locator).text.strip()

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