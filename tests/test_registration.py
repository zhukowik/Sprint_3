from selenium.webdriver.support.wait import WebDriverWait

from curl import login_site
from helper import generate_registration_data
from locators import Locators
from selenium.webdriver.support import expected_conditions as ec

class TestRegistarationNewUser:

    def test_sucsess_registration(self, driver_reg):
        email, password, name = generate_registration_data()
        driver_reg.find_element(*Locators.NAME).send_keys(name)
        driver_reg.find_element(*Locators.REG_EMAIL).send_keys(email)
        driver_reg.find_element(*Locators.REG_PASSWORD).send_keys(password)
        driver_reg.find_element(*Locators.BUTTON_REG).click()
        WebDriverWait(driver_reg, 4).until(ec.visibility_of_element_located(Locators.LABEL_LOGIN))
        assert driver_reg.current_url == login_site

    def test_registation_error_for_an_incorrect_password(self, driver_reg):
        email,password, name = generate_registration_data()
        driver_reg.find_element(*Locators.NAME).send_keys(name)
        driver_reg.find_element(*Locators.REG_EMAIL).send_keys(email)
        driver_reg.find_element(*Locators.REG_PASSWORD).send_keys("1234")
        driver_reg.find_element(*Locators.BUTTON_REG).click()
        WebDriverWait(driver_reg, 10).until(ec.visibility_of_element_located(Locators.ERROR_PASSWORD))
        assert driver_reg.find_element(*Locators.ERROR_PASSWORD).text == 'Некорректный пароль'