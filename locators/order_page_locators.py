from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Поле Имя
    FIRST_NAME_INPUT = (
        By.CSS_SELECTOR,
        "input[placeholder='* Имя']",
    )
    # Поле Фамилия
    LAST_NAME_INPUT = (
        By.CSS_SELECTOR,
        "input[placeholder='* Фамилия']",
    )
    # Поле адрес
    ADDRESS_INPUT = (
        By.CSS_SELECTOR,
        "input[placeholder='* Адрес: куда привезти заказ']",
    )
    # Поле метро
    METRO_INPUT = (
        By.CSS_SELECTOR,
        "input.select-search__input[placeholder='* Станция метро']",
    )
    # Список со станциями метро
    METRO_OPTION = (
        By.XPATH,
        "//*[contains(concat(' ', normalize-space(@class), ' '), "
        "' select-search__option ') and normalize-space(.)='{}']",
    )

    # Поле номер телефона
    PHONE_INPUT = (
        By.CSS_SELECTOR,
        "input[placeholder='* Телефон: на него позвонит курьер']",
    )
    # Кнопка далее
    NEXT_BUTTON = (
        By.XPATH,
        "//button[normalize-space(.)='Далее']",
    )
    # Поле выбора даты заказа
    DATE_INPUT = (
        By.CSS_SELECTOR,
        "input[placeholder='* Когда привезти самокат']",
    )
    DATE_PICKER = (
        By.CSS_SELECTOR,
        ".react-datepicker",
    )
    # Поле выбора периода заказа
    RENTAL_PERIOD_DROPDOWN = (
        By.CSS_SELECTOR,
        ".Dropdown-control",
    )
    # Выбор периода заказа
    RENTAL_PERIOD_OPTION = (
        By.XPATH,
        "//div[contains(@class, 'Dropdown-option') "
        "and normalize-space(.)='{}']",
    )
    # Поле выбора цвета самоката
    COLOR_LABELS = {
        "black": (By.CSS_SELECTOR, "label[for='black']"),
        "grey": (By.CSS_SELECTOR, "label[for='grey']"),
    }
    # Поле комментарии для курьера
    COMMENT_INPUT = (
        By.CSS_SELECTOR,
        "input[placeholder='Комментарий для курьера'], "
        "textarea[placeholder='Комментарий для курьера']",
    )
    # Кнопка заказать
    SUBMIT_ORDER_BUTTON = (
        By.XPATH,
        "(//button[normalize-space(.)='Заказать'])[last()]",
    )
    # Окно подтверждения заказа
    CONFIRMATION_TITLE = (
        By.XPATH,
        "//div[contains(@class, 'Order_ModalHeader') "
        "and contains(normalize-space(.), 'Хотите оформить заказ?')]",
    )
    # Кнопка подтверждения заказа Да
    CONFIRM_ORDER_BUTTON = (
        By.XPATH,
        "//button[normalize-space(.)='Да']",
    )
    # Окно успешно созданного заказа
    SUCCESS_TITLE = (
        By.XPATH,
        "//div[contains(@class, 'Order_ModalHeader') "
        "and contains(normalize-space(.), 'Заказ оформлен')]",
    )