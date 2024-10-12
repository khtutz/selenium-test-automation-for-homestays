from utilities.base_class import BaseClass
from page_objects.home_page import HomePage
import tests.constants as const
import time

class TestSignUp(BaseClass):
    def test_signup(self):
        
        home_page = HomePage(self.driver)
        signup_login_page = home_page.load_signup_login_page(const.SIGNUP_LOGIN_URL)
    
        # Signup/Login page
        # Prompting for manual input
        email = 'wotilon587@craftapk.com'
        first_name = 'Timonthy'
        last_name = 'Delton'
        date_of_birth = '05/06/2002'
        password = 'hY1#2$3door'
        receive_promo = 'no'
        '''
        email = input('Enter your email: ')
        first_name = input('Enter your first name: ')
        last_name = input('Enter your last name: ')
        date_of_birth = input('Enter your date of birth (mm/dd/yyyy): ')
        password = input('Enter your password: ')
        receive_promo = input('Receive promotional emails? (yes/no): ').lower() == 'yes'
        '''
        # Fill the form, and proceed
        signup_login_page.continue_with_email(email)
        signup_login_page.signup_with_email(
            first_name,
            last_name,
            date_of_birth,
            password,
            receive_promo
        )
        # Wait for manual entering of security code sent to email
        time.sleep(20)
        signup_login_page.agree_and_continue()
        signup_successful = signup_login_page.confirm_successful_signup_or_login()
        assert signup_successful == True, 'Account sign-up has failed!'
        # Save credentials after successful sign-up
        if signup_successful:
            signup_login_page.save_credentials_to_env(email, password)
