import allure

from data import ORDERS_HISTORY, LOGIN_PAGE_HEADER, PROFILE_DESCRIPTION
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage


class TestPersonalAccountPage:
    @allure.title("Тест проверяет переход по клику на «Личный кабинет»")
    def test_click_personal_account_authorized(self, create_new_customer_and_delete_after_test, driver):
        payload = create_new_customer_and_delete_after_test
        main_page = MainPage(driver)
        personal_account_page = PersonalAccountPage(driver)

        main_page.click_personal_account_button()
        personal_account_page.sign_up_and_sign_in(payload)
        main_page.click_personal_account_button()
        text = personal_account_page.get_profile_description()
        assert text == PROFILE_DESCRIPTION

    @allure.title("Тест проверяет переход в раздел «История заказов»")
    def test_click_order_history_button(self, create_new_customer_and_delete_after_test, driver):
        payload = create_new_customer_and_delete_after_test
        main_page = MainPage(driver)
        personal_account_page = PersonalAccountPage(driver)

        main_page.click_personal_account_button()
        personal_account_page.sign_up_and_sign_in(payload)
        main_page.click_personal_account_button()
        current_url = personal_account_page.click_order_history_button()
        assert current_url == ORDERS_HISTORY

    @allure.title("Тест проверяет выход из аккаунта")
    def test_sign_out(self, create_new_customer_and_delete_after_test, driver):
        payload = create_new_customer_and_delete_after_test
        main_page = MainPage(driver)
        personal_account_page = PersonalAccountPage(driver)

        main_page.click_personal_account_button()
        personal_account_page.sign_up_and_sign_in(payload)
        main_page.click_personal_account_button()
        page_text = personal_account_page.sign_out()
        assert page_text == LOGIN_PAGE_HEADER
