from urllib.parse import urlparse

import allure
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage


class DzenPage(BasePage):
    @staticmethod
    def is_homepage_url(url):
        parsed = urlparse(url)
        host = parsed.hostname or ""

        return (
            (host == "dzen.ru" or host.endswith(".dzen.ru"))
            and parsed.path.rstrip("/") == ""
        )

    @allure.step("Дождаться главной страницы Дзена")
    def wait_until_homepage(self):
        WebDriverWait(self.driver, 30).until(
            lambda driver: self.is_homepage_url(driver.current_url)
        )
        return self