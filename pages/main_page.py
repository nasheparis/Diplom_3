import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step("Клик по оверлею")
    def click_overlay(self):
        self.click_on_element_to_disappear(MainPageLocators.OVERLAY)

    @allure.step("Клик по кнопке 'Войти в аккаунт'")
    def click_sign_in_from_main_page(self):
        self.click_overlay()
        self.click_to_element(MainPageLocators.SIGN_IN_BUTTON)

    @allure.step("Переход по клику на «Личный кабинет»")
    def click_personal_account_button(self):
        self.click_overlay()
        self.click_to_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        self.click_overlay()

    @allure.step("Переход в раздел «Лента заказов»")
    def click_feed_button_without_overlay(self):
        self.click_to_element(MainPageLocators.FEED_BUTTON)

    @allure.step("Переход в раздел «Лента заказов»")
    def click_feed_button(self):
        self.click_overlay()
        self.click_to_element(MainPageLocators.FEED_BUTTON)
        current_url = self.get_current_url()
        return current_url

    @allure.step("Переход по клику на «Конструктор»")
    def click_constructor_button(self):
        self.click_overlay()
        self.click_to_element(MainPageLocators.CONSTRUCTOR_BUTTON)
        current_url = self.get_current_url()
        return current_url

    @allure.step("Клик на ингредиент")
    def click_on_ingredient(self):
        self.click_to_element(MainPageLocators.BURGER_INGREDIENT)
        header_text = self.get_text_from_element(MainPageLocators.INGREDIENT_INFO)
        return header_text

    @allure.step("Клик по крестику")
    def click_close(self):
        self.click_to_element(MainPageLocators.BURGER_INGREDIENT)
        self.get_text_from_element(MainPageLocators.INGREDIENT_INFO)
        self.click_to_element(MainPageLocators.CLOSE_BUTTON)
        self.find_element_with_wait(MainPageLocators.MODAL_WINDOW)

    @allure.step("Добавление ингредиента в заказ")
    def add_ingredient(self):
        bun = self.find_element_with_wait(MainPageLocators.BUN)
        cart = self.find_element_with_wait(MainPageLocators.ORDER_DRAG_AND_DROP_PLACE)
        self.drag_and_drop(bun, cart)
        count = self.get_text_from_element(MainPageLocators.INGREDIENT_COUNTER)
        return count

    @allure.step("Оформление заказа")
    def make_order(self):
        self.add_ingredient()
        self.click_to_element(MainPageLocators.PLACE_ORDER_BUTTON)
        text = self.get_text_from_element(MainPageLocators.ORDER_ACCEPTED)
        return text

    @allure.step("Переход в личный кабинет после оформления заказа")
    def go_to_personal_account_after_order(self):
        self.add_ingredient()
        self.click_to_element(MainPageLocators.PLACE_ORDER_BUTTON)
        self.wait_for_number_to_change(MainPageLocators.ORDER_NUMBER, '9999')
        self.click_to_element(MainPageLocators.ORDER_CARD_CLOSE_BUTTON)
        self.click_personal_account_button()

    @allure.step("Переход на оформление заказа с последующим переходом в 'Ленту заказов'")
    def go_from_feed_to_make_order_then_to_feed(self):
        self.click_constructor_button()
        self.add_ingredient()
        self.click_to_element(MainPageLocators.PLACE_ORDER_BUTTON)
        self.wait_for_number_to_change(MainPageLocators.ORDER_NUMBER, '9999')
        self.click_to_element(MainPageLocators.ORDER_CARD_CLOSE_BUTTON)
        self.click_feed_button()

    @allure.step("Получение номера оформленного заказа")
    def get_order_number(self):
        self.add_ingredient()
        self.click_to_element(MainPageLocators.PLACE_ORDER_BUTTON)
        self.wait_for_number_to_change(MainPageLocators.ORDER_NUMBER, '9999')
        order_number = self.get_text_from_element(MainPageLocators.ORDER_NUMBER)
        return order_number

    @allure.step("Закрытие окна с номером заказа")
    def close_order_window_proceed_to_feed(self):
        self.click_to_element(MainPageLocators.ORDER_CARD_CLOSE_BUTTON)
        self.click_feed_button()
