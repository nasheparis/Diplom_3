from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:
    OVERLAY = By.XPATH, '//div[contains(@class, "Modal_modal_overlay")]'
    FORGOT_PASSWORD_BUTTON_SIGN_IN = By.XPATH, '//a[@href="/forgot-password"]'
    EMAIL_FIELD = By.XPATH, '//input[contains(@class, "input__textfield") and contains(@name, "name")]'
    RESTORE_PASSWORD_BUTTON = By.XPATH, '//button[contains(text(), "Восстановить")]'
    RESET_PASSWORD_TEXT = By.XPATH, '//h2[contains(text(), "Восстановление пароля")]'
    PASSWORD_FIELD = By.XPATH, '//label[contains(text(), "Пароль")]'
    SHOW_PASSWORD_ICON = By.XPATH, '//div[contains(@class, "input__icon")]'
    PASSWORD_FIELD_ACTIVE = By.XPATH, ('//div[contains(@class, "input_type_text") and contains(@class, '
                                       '"input_status_active")]')
