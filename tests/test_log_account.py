from selenium.webdriver.support.wait import WebDriverWait
from data import DataUser
from conftest import driver_main
from curl import MAIN_SITE
from locators import Locators
from selenium.webdriver.support import expected_conditions as ec

class TestLogAccount:


    def test_log_account_in_using_the_log_in_to_account_button_on_the_main_page(self,driver_main):
        driver_main.find_element(*Locators.BUTTON_LOG_MAIN).click()
        WebDriverWait(driver_main, 5).until(ec.visibility_of_element_located(Locators.LABEL_LOGIN))
        driver_main.find_element(*Locators.LOG_EMAIL).send_keys(DataUser.email)
        driver_main.find_element(*Locators.LOG_PASSWORD).send_keys(DataUser.password)
        driver_main.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver_main, 5).until(ec.visibility_of_element_located(Locators.LABEL_COLLECT_BURGER))
        assert driver_main.current_url == MAIN_SITE


    def test_log_account_in_using_the_personal_account_button_on_the_main_page(self, driver_main):
        driver_main.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver_main, 5).until(ec.visibility_of_element_located(Locators.LABEL_LOGIN))
        driver_main.find_element(*Locators.LOG_EMAIL).send_keys(DataUser.email)
        driver_main.find_element(*Locators.LOG_PASSWORD).send_keys(DataUser.password)
        driver_main.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver_main, 5).until(ec.visibility_of_element_located(Locators.LABEL_COLLECT_BURGER))
        assert driver_main.current_url == MAIN_SITE

    def test_log_account_in_using_log_button_on_the_registration_page(self, driver_reg):
        driver_reg.find_element(*Locators.BUTTON_LOG_IN_REG).click()
        WebDriverWait(driver_reg, 5).until(ec.visibility_of_element_located(Locators.LABEL_LOGIN))
        driver_reg.find_element(*Locators.LOG_EMAIL).send_keys(DataUser.email)
        driver_reg.find_element(*Locators.LOG_PASSWORD).send_keys(DataUser.password)
        driver_reg.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver_reg, 5).until(ec.visibility_of_element_located(Locators.LABEL_COLLECT_BURGER))
        assert driver_reg.current_url == MAIN_SITE

    def test_log_account_in_using_log_button_on_the_recovery_password_page(self, driver_recovery_password):
        driver_recovery_password.find_element(*Locators.BUTTON_LOG_IN_REC_PASSWORD).click()
        WebDriverWait(driver_recovery_password, 5).until(ec.visibility_of_element_located(Locators.LABEL_LOGIN))
        driver_recovery_password.find_element(*Locators.LOG_EMAIL).send_keys(DataUser.email)
        driver_recovery_password.find_element(*Locators.LOG_PASSWORD).send_keys(DataUser.password)
        driver_recovery_password.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver_recovery_password, 5).until(ec.visibility_of_element_located(Locators.LABEL_COLLECT_BURGER))
        assert driver_recovery_password.current_url == MAIN_SITE

