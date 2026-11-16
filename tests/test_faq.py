import allure
import pytest

from pages.main_page import MainPage


FAQ_CASES = [
    pytest.param(
        0,
        "Сколько это стоит? И как оплатить?",
        "Сутки — 400 рублей. Оплата курьеру — наличными или картой.",
        id="cost-and-payment",
    ),
    pytest.param(
        1,
        "Хочу сразу несколько самокатов! Так можно?",
        "Пока что у нас так: один заказ — один самокат. Если хотите "
        "покататься с друзьями, можете просто сделать несколько "
        "заказов — один за другим.",
        id="several-scooters",
    ),
    pytest.param(
        2,
        "Как рассчитывается время аренды?",
        "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. "
        "Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. "
        "Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.",
        id="rental-time",
    ),
    pytest.param(
        3,
        "Можно ли заказать самокат прямо на сегодня?",
        "Только начиная с завтрашнего дня. Но скоро станем расторопнее.",
        id="order-for-today",
    ),
    pytest.param(
        4,
        "Можно ли продлить заказ или вернуть самокат раньше?",
        "Пока что нет! Но если что-то срочное — всегда можно позвонить "
        "в поддержку по красивому номеру 1010.",
        id="extend-or-return",
    ),
    pytest.param(
        5,
        "Вы привозите зарядку вместе с самокатом?",
        "Самокат приезжает к вам с полной зарядкой. Этого хватает "
        "на восемь суток — даже если будете кататься без передышек "
        "и во сне. Зарядка не понадобится.",
        id="charger",
    ),
    pytest.param(
        6,
        "Можно ли отменить заказ?",
        "Да, пока самокат не привезли. Штрафа не будет, "
        "объяснительной записки тоже не попросим. Все же свои.",
        id="cancel-order",
    ),
    pytest.param(
        7,
        "Я живу за МКАДом, привезёте?",
        "Да, обязательно. Всем самокатов! И Москве, и Московской области.",
        id="delivery-outside-mkad",
    ),
]


class TestImportantQuestions:
    @pytest.mark.parametrize(
        "index, expected_question, expected_answer",
        FAQ_CASES,
    )
    @allure.epic("Яндекс.Самокат")
    @allure.feature("Вопросы о важном")
    @allure.title("Проверить ответ на вопрос «{expected_question}»")
    def test_faq_answer_matches_question(
        self,
        driver,
        index,
        expected_question,
        expected_answer,
    ):
        page = MainPage(driver)
        actual_question, actual_answer = page.expand_faq(index)

        assert actual_question == expected_question
        assert actual_answer == expected_answer