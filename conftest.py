import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from data import DataUser
from locators import Locators
from curl import MAIN_SITE, REGISTRATION_SITE, RECOVERY_PASSWORD_SITE
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="session")
def driver_main():
    browser = webdriver.Chrome()
    browser.get(MAIN_SITE)
    yield browser
    browser.quit()

@pytest.fixture(scope="function")
def driver_reg():
    browser = webdriver.Chrome()
    browser.get(REGISTRATION_SITE)
    yield browser
    browser.quit()

@pytest.fixture(scope="function")
def driver_recovery_password():
    browser = webdriver.Chrome()
    browser.get(RECOVERY_PASSWORD_SITE)
    yield browser
    browser.quit()

@pytest.fixture(scope="function")
def driver_log_account():
    browser = webdriver.Chrome()
    browser.get(MAIN_SITE)
    browser.find_element(*Locators.BUTTON_LOG_MAIN).click()
    WebDriverWait(browser, 5).until(ec.visibility_of_element_located(Locators.LABEL_LOGIN))
    browser.find_element(*Locators.LOG_EMAIL).send_keys(DataUser.email)
    browser.find_element(*Locators.LOG_PASSWORD).send_keys(DataUser.password)
    browser.find_element(*Locators.BUTTON_LOGIN).click()
    WebDriverWait(browser, 5).until(ec.visibility_of_element_located(Locators.LABEL_COLLECT_BURGER))
    yield browser
    browser.quit()