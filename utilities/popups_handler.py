from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def close_icons_popup(driver):
    try:
        close_btn = driver.find_element(
            By.CSS_SELECTOR,
            'div[role="dialog"] button[aria-label="Close"]'
        )
        close_btn.click()
    except NoSuchElementException:
        print("Icons popup is not found!")

def close_translations_popup(driver):
    try:
        close_btn = driver.find_element(
            By.CSS_SELECTOR,
            'div[role="dialog"] button[aria-label="Close"]'
        )
        close_btn.click()
    except NoSuchElementException:
        print("Translations popup is not found!")