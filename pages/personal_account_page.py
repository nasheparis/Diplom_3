import allure

from locators.personal_account_page_locators import PersonalAccountPageLocators
from pages.base_page import BasePage


class PersonalAccountPage(BasePage):
    @allure.step("Регистрация и вход")
    def sign_up_and_sign_in(self, payload):
        self.click_to_element(PersonalAccountPageLocators.SIGN_UP_BUTTON)
        self.add_text_to_element(PersonalAccountPageLocators.NAME_INPUT_SIGN_UP, payload['name'])
        self.add_text_to_element(PersonalAccountPageLocators.EMAIL_INPUT_SIGN_UP, payload['email'])
        self.add_text_to_element(PersonalAccountPageLocators.PASSWORD_INPUT_SIGN_UP, payload['password'])
        self.click_to_element(PersonalAccountPageLocators.SIGN_UP_BUTTON_TO_REGISTER)
        self.find_element_with_wait(PersonalAccountPageLocators.SIGN_IN_BUTTON_TO_SIGN_IN)
        self.add_text_to_element(PersonalAccountPageLocators.EMAIL_INPUT_SIGN_IN, payload['email'])
        self.add_text_to_element(PersonalAccountPageLocators.PASSWORD_INPUT_SIGN_IN, payload['password'])
        self.click_to_element(PersonalAccountPageLocators.SIGN_IN_BUTTON_TO_SIGN_IN)

    @allure.step("Получение текста в профиле")
    def get_profile_description(self):
        text = self.get_text_from_element(PersonalAccountPageLocators.DESCRIPTION)
        return text

    @allure.step("Переход в раздел «История заказов»")
    def click_order_history_button(self):
        self.click_to_element(PersonalAccountPageLocators.ORDER_HISTORY)
        current_url = self.get_current_url()
        return current_url

    @allure.step("Выход из аккаунта")
    def sign_out(self):
        self.click_to_element(PersonalAccountPageLocators.SIGN_OUT_BUTTON)
        page_text = self.get_text_from_element(PersonalAccountPageLocators.LOGIN_PAGE_HEADER_LOCATOR)
        return page_text

    @allure.step("Получение номера заказа")
    def get_order_number(self):
        self.click_order_history_button()
        order_number = self.get_text_from_element(PersonalAccountPageLocators.ORDER_NUMBER_LIST)
        return order_number
