from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class BaseClassPage(object):

    def __init__(self, driver):
        self.driver = driver

    # Locator_finding
    def find_elem(self, locator, time=10):
        try:
            return WebDriverWait(self.driver, time).until(EC.presence_of_element_located((By.CSS_SELECTOR, locator)))
        except TimeoutException:
            raise TimeoutException(f'{locator} not found')

    # Element_visibility
    def wait_for_elem_visibility(self, locator, time=10):
        try:
            return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        except TimeoutException:
            raise TimeoutException(f'{locator} is not visible')

    # Title_matching
    def wait_for_title_match(self, title_string, time=25):
        try:
            return WebDriverWait(self.driver, time).until(EC.title_contains(title_string))
        except TimeoutException:
            raise TimeoutException(f'{title_string} is not available in {self.driver.title}')
