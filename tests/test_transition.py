from selenium.webdriver.support.expected_conditions import WebDriverOrWebElement
from selenium.webdriver.support.wait import WebDriverWait
from curl import PERSONAL_ACCOUNT, MAIN_SITE, LOGIN_SITE
from locators import Locators
from selenium.webdriver.support import expected_conditions as ec

class TestTransition:


    def test_transition_to_personal_account(self, driver_log_account):
        driver_log_account.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver_log_account, 5).until(ec.visibility_of_element_located(Locators.LABEL_PROFILE))
        assert driver_log_account.current_url == PERSONAL_ACCOUNT

    def test_transition_from_personal_account_to_constructor(self, driver_log_account):
        driver_log_account.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver_log_account, 5).until(ec.visibility_of_element_located(Locators.LABEL_PROFILE))
        driver_log_account.find_element(*Locators.BUTTON_CONSTRUCTOR).click()
        WebDriverWait(driver_log_account, 5).until(ec.visibility_of_element_located(Locators.LABEL_COLLECT_BURGER))
        assert driver_log_account.current_url == MAIN_SITE

    def test_exit_account(self, driver_log_account):
        driver_log_account.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver_log_account, 5).until(ec.visibility_of_element_located(Locators.LABEL_PROFILE))
        driver_log_account.find_element(*Locators.BUTTON_EXIT_ACCOUNT).click()
        WebDriverWait(driver_log_account, 4).until(ec.visibility_of_element_located(Locators.LABEL_LOGIN))
        assert driver_log_account.current_url == LOGIN_SITE

    def test_transition_bun(self, driver_main):
        driver_main.find_element(*Locators.BUTTON_SAUCE).click()
        driver_main.find_element(*Locators.BUTTON_BUN).click()
        assert driver_main.find_element(*Locators.FIRST_BUN_IN_LIST).text == "Флюоресцентная булка R2-D3"

    def test_transition_sauce(self, driver_main):
        driver_main.find_element(*Locators.BUTTON_SAUCE).click()
        assert driver_main.find_element(*Locators.FIRST_SAUCE_IN_LIST).text == "Соус Spicy-X"

    def test_transition_filling(self, driver_main):
        driver_main.find_element(*Locators.BUTTON_FILLING).click()
        assert driver_main.find_element(
            *Locators.FIRST_FILLING_IN_LIST).text == "Мясо бессмертных моллюсков Protostomia"




