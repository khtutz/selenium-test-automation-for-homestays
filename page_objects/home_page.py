from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.properties_result_page import PropertiesResultPage
from page_objects.signup_login_page import SignupLoginPage

class HomePage:
    ADULTS = 'adults'
    CHILDREN = 'children'
    INFANTS = 'infants'
    PETS = 'pets'

    def __init__(self, driver):
        self.driver = driver

    def select_currency(self, currency):
        # Click 'Language and Currency' icon at the Home page
        lang_curr_btn = self.driver.find_element(
            By.CSS_SELECTOR,
            'button[aria-label="Choose a language and currency"]'
        )
        lang_curr_btn.click()
        # Select currency tab
        currency_tab = self.driver.find_element(
            By.CSS_SELECTOR,
            'button[id="tab--language_region_and_currency--1"]'
        )
        currency_tab.click()
        # Select the currency
        currency_option = self.driver.find_element(
            By.XPATH,
            f'//li[.//div[text()="{currency}"]]'
        )
        currency_option.click()

    def confirm_current_currency(self):
        # Retrieve currently selected currency for assertions
        currency_displays = self.driver.find_elements(
            By.XPATH,
            '//span[@class="l120a03b atm_cs_10d11i2 atm_rd_8stvzk_1nos8r dir dir-ltr"]')
        return currency_displays[5].text

    def select_destination(self, destination):
        # Enter the destination
        dest_input_locator = (
            By.CSS_SELECTOR,
            'input[data-testid="structured-search-input-field-query"]'
        )
        wait = WebDriverWait(self.driver, 25)
        wait.until(EC.element_to_be_clickable(dest_input_locator))
        dest_input = self.driver.find_element(*dest_input_locator)
        dest_input.send_keys(destination)
        # Wait until autocompleted search results come out
        autocomplete_result_locator = (
            By.CSS_SELECTOR, 
            'div[data-index="0"] div:nth-child(2) div'
        )
        wait.until(EC.text_to_be_present_in_element(
            autocomplete_result_locator,
            destination.capitalize()
        ))
        # Click the result
        destination_result = self.driver.find_element(*autocomplete_result_locator)
        destination_result.click()

    def confirm_destination(self):
        # Retrieve choosen destination for assertion
        dest_input = self.driver.find_element(
            By.CSS_SELECTOR,
            'input[data-testid="structured-search-input-field-query"]'
        )
        return dest_input.get_attribute('value')

    def add_checkin_and_checkout_dates(self, checkin_date, checkout_date):
        # Choose check in date
        checkin_date = self.driver.find_element(
            By.CSS_SELECTOR,
            f'div[data-testid="{checkin_date}"]'
        )   
        checkin_date.click()
        # Choose check out date
        checkout_date = self.driver.find_element(
            By.CSS_SELECTOR,
            f'div[data-testid="{checkout_date}"]'
        )
        checkout_date.click()

    def confirm_checkin_and_checkout_dates(self):
        # Retrieve selected dates for assertion
        checkin_date = self.driver.find_element(
            By.CSS_SELECTOR,
            'div[data-testid="structured-search-input-field-split-dates-0"] div div:nth-child(2)'
        )
        checkout_date = self.driver.find_element(
            By.CSS_SELECTOR,
            'div[data-testid="structured-search-input-field-split-dates-1"] div div:nth-child(2)'
        )
        return checkin_date.text, checkout_date.text

    def add_guests(
        self,
        adults=1,
        children=0,
        infants=0,
        pets=0
    ):
        # Select to add guests
        add_guests = self.driver.find_element(
            By.CSS_SELECTOR,
            'div[data-testid="structured-search-input-field-guests-button"]'
        )
        add_guests.click()
        # Add different types of guests
        if adults >= 1:
            self.add_in_guests(adults, self.ADULTS)
        if children >= 1:
            self.add_in_guests(children, self.CHILDREN)
        if infants >= 1:
            self.add_in_guests(infants, self.INFANTS)
        if pets >= 1:
            self.add_in_guests(pets, self.PETS)


    def add_in_guests(self, guests, guest_type):
        add_guests = self.driver.find_element(
            By.CSS_SELECTOR,
            f'button[data-testid="stepper-{guest_type}-increase-button"]'
        )
        for i in range(0, guests):
            add_guests.click()

    def confirm_guests(self):
        guests = self.driver.find_element(
            By.CSS_SELECTOR,
            'div[data-testid="structured-search-input-field-guests-button"] div div:nth-child(2)'
        )
        return guests.text

    def search_and_get_result_page(self):
        self.search_properties()
        properties_result_page = self.get_properties_result_page()
        return properties_result_page

    def search_properties(self):
        search_btn = self.driver.find_element(
            By.CSS_SELECTOR,
            'button[data-testid="structured-search-input-search-button"]'
        )
        search_btn.click()

    def get_properties_result_page(self):
        page = PropertiesResultPage(self.driver)
        return page

    def load_signup_login_page(self, url):
        self.driver.get(url)
        signup_login_page = self.get_signup_login_page()
        return signup_login_page

    def get_signup_login_page(self):
        page = SignupLoginPage(self.driver)
        return page