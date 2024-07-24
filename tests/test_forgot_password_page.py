import allure

from data import FORGOT_PASSWORD, RESET_PASSWORD_TEXT
from pages.forgot_password_page import ForgotPasswordPage
from pages.main_page import MainPage


class TestForgotPasswordPage:
    @allure.title("Тест проверяет переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_click_on_forgot_password_button(self, driver):
        main_page = MainPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)

        main_page.click_sign_in_from_main_page()
        current_url = forgot_password_page.click_on_forgot_password_button()
        assert current_url == FORGOT_PASSWORD

    @allure.title("Тест проверяет переход на страницу сброса пароля после ввода почты и клику по кнопке «Восстановить»")
    def test_enter_email_and_click_restore(self, driver):
        main_page = MainPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)

        main_page.click_sign_in_from_main_page()
        text = forgot_password_page.enter_email_and_click_restore()
        assert text == RESET_PASSWORD_TEXT

    @allure.title("Тест проверяет, что клик по кнопке показать пароль делает поле активным (подсвеченным)")
    def test_click_show_password(self, driver):
        main_page = MainPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)

        main_page.click_sign_in_from_main_page()
        expected_result = forgot_password_page.click_show_password()
        assert expected_result is not None
