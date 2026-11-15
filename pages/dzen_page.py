from urllib.parse import urlparse

import allure

from pages.base_page import BasePage


class DzenPage(BasePage):
    @staticmethod
    def is_homepage_url(url):
        parsed_url = urlparse(url)
        hostname = parsed_url.hostname or ""

        return (
            (hostname == "dzen.ru" or hostname.endswith(".dzen.ru"))
            and parsed.path.rstrip("/") == ""
        )

    @allure.step("Дождаться главной страницы Дзена")
    def wait_until_homepage(self):
        
        return self.wait_for_url(self.is_homepage_url, timeout=30)