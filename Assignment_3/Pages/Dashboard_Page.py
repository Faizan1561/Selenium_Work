from Pages.Base_Page import BaseClassPage


class Dashboard(BaseClassPage):

    def on_dashboard_page(self):
        # Open_and_verify_sign_in page
        self.wait_for_title_match('Home')
        self.find_elem('._layout-module--nav--3qaiq ._'
                       'nav-module--nav-groups--3Eal6 > :first-child> :first-child>:first-child')
        return True

