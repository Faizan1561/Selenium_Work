from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random

class Home(object):

    Ran_Num = random.randint(101, 999)
    Password = random.randint(11111, 99999)

    def __init__(self, driver):
        self.driver = driver

    def on_home_page(self):
        # Open_and_verify_sign_in page
        # self.driver.get('https://www.udacity.com')
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'.header__navbar--navigation .normal >:nth-child(6)')))
        WebDriverWait(self.driver,10).until(EC.title_contains,'Learn the Latest')
        # print('on home page pass')
        return True
    def do_logout(self):
        logout_button = self.driver.find_element_by_css_selector(
            '._nav-module--nav-groups--3Eal6 > :nth-child(2) >:nth-child(2)>a')
        logout_button.click()
