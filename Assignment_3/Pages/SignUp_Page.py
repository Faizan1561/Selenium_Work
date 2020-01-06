from Pages.Base_Page import BaseClassPage


class Signup(BaseClassPage):

    def open_signup_form(self):
        # Open_and_verify_sign_in page
        self.find_elem('.header__navbar--navigation .normal >:nth-child(6)').click()
        self.wait_for_elem_visibility('.tabbed-pane_tabs__1rsRG > :nth-child(1)')
        return True

    def fill_Signup_form(self, email, password):
        # Fill_out_all_fields_of_signup_form e.g. name,email and password
        first_name = self.find_elem('.form_form__1IFP- >:first-child > :first-child')
        first_name.send_keys('Faizan')

        second_name = self.find_elem('.form_form__1IFP- >:first-child > :nth-child(2)')
        second_name.send_keys('Yaqoob')

        reg_email_field = self.find_elem('input[type="email"')
        reg_email_field.send_keys(email)

        reg_password_field = self.find_elem('.form_form__1IFP- >:nth-child(3) :first-child')
        reg_password_field.send_keys(password)
        reg_confirm_password_field = self.find_elem('.form_form__1IFP- >:nth-child(3) :nth-child(2)')
        reg_confirm_password_field.send_keys(password)

    def submit_signup_form(self):
        # Find_and_click_submit_button
        sign_up_button = self.find_elem('.tabbed-pane_content__3zivd .button_primary__1qhjh')
        sign_up_button.click()
