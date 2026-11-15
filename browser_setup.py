from pages.main_page import MainPage


def prepare_page_before_test(browser):
    page = MainPage(browser)

    page.open()
    page.delete_all_cookies()
    page.refresh_page()
    page.wait_until_home()
    page.accept_cookie_banner()
    