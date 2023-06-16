import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    #driver = webdriver.Chrome(executable_path="./driver/chromedriver")
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

