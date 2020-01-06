from Pages.Base_Page import BaseClassPage
import random


class Home(BaseClassPage):

    Ran_Num = random.randint(101, 999)
    Password = random.randint(11111, 99999)

    def on_home_page(self):
        # Open_and_verify_sign_in page
        self.find_elem('.header__navbar--navigation .normal >:nth-child(6)')
        self.wait_for_title_match('Learn the Latest')
        return True

    def do_logout(self):
        logout_button = self.find_elem('._nav-module--nav-groups--3Eal6 > :nth-child(2) >:nth-child(2)>a')
        logout_button.click()
