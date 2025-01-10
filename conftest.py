import pytest
from selenium import webdriver


@pytest.fixture()
def browser():
    browser_object = webdriver.Chrome()
    yield browser_object
    browser_object.quit()

