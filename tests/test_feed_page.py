import allure

from pages.feed_page import FeedPage
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage


class TestFeedPage:
    @allure.title("Тест проверяет открытие всплывающего окна с деталями по клике на заказ")
    def test_click_on_order(self, driver):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)

        main_page.click_feed_button()
        text = feed_page.click_on_order()
        assert 'бургер' in text

    @allure.title(
        "Тест проверяет, что заказ пользователя из раздела «История заказов» отображается на странице «Лента заказов»")
    def test_check_order_in_feed(self, driver, create_new_customer_and_delete_after_test):
        payload = create_new_customer_and_delete_after_test
        personal_account_page = PersonalAccountPage(driver)
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)

        main_page.click_personal_account_button()
        personal_account_page.sign_up_and_sign_in(payload)
        main_page.go_to_personal_account_after_order()
        order_number = personal_account_page.get_order_number().split('\n')[0]
        main_page.click_feed_button_without_overlay()
        feed_order_number = feed_page.check_order_in_feed().split('\n')[0]
        assert order_number == feed_order_number

    @allure.title("Тест проверяет, что при создании нового заказа счётчик 'Выполнено за всё время' увеличивается")
    def test_check_orders_number_all_time(self, driver, create_new_customer_and_delete_after_test):
        payload = create_new_customer_and_delete_after_test
        personal_account_page = PersonalAccountPage(driver)
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)

        main_page.click_personal_account_button()
        personal_account_page.sign_up_and_sign_in(payload)
        main_page.click_feed_button()
        orders_number_all_time = feed_page.get_orders_number_all_time()
        main_page.go_from_feed_to_make_order_then_to_feed()
        orders_number_all_time_updated = feed_page.get_orders_number_all_time()
        assert orders_number_all_time < orders_number_all_time_updated

    @allure.title("Тест проверяет, что при создании нового заказа счётчик 'Выполнено за сегодня' увеличивается")
    def test_check_orders_number_today(self, driver, create_new_customer_and_delete_after_test):
        payload = create_new_customer_and_delete_after_test
        personal_account_page = PersonalAccountPage(driver)
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)

        main_page.click_personal_account_button()
        personal_account_page.sign_up_and_sign_in(payload)
        main_page.click_feed_button()
        orders_number_today = feed_page.get_orders_number_today()
        main_page.go_from_feed_to_make_order_then_to_feed()
        orders_number_today_updated = feed_page.get_orders_number_today()
        assert orders_number_today < orders_number_today_updated

    @allure.title("Тест проверяет, что после оформления заказа его номер появляется в разделе 'В работе'")
    def test_check_order_in_progress(self, driver, create_new_customer_and_delete_after_test):
        payload = create_new_customer_and_delete_after_test
        personal_account_page = PersonalAccountPage(driver)
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)

        main_page.click_personal_account_button()
        personal_account_page.sign_up_and_sign_in(payload)
        order_number = main_page.get_order_number()
        main_page.close_order_window_proceed_to_feed()
        order_number_in_progress = feed_page.get_order_number_in_progress()
        assert '0' + order_number == order_number_in_progress
