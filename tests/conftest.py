from selenium import webdriver

import pytest
import os
import time

import tests.constants as const 

driver = None

# Ref: https://docs.pytest.org/en/7.1.x/example/simple.html
def pytest_addoption(parser):
    parser.addoption(
        '--browser_name', 
        action='store', 
        default='chrome'
    )

@pytest.fixture(scope='class')
def setup(request):
    global driver
    # Capture browser name from CLI
    browser_name = request.config.getoption('browser_name')
    if browser_name == 'chrome':
        driver = setup_chrome()
    elif browser_name == 'firefox':
        ...
    else:
        ...
    driver.get(const.BASE_URL)
    #driver.maximize_window()
    driver.implicitly_wait(20)
    request.cls.driver = driver
    yield
    time.sleep(4)
    driver.quit()

def setup_chrome():
    #os.environ['PATH'] += const.CHROME_DRIVER_PATH
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    return webdriver.Chrome(options=options)

def pytest_runtest_makereport(item):
    ...