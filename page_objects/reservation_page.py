from selenium.webdriver.common.by import By
from page_objects.payment_page import ConfirmAndPayPage
import re

class ReservationPage():
    def __init__(self, driver):
        self.driver = driver

    def reserve_and_get_payment_page(self):
        self.reserve_the_property()
        payment_page = self.get_payment_page()
        return payment_page

    def reserve_the_property(self):
        reserve_btn = self.driver.find_element(
            By.CSS_SELECTOR,
            'div[class="_fz3zdn"] > div > button[data-testid="homes-pdp-cta-btn"]'
        )
        reserve_btn.click()

    def confirm_amenities(self):
        # Retrieve names of amenities offered by the place for assertion
        self.show_all_amenities()
        amenities = self.driver.find_elements(
            By.CSS_SELECTOR,
            'div[class="_11jhslp"] ul > li'
        )
        amenity_names = []
        for amenity in amenities:
            amenity_names.append(amenity.text)
        self.close_show_all_amenities()
        return amenity_names

    def show_all_amenities(self):
        # Click the button to display all amentities
        show_all_btn = self.driver.find_element(
            By.XPATH,
            '//button[contains(text(), "Show all") and contains(text(), "amenities")]'
        )
        show_all_btn.click()

    def close_show_all_amenities(self):
        close_btn = self.driver.find_element(
            By.CSS_SELECTOR,
            'div[data-testid="modal-container"] button'
        )
        close_btn.click()

    def confirm_price_per_night(self):
        # Retrieve the price per night without service fees, and before tax for assertion
        amount_element = self.driver.find_elements(
            By.CSS_SELECTOR,
            'span[class="_11jcbg2"]')[1]
        number = re.sub(r'\D', '', amount_element.text) # Remove currency symbol
        return float(number)

    def get_payment_page(self):
        payment_page = ConfirmAndPayPage(self.driver)
        return payment_page
    