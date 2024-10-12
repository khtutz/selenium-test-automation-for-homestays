from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import re

from page_objects.reservation_page import ReservationPage

import time

class PropertiesResultPage():
    # Place types
    ANY_TYPE = 'Any type'
    ROOM = 'Room'
    ENTIRE_HOME = 'Entire home'

    # Property types
    HOUSE = 'House'
    APARTMENT = 'Apartment'
    GUESTHOUSE = 'Guesthouse'
    HOTEL = 'Hotel'

    # Amenities
    AMENITY_OPTIONS =  {
        'Beachfront': 'Beachfront',
        'Pool': 'Pool',
        'Wifi': 'Wifi',
        'Air conditioning': 'Air conditioning',
        'Kitchen': 'Kitchen',
        'Free parking': 'Free parking',
        'Washer': 'Washer',
        'Dryer': 'Dryer',
        'Heating': 'Heating',
        'Dedicated workspace': 'Dedicated workspace',
        'TV': 'TV',
        'Hair dryer': 'Hair dryer',
        'Iron': 'Iron',
        'Hot tub': 'Hot tub',
        'EV charger': 'EV charger',
        'Crib': 'Crib',
        'King bed': 'King bed',
        'Gym': 'Gym',
        'BBQ grill': 'BBQ grill',
        'Breakfast': 'Breakfast',
        'Indoor fireplace': 'Indoor fireplace',
        'Smoking allowed': 'Smoking allowed',
        'Waterfront': 'Waterfront',
        'Smoke alarm': 'Smoke alarm',
        'Carbon monoxide alarm': 'Carbon monoxide alarm'
    }

    # Booking options
    BOOKING_OPTIONS = {
        'Instant Book': 'ib',
        'Self check-in': 'amenities-51',
        'Free cancellation': 'flexible_cancellation',
        'Allows pets': 'pets'
    }

    def __init__(self, driver):
        self.driver = driver

    def apply_all_filters(self, **kwargs):
        self.save_filters(**kwargs)
        self.click_filters_btn()
        # Apply all types of filter
        self.select_type_of_place(
            kwargs.get('type_of_place', self.ANY_TYPE)
        ).select_price_range(
            kwargs.get('min_price', 10),
            kwargs.get('max_price', 300)
        ).select_num_of_rooms_and_beds(
            kwargs.get('bedrooms', 0),
            kwargs.get('beds', 0),
            kwargs.get('bathrooms', 0)
        ).select_property_type(
            kwargs.get('property_type', '')
        ).select_amenities(
            kwargs.get('amenities', [])
        ).select_booking_options(
            kwargs.get('booking_options', [])
        ).show_homes()

    def save_filters(self, **kwargs):
        self.applied_filters = {
            'type_of_place': kwargs.get('type_of_place', self.ANY_TYPE),
            'min_price': kwargs.get('min_price', 10),
            'max_price': kwargs.get('max_price', 300),
            'bedrooms': kwargs.get('bedrooms', 0),
            'beds': kwargs.get('beds', 0),
            'bathrooms': kwargs.get('bathrooms', 0),
            'property_type': kwargs.get('property_type', ''),
            'amenities': kwargs.get('amenities', []),
            'booking_options': kwargs.get('booking_options', [])
        }

    def click_filters_btn(self):
        filter_btn_locator = (
            By.CSS_SELECTOR, 
            'button[data-testid="category-bar-filter-button"]'
        )
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable(filter_btn_locator))
        filter_btn = self.driver.find_element(*filter_btn_locator)
        filter_btn.click()

    def select_type_of_place(self, type_of_place):
        type_of_place_btn = self.driver.find_element(
            By.CSS_SELECTOR,
            f'div[aria-describedby="room-filter-description-{type_of_place}"]'
        )
        type_of_place_btn.click()
        return self
    
    def select_price_range(self, min_price, max_price):
        min_price_input = self.driver.find_element(
            By.ID,
            'price_filter_min'
        )
        min_price_input.send_keys(Keys.CONTROL + 'a')
        min_price_input.send_keys(min_price)
        max_price_input = self.driver.find_element(
            By.ID,
            'price_filter_max'
        )
        max_price_input.send_keys(Keys.CONTROL + 'a')
        max_price_input.send_keys(max_price)
        return self
    
    def select_num_of_rooms_and_beds(self, bedrooms, beds, bathrooms):
        # Select number of bedrooms
        bedrooms_btn = self.driver.find_element(
            By.CSS_SELECTOR,
            f'button[data-testid="stepper-filter-item-min_bedrooms-stepper-increase-button"]'
        )
        for _ in range(bedrooms):
            bedrooms_btn.click()
        # Select number of beds
        beds_btn = self.driver.find_element(
            By.CSS_SELECTOR,
            f'button[data-testid="stepper-filter-item-min_beds-stepper-increase-button"]'
        )
        for _ in range(beds):
            beds_btn.click()
        # Select number of bathrooms
        bathrooms_btn = self.driver.find_element(
            By.CSS_SELECTOR,
            f'button[data-testid="stepper-filter-item-min_bathrooms-stepper-increase-button"]'
        )
        for _ in range(bathrooms):
            bathrooms_btn.click()
        return self

    def select_property_type(self, property_type):
        if property_type:
            propety_type_section = self.driver.find_element(
                By.CSS_SELECTOR,
                'div[id="FILTER_SECTION_CONTAINER:PROPERTY_TYPES_WITH_SUBCATEGORY-row-title"]'
            )
            propety_type_section.click()
            property_btn = self.driver.find_element(
                By.XPATH,
                f'//button/span[contains(text(), "{property_type}")]'
            )
            property_btn.click()
        return self

    def select_amenities(self, amenities):
        show_more_btn = self.driver.find_element(
            By.XPATH,
            '//section[div[div[h2[text()="Amenities"]]]]/div/div/div/button'
        )
        show_more_btn.click()
        for amenity in amenities:
            self.driver.find_element(
                By.XPATH,
                f'//button[span[text()="{amenity}"]]'
            ).click()
        return self
    
    def select_booking_options(self, booking_options):
        for option in booking_options:
            self.driver.find_element(
                By.CSS_SELECTOR,
                f'button[id="filter-item-{option}"]'
            )
        return self

    def show_homes(self):
        homes_link = self.driver.find_element(
            By.XPATH,
            '//a[contains(text(), "Show")]'
        )
        homes_link.click()

    def choose_property_and_get_reservation_page(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.text_to_be_present_in_element((
            By.CSS_SELECTOR,
            'button[data-testid="category-bar-filter-button"] + div'
        ), '7'))
        property = self.driver.find_element(
            By.CSS_SELECTOR,
            'div[class="df8mizf atm_5sauks_glywfm dir dir-ltr"] > div:first-child > div:nth-child(2)'
        )
        property.click()

        reservation_page = ReservationPage(self.driver)
        return reservation_page
