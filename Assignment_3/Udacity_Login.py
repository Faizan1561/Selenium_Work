import unittest
from selenium import webdriver
from Pages.SignUp_Page import Signup
from Pages.LogIn_Page import Login
from Pages.Home_Page import Home
from Pages.Dashboard_Page import Dashboard


class UdacityLogIn(unittest.TestCase):

    def setUp(self):
        self.chrome_browser = webdriver.Chrome()
        self.chrome_browser.maximize_window()

        self.chrome_browser.get('https://www.udacity.com')

        self.login = Login(self.chrome_browser)
        self.signup = Signup(self.chrome_browser)
        self.home = Home(self.chrome_browser)
        self.dashboard = Dashboard(self.chrome_browser)

        self.email = f'faizanyaqoob{self.home.Ran_Num}@gmail.com'
        self.password = f'Kayak{self.home.Ran_Num}#'

    def test_Signup(self):
        self.assertTrue(self.home.on_home_page())
        self.signup.open_signup_form()
        self.signup.fill_Signup_form(self.email, self.password)
        self.signup.submit_signup_form()
        self.assertTrue(self.dashboard.on_dashboard_page())
        self.home.do_logout()

        print(f'Your account credentials are: ')
        print(f'Email address: {self.email}')
        print(f'password: {self.password}')

        self.assertTrue(self.home.on_home_page())
        self.login.open_login_form()
        self.login.fill_login_form(self.email, self.password)
        self.login.submit_login_form()
        self.assertTrue(self.dashboard.on_dashboard_page())

    def tearDown(self):
        self.chrome_browser.close()


if __name__ == '__main__':
    unittest.main()
