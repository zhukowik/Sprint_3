from selenium.webdriver.support.expected_conditions import WebDriverOrWebElement
from selenium.webdriver.support.wait import WebDriverWait
from curl import personal_account, main_site, login_site
from locators import Locators
from selenium.webdriver.support import expected_conditions as ec

class TestTransition:


    def test_transition_to_personal_account(self, driver_log_account):
        driver_log_account.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver_log_account, 5).until(ec.visibility_of_element_located(Locators.LABEL_PROFILE))
        assert driver_log_account.current_url == personal_account

    def test_transition_from_personal_account_to_constructor(self, driver_log_account):
        driver_log_account.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver_log_account, 5).until(ec.visibility_of_element_located(Locators.LABEL_PROFILE))
        driver_log_account.find_element(*Locators.BUTTON_CONSTRUCTOR).click()
        WebDriverWait(driver_log_account, 5).until(ec.visibility_of_element_located(Locators.LABEL_COLLECT_BURGER))
        assert driver_log_account.current_url == main_site

    def test_exit_account(self, driver_log_account):
        driver_log_account.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver_log_account, 5).until(ec.visibility_of_element_located(Locators.LABEL_PROFILE))
        driver_log_account.find_element(*Locators.BUTTON_EXIT_ACCOUNT).click()
        WebDriverWait(driver_log_account, 4).until(ec.visibility_of_element_located(Locators.LABEL_LOGIN))
        assert driver_log_account.current_url == login_site

    def test_transition_bun(self, driver_main):
        driver_main.find_element(*Locators.BUTTON_FILLING).click()
        WebDriverWait(driver_main, 5).until(ec.visibility_of_element_located(Locators.LABEL_FILLING))
        driver_main.find_element(*Locators.BUTTON_BUN).click()
        text = WebDriverWait(driver_main, 5).until(ec.visibility_of_element_located(Locators.LABEL_BUN)).text
        assert text == "Булки"

    def test_transition_sauce(self, driver_main):
        driver_main.find_element(*Locators.BUTTON_FILLING).click()
        WebDriverWait(driver_main, 5).until(ec.visibility_of_element_located(Locators.LABEL_FILLING))
        driver_main.find_element(*Locators.BUTTON_SAUCE).click()
        text = WebDriverWait(driver_main, 5).until(ec.visibility_of_element_located(Locators.LABEL_SAUCE)).text
        assert text == "Соусы"

    def test_transition_filling(self, driver_main):
        driver_main.find_element(*Locators.BUTTON_FILLING).click()
        text = WebDriverWait(driver_main, 5).until(ec.visibility_of_element_located(Locators.LABEL_FILLING)).text
        assert text == "Начинки"