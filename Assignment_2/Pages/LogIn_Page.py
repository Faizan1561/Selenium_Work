from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Login(object):

    def __init__(self, driver):
        self.driver = driver

    def open_login_form(self):
        # Open_and_verify_sign_in page
        self.driver.find_element_by_css_selector(
            '.header__navbar--navigation .normal >:nth-child(5)').click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.tabbed-pane_tabs__1rsRG > :nth-child(2)')))
        return True

    def fill_login_form(self,Email,Password):

        # Find_and_fill_email_field
        Email_Field = self.driver.find_element_by_css_selector('input[type="email"]')
        Email_Field.send_keys(Email)
        # Find_and_fill_password_field
        Password_Field = self.driver.find_element_by_css_selector('input[type="password"]')
        Password_Field.send_keys(Password)

    def submit_login_form(self):
        # Find_and_click_submit_button
        Sign_In_Button = self.driver.find_element_by_css_selector(
            '.tabbed-pane_content__3zivd .button_primary__1qhjh')
        Sign_In_Button.click()