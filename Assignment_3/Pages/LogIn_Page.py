from Pages.Base_Page import BaseClassPage


class Login(BaseClassPage):

    def open_login_form(self):
        # Open_and_verify_sign_in page
        self.find_elem('.header__navbar--navigation .normal >:nth-child(5)').click()
        self.wait_for_elem_visibility('.tabbed-pane_tabs__1rsRG > :nth-child(2)')
        return True

    def fill_login_form(self, email, password):

        # Find_and_fill_email_field
        email_field = self.find_elem('input[type="email"]')
        email_field.send_keys(email)
        # Find_and_fill_password_field
        password_field = self.find_elem('input[type="password"]')
        password_field.send_keys(password)

    def submit_login_form(self):
        # Find_and_click_submit_button
        sign_in_button = self.find_elem('.tabbed-pane_content__3zivd .button_primary__1qhjh')
        sign_in_button.click()
