import allure

from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):
    @allure.step("Переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def click_on_forgot_password_button(self):
        self.click_to_element(ForgotPasswordPageLocators.FORGOT_PASSWORD_BUTTON_SIGN_IN)
        current_url = self.get_current_url()
        return current_url

    @allure.step("Ввод почты и клик по кнопке «Восстановить»")
    def enter_email_and_click_restore(self):
        self.click_to_element(ForgotPasswordPageLocators.FORGOT_PASSWORD_BUTTON_SIGN_IN)
        self.add_text_to_element(ForgotPasswordPageLocators.EMAIL_FIELD, "testemail@ya.ru")
        self.click_to_element(ForgotPasswordPageLocators.RESTORE_PASSWORD_BUTTON)
        text = self.get_text_from_element(ForgotPasswordPageLocators.RESET_PASSWORD_TEXT)
        return text

    @allure.step("Клик по кнопке показать пароль делает поле активным (подсвеченным)")
    def click_show_password(self):
        self.click_to_element(ForgotPasswordPageLocators.FORGOT_PASSWORD_BUTTON_SIGN_IN)
        self.add_text_to_element(ForgotPasswordPageLocators.EMAIL_FIELD, "testemail@ya.ru")
        self.click_to_element(ForgotPasswordPageLocators.RESTORE_PASSWORD_BUTTON)
        self.click_on_element_to_disappear(ForgotPasswordPageLocators.OVERLAY)
        self.click_to_element(ForgotPasswordPageLocators.SHOW_PASSWORD_ICON)
        expected_result = self.find_element_with_wait(ForgotPasswordPageLocators.PASSWORD_FIELD_ACTIVE)
        return expected_result
