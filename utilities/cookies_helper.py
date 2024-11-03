import pickle
import os

DEFAULT_COOKIES_PATH = os.path.join('..',
                                    'cookies',
                                    'default_login_cookies.pkl')

def save_cookies(driver, path=DEFAULT_COOKIES_PATH):
    with open(path, 'wb') as file:
        pickle.dump(driver.get_cookies(), file)

def load_cookies(driver, path=DEFAULT_COOKIES_PATH):
    with open(path, 'rb') as file:
        cookies = pickle.load(file)
        for cookie in cookies:
            driver.add_cookie(cookie)
