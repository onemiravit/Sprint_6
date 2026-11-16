import allure
from selenium.webdriver.common.keys import Keys

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step("Дождаться загрузки формы заказа")
    def wait_until_ready(self):
        self.wait_visible(OrderPageLocators.FIRST_NAME_INPUT)
        return self

    @allure.step("Заполнить данные получателя")
    def fill_customer_data(self, data):
        # Вводим Имя
        self.enter_text(
            OrderPageLocators.FIRST_NAME_INPUT,
            data["first_name"],
        )
        # Вводим Фамилию
        self.enter_text(
            OrderPageLocators.LAST_NAME_INPUT,
            data["last_name"],
        )
        # Вводим адрес
        self.enter_text(
            OrderPageLocators.ADDRESS_INPUT,
            data["address"],
        )
        # Выбираем метро
        self.enter_text(
            OrderPageLocators.METRO_INPUT,
            data["metro"],
        )

        metro_option = self.format_locator(
            OrderPageLocators.METRO_OPTION,
            data["metro"],
        )
        self.click(metro_option)

        self.wait_for_attribute_value(
            OrderPageLocators.METRO_INPUT,
            "value",
            data["metro"],
        )
        # Вводим номер телефона
        self.enter_text(
            OrderPageLocators.PHONE_INPUT,
            data["phone"],
        )
        # Кликаем на кнопку подтверждения
        self.click(OrderPageLocators.NEXT_BUTTON)
        self.wait_visible(OrderPageLocators.DATE_INPUT)

    @allure.step("Заполнить данные аренды")
    def fill_rental_data(self, data):
        self.click(OrderPageLocators.DATE_INPUT)
        self.enter_text(
            OrderPageLocators.DATE_INPUT,
            data["delivery_date"],
        )
        self.send_keys(
            OrderPageLocators.DATE_INPUT,
            Keys.TAB,
        )

        self.wait_for_attribute_value(
            OrderPageLocators.DATE_INPUT,
            "value",
            data["delivery_date"],
        )

        self.send_keys(
            OrderPageLocators.DATE_INPUT,
            Keys.ESCAPE,
        )
        self.wait_invisible(OrderPageLocators.DATE_PICKER)

        self.click(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        rental_option = self.format_locator(
            OrderPageLocators.RENTAL_PERIOD_OPTION,
            data["rental_period"],
        )
        self.click(rental_option)

        color_locator = OrderPageLocators.COLOR_LABELS.get(
            data["color"]
        )
        if color_locator is None:
            raise ValueError(
                f"Неизвестный цвет самоката: {data['color']}"
            )

        self.click(color_locator)

        comment = data.get("comment", "")
        if comment:
            self.enter_text(
                OrderPageLocators.COMMENT_INPUT,
                comment,
            )

    @allure.step("Подтвердить заказ")
    def submit_and_confirm(self):
        # Кликаем на кнопку заказа
        self.click(OrderPageLocators.SUBMIT_ORDER_BUTTON)
        self.wait_visible(OrderPageLocators.CONFIRMATION_TITLE)
        # Кликаем на кнопку подтверждения заказа
        self.click(OrderPageLocators.CONFIRM_ORDER_BUTTON)
        success_title = self.wait_visible(
            OrderPageLocators.SUCCESS_TITLE
        )
        return success_title.text.strip()