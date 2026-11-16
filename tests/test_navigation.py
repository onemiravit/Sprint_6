import allure

from pages.dzen_page import DzenPage
from pages.main_page import MainPage


class TestLogoNavigation:
    @allure.epic("Яндекс.Самокат")
    @allure.feature("Переходы по логотипам")
    @allure.title("Логотип Самоката открывает главную страницу")
    def test_scooter_logo_opens_homepage(self, driver):
        main_page = MainPage(driver).open()
        order_page = main_page.click_order_button("top")

        order_page.click_scooter_logo()
        actual_url = main_page.wait_until_home()

        assert MainPage.is_homepage_url(actual_url)

    @allure.epic("Яндекс.Самокат")
    @allure.feature("Переходы по логотипам")
    @allure.title("Логотип Яндекса открывает Дзен в новом окне")
    def test_yandex_logo_opens_dzen_in_new_window(self, driver):
        main_page = MainPage(driver).open()
        previous_handles = main_page.get_window_handles()

        main_page.click_yandex_logo()
        new_handle = main_page.wait_for_new_window(previous_handles)
        main_page.switch_to_window(new_handle)

        dzen_page = main_page.create_page(DzenPage)
        actual_url = dzen_page.wait_until_homepage()

        assert DzenPage.is_homepage_url(actual_url)