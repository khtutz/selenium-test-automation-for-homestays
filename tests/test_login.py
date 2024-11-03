from utilities.base_class import BaseClass
from page_objects.home_page import HomePage
from utilities import cookies_helper
import tests.constants as const

class TestLogIn(BaseClass):
    def test_login(self):
        home_page = HomePage(self.driver)
        signup_login_page = home_page.load_signup_login_page(const.SIGNUP_LOGIN_URL)

        # Prompt for email and password inputs
        email = input('Enter your email: ')
        password = input('Enter your password: ')
        # Fill the fields, and log in
        signup_login_page.continue_with_email(email)
        signup_login_page.login_with_password(password)
        # Check for successful login
        login_successful = signup_login_page.confirm_successful_signup_or_login()
        assert login_successful == True, 'Account log-in has failed!'

        # Store session data inside cookies
        if login_successful:
            cookies_helper.save_cookies(self.driver)
        
    def test_login_with_cookies(self):
        print('Testing login with cookies')
