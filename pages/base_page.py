from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_to_element(self, locator):
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def click_on_element_to_disappear(self, locator):
        element = WebDriverWait(self.driver, 20).until(expected_conditions.invisibility_of_element_located(locator))
        ActionChains(self.driver).move_to_element(element).click().perform()

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def get_current_url(self):
        return self.driver.current_url

    def drag_and_drop(self, source_element, target_element):
        ActionChains(self.driver).drag_and_drop(source_element, target_element).pause(10).perform()

    def wait_for_number_to_change(self, locator, value):
        return WebDriverWait(self.driver, 20).until_not(
            expected_conditions.text_to_be_present_in_element(locator, value))
