from selenium.webdriver.common.by import By


class FeedPageLocators:
    ORDER_CARD = By.XPATH, '//*[contains(@class, "OrderHistory_listItem")]'
    ORDER_CARD_NAME = By.XPATH, '//*[contains(@class, "OrderHistory_listItem")]//h2'
    ORDER_NUMBER = By.XPATH, '//div[contains(@class, "OrderHistory_textBox")]'
    ORDERS_NUMBER_ALL_TIME = By.XPATH, ('//p[contains(text(), "Выполнено за все время")]/following-sibling::p['
                                        'contains(@class, "OrderFeed_number__")]')
    ORDERS_NUMBER_TODAY = By.XPATH, ('//p[contains(text(), "Выполнено за сегодня")]/following-sibling::p[contains('
                                     '@class, "OrderFeed_number__")]')
    ORDER_NUMBER_IN_PROGRESS = By.XPATH, ('//ul[contains(@class, "OrderFeed_orderListReady")]/li[contains(@class, '
                                          '"text_type_digits-default")]')

