from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Signup(object):

    def __init__(self, driver):
        self.driver = driver

    def open_signup_form(self):
        # Open_and_verify_sign_in page
        self.driver.find_element_by_css_selector(
            '.header__navbar--navigation .normal >:nth-child(6)').click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.tabbed-pane_tabs__1rsRG > :nth-child(1)')))
        # print("Signup form found")
        return True

    def fill_Signup_form(self,Email,Password):

        First_Name = self.driver.find_element_by_css_selector(
            '.form_form__1IFP- >:first-child > :first-child')
        First_Name.send_keys('Faizan')
        Second_Name = self.driver.find_element_by_css_selector(
            '.form_form__1IFP- >:first-child > :nth-child(2)')
        Second_Name.send_keys('Yaqoob')
        Reg_Email_Field = self.driver.find_element_by_css_selector(
            'input[type="email"')
        Reg_Email_Field.send_keys(Email)
        Reg_Password_Field = self.driver.find_element_by_css_selector(
            '.form_form__1IFP- >:nth-child(3) :first-child')
        Reg_Password_Field.send_keys(Password)
        Reg_Confirm_Password_Field = self.driver.find_element_by_css_selector(
            '.form_form__1IFP- >:nth-child(3) :nth-child(2)')
        Reg_Confirm_Password_Field.send_keys(Password)
        # print("sign up form filled")

    def submit_signup_form(self):
        # Find_and_click_submit_button
        Sign_Up_Button = self.driver.find_element_by_css_selector(
            '.tabbed-pane_content__3zivd .button_primary__1qhjh')
        Sign_Up_Button.click()