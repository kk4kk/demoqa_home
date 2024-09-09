import pytest
from selenium import webdriver

# ФИКСТУРА
@pytest.fixture(scope='session')
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()