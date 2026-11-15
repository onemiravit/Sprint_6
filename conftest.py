import pytest
from selenium import webdriver

from browser_setup import prepare_page_before_test
from selenium.webdriver.firefox.options import Options


@pytest.fixture
def driver():
    # Создаём отдельный браузер для текущего теста.
    browser = webdriver.Firefox()

    try:
        prepare_page_before_test(browser)

        # Передаём браузер тесту.
        yield browser
    finally:
        # Закрываем браузер после завершения теста.
        browser.quit()

    