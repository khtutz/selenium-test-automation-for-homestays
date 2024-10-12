from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities import pw_encrypt, pw_decrypt

class SignupLoginPage():
    def __init__(self, driver):
        self.driver = driver

    def continue_with_email(self, email):
        email_btn = self.driver.find_element(
            By.CSS_SELECTOR,
            'button[data-testid="social-auth-button-email"]'
        )
        email_btn.click()
        email_input = self.driver.find_element(
            By.CSS_SELECTOR,
            'input[id="email-login-email"]'
        )
        email_input.send_keys(email)
        continue_btn = self.driver.find_element(
            By.CSS_SELECTOR,
            'button[data-testid="signup-login-submit-btn"]'
        )
        continue_btn.click()

    def signup_with_email(
            self,
            first_name,
            last_name,
            date_of_birth,
            password,
            receive_promotional_mail
        ):
        # Input names
        first_name_input = self.driver.find_element(
            By.CSS_SELECTOR,
            'input[data-testid="email-signup-user[first_name]"]'
        )
        first_name_input.send_keys(first_name)
        last_name_input = self.driver.find_element(
            By.CSS_SELECTOR,
            'input[data-testid="email-signup-user[last_name]"]'
        )
        last_name_input.send_keys(last_name)
        # Input date of birth
        signup_date_input = self.driver.find_element(
            By.CSS_SELECTOR,
            'input[id="email-signup-date"]'
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(signup_date_input).click().send_keys(date_of_birth).perform()
        # Input password
        password_input = self.driver.find_element(
            By.CSS_SELECTOR,
            'input[data-testid="email-signup-password"]'
        )
        password_input.send_keys(password)
        # Promotinal mail
        if not receive_promotional_mail:
            promotional_email_chkbx = self.driver.find_element(
                By.CSS_SELECTOR,
                'input[id="email-signupuser_profile_info[receive_promotional_email]"]'
            )
            promotional_email_chkbx.click()
        # Submit sign-up form
        submit_btn = self.driver.find_element(
            By.CSS_SELECTOR,
            'button[data-testid="signup-login-submit-btn"]'
        )
        submit_btn.click()

    def login_with_password(self, password):
        password_input = self.driver.find_element(
            By.CSS_SELECTOR,
            'input[data-testid="email-signup-password"]'
        )
        password_input.send_keys(password)
        login_btn = self.driver.find_element(
            By.CSS_SELECTOR,
            'button[data-testid="signup-login-submit-btn"]'
        )
        login_btn.click()

    def agree_and_continue(self):
        btn = self.driver.find_element(
            By.CSS_SELECTOR,
            'button[data-testid="cc-accept"]'
        )
        btn.click()

    def confirm_successful_signup_or_login(self):
        try:
            profile_img_locator = (
                By.CSS_SELECTOR,
                'button[data-testid="cypress-headernav-profile"] img'
            )
            wait = WebDriverWait(self.driver, 25)
            wait.until(EC.presence_of_element_located(profile_img_locator))
            self.driver.find_element(*profile_img_locator)
            return True
        except NoSuchElementException as e:
            print(e)
            return False

    # To be called after signup_with_email() has been successful
    def save_credentials_to_env(self, email, password):
        key, encrypted_password = pw_encrypt.encrypt_password(password)
        with open('../.env', 'a') as file:
            file.write(f'EMAIL={email}\n')
            file.write(f'KEY={key.decode()}\n')
            file.write(f'PASSWORD={encrypted_password.decode()}\n')

    # Simple method to get password from env file
    def retrieve_password_from_env(self):
        password = pw_decrypt.get_password()
        return password
    
    def save_password_in_cookies(self):
        ...
