import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from data import DataUser
from locators import Locators
from curl import main_site, registration_site, recovery_password_site
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="session")
def driver_main():
    browser = webdriver.Chrome()
    browser.get(main_site)
    yield browser
    browser.quit()

@pytest.fixture(scope="function")
def driver_reg():
    browser = webdriver.Chrome()
    browser.get(registration_site)
    yield browser
    browser.quit()

@pytest.fixture(scope="function")
def driver_recovery_password():
    browser = webdriver.Chrome()
    browser.get(recovery_password_site)
    yield browser
    browser.quit()

@pytest.fixture(scope="function")
def driver_log_account():
    browser = webdriver.Chrome()
    browser.get(main_site)
    browser.find_element(*Locators.BUTTON_LOG_MAIN).click()
    WebDriverWait(browser, 5).until(ec.visibility_of_element_located(Locators.LABEL_LOGIN))
    browser.find_element(*Locators.LOG_EMAIL).send_keys(DataUser.email)
    browser.find_element(*Locators.LOG_PASSWORD).send_keys(DataUser.password)
    browser.find_element(*Locators.BUTTON_LOGIN).click()
    WebDriverWait(browser, 5).until(ec.visibility_of_element_located(Locators.LABEL_COLLECT_BURGER))
    yield browser
    browser.quit()