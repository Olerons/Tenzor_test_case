import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os

@pytest.fixture(scope="session")
def browser():
    # -- > Chrome
    service = Service(executable_path=os.path.abspath(r'driver\chromedriver.exe'))
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")  # This make Chromium reachable
    options.add_argument("--no-default-browser-check")  # Overrides default choices
    options.add_argument("--no-first-run")
    options.add_argument("--disable-default-apps")

    driver = webdriver.Chrome(service=service, options=options)

    yield driver
    driver.quit()

