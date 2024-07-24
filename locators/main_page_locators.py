from selenium.webdriver.common.by import By


class MainPageLocators:
    OVERLAY = By.XPATH, '//div[contains(@class, "Modal_modal_overlay")]'
    SIGN_IN_BUTTON = By.XPATH, './/button[text()="Войти в аккаунт"]'
    LOADING_SPINNER = By.XPATH, '//div[@class="loading-spinner"]'
    PERSONAL_ACCOUNT_BUTTON = By.XPATH, '//p[contains(text(), "Личный Кабинет")]'
    FEED_BUTTON = By.XPATH, '//p[contains(text(), "Лента Заказов")]'
    CONSTRUCTOR_BUTTON = By.XPATH, ('//p[contains(@class, "AppHeader_header__linkText")][contains(text(), '
                                    '"Конструктор")]')
    BURGER_INGREDIENT = By.XPATH, '//img[contains(@class, "BurgerIngredient_ingredient")]'
    INGREDIENT_INFO = By.XPATH, '//h2[contains(text(), "Детали ингредиента")]'
    CLOSE_BUTTON = By.XPATH, '//button[contains(@class, "Modal_modal__close")]'
    MODAL_WINDOW_OPENED = By.XPATH, '//section[contains(@class, "Modal_modal_opened")]'
    MODAL_WINDOW = By.XPATH, '//section[contains(@class, "Modal_modal")]'
    BUN = By.XPATH, ('//img[contains(@class, "BurgerIngredient_ingredient__image") and contains(@alt, "Флюоресцентная '
                     'булка R2-D3")]')
    ORDER_DRAG_AND_DROP_PLACE = By.XPATH, '//span[contains(text(), "Перетяните булочку сюда")]'
    INGREDIENT_COUNTER = By.XPATH, '//p[contains(@class, "counter_counter__num__")]'
    PLACE_ORDER_BUTTON = By.XPATH, './/button[text()="Оформить заказ"]'
    ORDER_ACCEPTED = By.XPATH, '//p[contains(text(), "Ваш заказ начали готовить")]'
    ORDER_NUMBER = By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//h2'
    ORDER_CARD_CLOSE_BUTTON = By.XPATH, ('//button[contains(@class, "Modal_modal__close") and contains(@class, '
                                         '"Modal_modal__close_modified")]')
