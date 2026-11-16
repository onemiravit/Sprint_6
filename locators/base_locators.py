from selenium.webdriver.common.by import By


class BaseLocators:
    # Ссылка лого "Самокат"
    SCOOTER_LOGO = (
        By.CSS_SELECTOR,
        "a[class*='Header_LogoScooter']",
    )
    # Ссылка лого Яндекс
    YANDEX_LOGO = (
        By.CSS_SELECTOR,
        "a[class*='Header_LogoYandex']",
    )
