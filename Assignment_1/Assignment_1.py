import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Udacity_Login(unittest.TestCase):

    def setUp(self):
        # Initialize_webdriver
        self.chrome_browser = webdriver.Chrome()
        self.chrome_browser.maximize_window()

    def test_Login(self):
        # Open_the Webiste_
        self.chrome_browser.get('https://www.udacity.com')

        # Open_and_verify_sign_in page
        self.chrome_browser.find_element_by_css_selector(
            '.header__navbar--navigation .normal >:nth-child(5)').click()
        WebDriverWait(self.chrome_browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.tabbed-pane_tabs__1rsRG > :nth-child(2)')))

        # Find_and_fill_login_form
        Email_Field = self.chrome_browser.find_element_by_css_selector('input[type="email"]')
        Email_Field.send_keys('firstbrowser104@gmail.com')

        # Find_and_fill_password_field
        Password_Field = self.chrome_browser.find_element_by_css_selector('input[type="password"]')
        Password_Field.send_keys('Kayak54321')

        # Find_and_click_submit_button
        Sign_In_Button = self.chrome_browser.find_element_by_css_selector(
            '.tabbed-pane_content__3zivd .button_primary__1qhjh')
        Sign_In_Button.click()

        # Verify_on_dashboard_page
        WebDriverWait(self.chrome_browser, 100).until(EC.title_contains('Home'))
        self.assertIn('https://classroom.udacity.com/me', self.chrome_browser.current_url)
        self.assertIn('Home', self.chrome_browser.title)

    def tearDown(self):
        # Browser_termination
        self.chrome_browser.close()


if __name__ == '__main__':
    unittest.main()
