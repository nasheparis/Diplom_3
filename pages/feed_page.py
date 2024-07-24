import allure

from locators.feed_page_locators import FeedPageLocators
from pages.base_page import BasePage


class FeedPage(BasePage):
    @allure.step("Клик на заказ")
    def click_on_order(self):
        self.click_to_element(FeedPageLocators.ORDER_CARD)
        text = self.get_text_from_element(FeedPageLocators.ORDER_CARD_NAME)
        return text

    @allure.step("Проверка заказа пользователя в 'Ленте заказов'")
    def check_order_in_feed(self):
        order_number = self.get_text_from_element(FeedPageLocators.ORDER_NUMBER)
        return order_number

    @allure.step("Получение количества заказов за все время")
    def get_orders_number_all_time(self):
        orders_number_all_time = self.get_text_from_element(FeedPageLocators.ORDERS_NUMBER_ALL_TIME)
        return orders_number_all_time

    @allure.step("Получение количества заказов за сегодня")
    def get_orders_number_today(self):
        orders_number_today = self.get_text_from_element(FeedPageLocators.ORDERS_NUMBER_TODAY)
        return orders_number_today

    @allure.step("Получение номера оформленного заказа в работе")
    def get_order_number_in_progress(self):
        order_number_in_progress = self.get_text_from_element(FeedPageLocators.ORDER_NUMBER_IN_PROGRESS)
        return order_number_in_progress
