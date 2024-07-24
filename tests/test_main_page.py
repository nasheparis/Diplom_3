import allure

from data import FEED, WEBSITE, INGREDIENT_INFO_HEADER, ORDER_ACCEPTED_TEXT
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage


class TestMainPage:
    @allure.title("Тест проверяет переход по клику на «Конструктор»")
    def test_click_constructor_button(self, driver):
        main_page = MainPage(driver)
        current_url = main_page.click_constructor_button()
        assert current_url == WEBSITE

    @allure.title("Тест проверяет переход в раздел «Лента заказов»")
    def test_click_feed_button(self, driver):
        main_page = MainPage(driver)
        current_url = main_page.click_feed_button()
        assert current_url == FEED

    @allure.title("Тест проверяет, что по клику на ингредиент, появится всплывающее окно с деталями")
    def test_click_on_ingredient(self, driver):
        main_page = MainPage(driver)
        header_text = main_page.click_on_ingredient()
        assert header_text == INGREDIENT_INFO_HEADER

    @allure.title("Тест проверяет, что всплывающее окно закрывается кликом по крестику")
    def test_click_on_ingredient(self, driver):
        main_page = MainPage(driver)
        expected_result = main_page.click_close()
        assert expected_result is None

    @allure.title("Тест проверяет, что при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента")
    def test_counter_after_drag_and_drop(self, driver):
        main_page = MainPage(driver)
        count = main_page.add_ingredient()
        assert count == "2"

    @allure.title("Тест проверяет, что залогиненный пользователь может оформить заказ")
    def test_make_order_authorized(self, create_new_customer_and_delete_after_test, driver):
        payload = create_new_customer_and_delete_after_test
        main_page = MainPage(driver)
        personal_account_page = PersonalAccountPage(driver)

        main_page.click_personal_account_button()
        personal_account_page.sign_up_and_sign_in(payload)
        text = main_page.make_order()
        assert text == ORDER_ACCEPTED_TEXT
