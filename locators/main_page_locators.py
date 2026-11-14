from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопка "Заказать" вверху сайта
    TOP_ORDER_BUTTON = (
        By.XPATH,
        "(//button[normalize-space(.)='Заказать'])[1]",
    )
    # Кнопка "Заказать" внизу сайта
    BOTTOM_ORDER_BUTTON = (
        By.XPATH,
        "(//button[normalize-space(.)='Заказать'])[last()]",
    )
    # Кнопка куки
    COOKIE_ACCEPT_BUTTON = (
        By.XPATH,
        "//button[text()= 'да все привыкли']",
    )
    
    ORDER_BUTTONS = {
        "top": TOP_ORDER_BUTTON,
        "bottom": BOTTOM_ORDER_BUTTON,
    }
    # Раздел вопросы
    # Ссылки навопросы
    FAQ_QUESTION = (By.ID, "accordion__heading-{}")
    # Ссылки на ответы
    FAQ_ANSWER = (By.ID, "accordion__panel-{}")
    