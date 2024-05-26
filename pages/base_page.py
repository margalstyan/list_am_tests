from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_visibility(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))

    def click(self, locator, timeout=10):
        element = self.wait_for_visibility(locator, timeout)
        element.click()

    def type_text(self, locator, text, timeout=10):
        element = self.wait_for_visibility(locator, timeout)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator, timeout=10):
        element = self.wait_for_visibility(locator, timeout)
        return element.text

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def get_placeholder_text(self, locator):
        return self.find_element(locator).get_attribute("placeholder")
