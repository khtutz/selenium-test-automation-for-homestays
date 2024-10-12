from selenium.webdriver.common.by import By

from utilities.base_class import BaseClass
from utilities import popups_handler
from page_objects.home_page import HomePage
from page_objects.properties_result_page import PropertiesResultPage
from page_objects.reservation_page import ReservationPage
from page_objects.payment_page import ConfirmAndPayPage

class TestEndToEnd(BaseClass):
    def test_endtoend(self):
        # Setup logging
        log = self.get_logger()
        log.info('-----Start of Booking Testing-----')
        
        # Home page
        home_page = HomePage(self.driver)
        log.info('Home page: selecting currency, destination, dates, and guest.')

        # Currency
        home_page.select_currency('USD – $')
        selected_currency = home_page.confirm_current_currency()
        assert selected_currency == 'USD', 'Currency mismatch'
        
        # Destination/Location
        home_page.select_destination('bali')
        selected_destination = home_page.confirm_destination()
        assert selected_destination == 'Bali, Indonesia', 'Destination mismatch'
        
        # Dates
        home_page.add_checkin_and_checkout_dates('11/18/2024', '11/20/2024')
        selected_dates = home_page.confirm_checkin_and_checkout_dates()
        assert selected_dates == ('Nov 18', 'Nov 20'), 'Check-in and check-out dates mismatch'
        
        # Guests
        home_page.add_guests(adults=2, pets=1)
        selected_guests = home_page.confirm_guests()
        assert selected_guests == '2 guests, 1 pet', 'Number and/or type of guest mismatch'

        properties_result_page : PropertiesResultPage = home_page.search_and_get_result_page()
        
        # Properties result page
        log.info('Properties result page: Applying filters to list desired locations.')
        min_price = 45
        max_price = 450
        amenities = [
            properties_result_page.AMENITY_OPTIONS['Hair dryer'], 
            properties_result_page.AMENITY_OPTIONS['Air conditioning'], 
            properties_result_page.AMENITY_OPTIONS['Iron']
        ]
        properties_result_page.apply_all_filters(
            type_of_place=properties_result_page.ENTIRE_HOME,
            min_price=min_price,
            max_price=max_price,
            bathrooms=2,
            property_type=properties_result_page.HOUSE,
            amenities=amenities,
            booking_options=[
                properties_result_page.BOOKING_OPTIONS['Allows pets']
            ]
        )
        reservation_page : ReservationPage = properties_result_page.choose_property_and_get_reservation_page()
        
        # Property reservation page
        log.info('Property reservation page: Checking expected items, and proceeding to reserve.')
        opened_windows = self.driver.window_handles
        self.driver.switch_to.window(opened_windows[1])
        popups_handler.close_translations_popup(self.driver)

        # Price per night
        price = reservation_page.confirm_price_per_night()
        assert min_price <= price <= max_price, 'Price for a night stay mismatch'

        # Amentities
        requested_amenities = properties_result_page.applied_filters['amenities']
        offered_amenities = reservation_page.confirm_amenities()
        for amenity in requested_amenities:
            assert amenity in offered_amenities, f'Expected amenity {amenity} not found in property amenities'

        payment_page : ConfirmAndPayPage = reservation_page.reserve_and_get_payment_page()

        # To proceed with payment, and confirmation
        log.info('Proceeding to the payment page.')
        log.info('-----End of Booking Testing-----')