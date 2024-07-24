from selenium.webdriver.common.by import By


class PersonalAccountPageLocators:
    SIGN_UP_BUTTON = By.XPATH, '//*[contains(@href, "register")]'
    SIGN_UP_BUTTON_TO_REGISTER = By.XPATH, '//*[contains(@class, "button_button_size_medium")]'
    NAME_INPUT_SIGN_UP = By.XPATH, '//*[text()="Имя"]/following-sibling::input'
    EMAIL_INPUT_SIGN_UP = By.XPATH, '//*[text()="Email"]/following-sibling::input'
    PASSWORD_INPUT_SIGN_UP = By.XPATH, '//*[text()="Пароль"]/following-sibling::input'
    EMAIL_INPUT_SIGN_IN = By.XPATH, '//*[text()="Email"]/following-sibling::input'
    PASSWORD_INPUT_SIGN_IN = By.XPATH, '//*[text()="Пароль"]/following-sibling::input'
    SIGN_IN_BUTTON_TO_SIGN_IN = By.XPATH, '//button[contains(., "Войти")]'
    ORDER_HISTORY = By.XPATH, '//a[contains(text(), "История заказов")]'
    SIGN_OUT_BUTTON = By.XPATH, '//button[contains(text(),"Выход")]'
    DESCRIPTION = By.XPATH, '//p[contains(@class, "Account_text")]'
    LOGIN_PAGE_HEADER_LOCATOR = By.XPATH, '//h2[contains(text(), "Вход")]'
    ORDER_NUMBER_LIST = (
        By.XPATH,
        '(//div[contains(@class, "OrderHistory_textBox")]''/p[contains(@class, "text_type_digits-default")])[1]')
    ORDER_NUMBER = By.XPATH, '//p[contains(@class, "text_type_digits-default")]'
    CLOSE_BUTTON = By.XPATH, ('//button[contains(@class, "Modal_modal__close_modified") and contains(@class, '
                              '"Modal_modal__close")]')
