
# Test Automation Documentation

## Overview
This document outlines the testing features such as end-to-end booking, signing up, and logging in, from guest perspective, for Airbnb website using Selenium with Python. The test case automates the process of registering user, selecting currency, choosing desired destination, selecting staying dates, filtering the result, and making a reservation.

## Test Objective
The objective of the test is to ensure the correct functionalities of the followings:
- Reservation: Selections of destination, dates, offered amenties, filtering, and booking of the property
- Account registration: filling the form with valid email, password, name, and date of birth
- Account log-in: signing in with valid credentials - email and password

## Test Scope
### Reservation
1. **Selecting Currency:** Ensure that the selected currency is applied correctly.
2. **Selecting Destination:** Verify that the chosen destination is reflected in the search.
3. **Selecting Dates:** Validate that the selected check-in and check-out dates match the expected values.
4. **Adding Guests:** Confirm the correct number and type of guests are added.
5. **Property Filters:** Apply filters for property type, price range, amenities, and booking options.
6. **Reservation Page Validation:** Ensure the selected property meets the filter criteria (price, amenities, etc.).
7. **Price and Amenity Verification:** Confirm the displayed price and amenities match the applied filters.
8. **Proceeding to Payment:** Successfully navigate to the payment page.

### Account Registration
#### Account Registration with Email
1. **Filling the Email Address** Enter valid email address, and confirm to proceed to sign-up form page
2. **Filling the Gest Name, and Contact Information** Ensure first name, last name, and valid email can be entered
3. **Date of Birth** Verify that only valid date of birth can be entered
4. **Password** Ensure that only valid password can be provided
5. **Proceeding to Sign Up** Verify that account is successfully created after entering confirmation code sent to email 

### Account Log-in
1. **Filling the Email Address** Enter the registered address
2. **Filling the Password** Ensure that password is ready to be entered after entering registered email address
3. **Proceeding to Sign In** Verify that account is successfully logged in after entering the valid password is entered

## Key Assertions for Reservation
The following assertions are made in the test to validate the functionality:
- Currency selected is USD.
- Destination is set to 'Bali, Indonesia'.
- Check-in and check-out dates are 'Nov 18' and 'Nov 20', respectively.
- The number of guests (2 adults and 1 pet) matches the expected input.
- Price per night is within the specified range ($45 - $450).
- All requested amenities (Hair dryer, Air conditioning, Iron) are present on the reservation page.

## Logging
Logging is implemented at each key step for better traceability and debugging. Important test actions and assertions are logged for review.

## Test Execution
The test is executed on a simulated environment using Selenium WebDriver for Chrome. The test uses the Page Object Model (POM) structure to abstract interactions with different pages.

### Test Classes: 
- `TestEndToEnd`: contains the full test scenario, interacting with the HomePage, PropertiesResultPage, and ReservationPage.
- `TestSignUp`: contains the account registration scenario, interacting with the HomePage, and SignupLoginPage
- `TestLogIn`: contains the account sign-in scenario, interacting with the HomePage, and SignupLoginPage


## Conclusion
These tests help ensure that the core booking functionality, and account creation of the website work as expected under a variety of conditions.
