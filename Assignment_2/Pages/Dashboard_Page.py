from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Dashboard(object):

    def __init__(self, driver):
        self.driver = driver

    def on_dashboard_page(self):
        # Open_and_verify_sign_in page
        WebDriverWait(self.driver, 100).until(EC.title_contains('Home'))
        WebDriverWait(self.driver, 100).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '._layout-module--nav--3qaiq ._nav-module--nav-groups--3Eal6 > :first-child> :first-child>:first-child')))
        return True

