import os
from contextlib import suppress

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from urls import URL
from locators.main_page_locators import MainPageLocators


def prepare_page_before_test(browser):
    """Открыть сайт, удалить старые cookies и принять уведомление."""

    browser.get(URL)

    # Сначала удаляем старые cookies на открытом домене.
    browser.delete_all_cookies()

    # Обновляем страницу, чтобы сайт загрузился уже без старых cookies.
    browser.refresh()

    wait = WebDriverWait(browser, 15)

    # Принимаем уведомление о cookies.
    wait.until(
        EC.element_to_be_clickable(
            MainPageLocators.COOKIE_ACCEPT_BUTTON
        )
    ).click()

    # Ждём, когда главная страница будет готова к тесту.
    wait.until(
        EC.visibility_of_element_located(
            MainPageLocators.TOP_ORDER_BUTTON
        )
    )


@pytest.fixture
def driver():
    options = webdriver.FirefoxOptions()
    options.add_argument("--window-size=1440,1000")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")

    
    browser = webdriver.Firefox(options=options)
    browser.implicitly_wait(0)

    try:
        prepare_page_before_test(browser)
        yield browser
    finally:
        browser.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        browser = item.funcargs.get("driver")
        if browser is not None:
            with suppress(Exception):
                allure.attach(
                    browser.get_screenshot_as_png(),
                    name="screenshot-on-failure",
                    attachment_type=allure.attachment_type.PNG,
                )