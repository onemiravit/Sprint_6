from datetime import date, timedelta

import allure
import pytest

from pages.main_page import MainPage


def delivery_date():
    return (date.today() + timedelta(days=2)).strftime("%d.%m.%Y")


ORDER_CASES = [
    pytest.param(
        "top",
        {
            "first_name": "Александр",
            "last_name": "Иванов",
            "address": "Москва, улица Ленина, 1",
            "metro": "Сокольники",
            "phone": "+79991234567",
            "delivery_date": delivery_date(),
            "rental_period": "двое суток",
            "color": "black",
            "comment": "Позвонить перед доставкой",
        },
        id="header-order-button",
    ),
    pytest.param(
        "bottom",
        {
            "first_name": "Мария",
            "last_name": "Смирнова",
            "address": "Москва, проспект Мира, 10",
            "metro": "Черкизовская",
            "phone": "+79991234568",
            "delivery_date": delivery_date(),
            "rental_period": "трое суток",
            "color": "grey",
            "comment": "Позвонить за 10 минут",
        },
        id="bottom-order-button",
    ),
]


class TestScooterOrder:
    @pytest.mark.parametrize(
        "entry_point, order_data",
        ORDER_CASES,
    )
    @allure.epic("Яндекс.Самокат")
    @allure.feature("Заказ самоката")
    @allure.story("Позитивный сценарий")
    @allure.title("Оформить заказ через кнопку {entry_point}")
    def test_successful_order(
        self,
        driver,
        entry_point,
        order_data,
    ):
        order_page = (
            MainPage(driver)
            .open()
            .click_order_button(entry_point)
        )

        order_page.fill_customer_data(order_data)
        order_page.fill_rental_data(order_data)
        success_message = order_page.submit_and_confirm()

        assert "Заказ оформлен" in success_message