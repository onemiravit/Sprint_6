import allure
from selenium.webdriver.support.ui import WebDriverWait

from pages.dzen_page import DzenPage
from pages.main_page import MainPage


class TestLogoNavigation:
    @allure.epic("Яндекс.Самокат")
    @allure.feature("Переходы по логотипам")
    @allure.title("Логотип Самоката открывает главную страницу")
    def test_scooter_logo_opens_homepage(self, driver):
        order_page = (
            MainPage(driver)
            .open()
            .click_order_button("top")
        )

        order_page.click_scooter_logo()
        MainPage(driver).wait_until_home()

        assert MainPage.is_homepage_url(driver.current_url)

    @allure.epic("Яндекс.Самокат")
    @allure.feature("Переходы по логотипам")
    @allure.title("Логотип Яндекса открывает Дзен в новом окне")
    def test_yandex_logo_opens_dzen_in_new_window(self, driver):
        main_page = MainPage(driver).open()
        original_handles = set(driver.window_handles)

        main_page.click_yandex_logo()

        new_handle = WebDriverWait(driver, 15).until(
            lambda current_driver: next(
                iter(
                    set(current_driver.window_handles)
                    - original_handles
                ),
                None,
            )
        )
        driver.switch_to.window(new_handle)

        dzen_page = DzenPage(driver).wait_until_homepage()

        assert dzen_page.is_homepage_url(driver.current_url)