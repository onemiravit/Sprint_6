import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


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

        self.wait.until(
            lambda driver: driver.find_element(
                *OrderPageLocators.METRO_INPUT
            ).get_property("value") == data["metro"]
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
        # Заполняем дату заказа
        date_field = self.wait_visible(OrderPageLocators.DATE_INPUT)
        date_field.click()
        date_field.clear()
        date_field.send_keys(data["delivery_date"])
        date_field.send_keys(Keys.TAB)

        self.wait.until(
            lambda driver: driver.find_element(
                *OrderPageLocators.DATE_INPUT
            ).get_attribute("value") == data["delivery_date"]
        )

        # Закрыть календарь, который перекрывает список срока аренды.
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
        self.wait.until(
            EC.invisibility_of_element_located(
                OrderPageLocators.DATE_PICKER
            )
        )
        # Выбираем период аренды
        self.click(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)

        rental_option = self.format_locator(
            OrderPageLocators.RENTAL_PERIOD_OPTION,
            data["rental_period"],
        )
        self.click(rental_option)
        # Выбираем цвет самоката
        color_locator = OrderPageLocators.COLOR_LABELS.get(data["color"])
        if color_locator is None:
            raise ValueError(f"Неизвестный цвет самоката: {data['color']}")

        self.click(color_locator)
        # Вводим комментарии для курьера
        comment = data.get("comment", "")
        if comment:
            self.enter_text(OrderPageLocators.COMMENT_INPUT, comment)

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