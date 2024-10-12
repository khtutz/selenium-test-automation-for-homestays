from utilities.base_class import BaseClass
from page_objects.home_page import HomePage
import tests.constants as const
import time

class TestSignUp(BaseClass):
    def test_signup(self):
        home_page = HomePage(self.driver)
        signup_login_page = home_page.load_signup_login_page(const.SIGNUP_LOGIN_URL)

        # Prompting for manual email, and password inputs
        email = input('Enter your email: ')
        password = input('Enter your password: ')
        # Fill the fields, and log in
        signup_login_page.continue_with_email(email)
        signup_login_page.login_with_password(password)
        # Check for successful login
        login_successful = signup_login_page.confirm_successful_signup_or_login()
        assert login_successful == True, 'Account log-in has failed!'
