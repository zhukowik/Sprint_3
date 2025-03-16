from selenium.webdriver.common.by import By


class Locators:
    # Локаторы для регистрации
    NAME = (By.XPATH, ".//fieldset[1]/div/div/input")
    REG_EMAIL = (By.XPATH, ".//fieldset[2]/div/div/input")
    REG_PASSWORD = (By.NAME, "Пароль")
    BUTTON_REG = (By.XPATH, ".//button[text()='Зарегистрироваться']")
    LABEL_LOGIN = (By.XPATH, ".//h2[text()='Вход']")
    ERROR_PASSWORD = (By.XPATH, ".//p[text()='Некорректный пароль']")

    #Локаторы для авторизации пользователя
    BUTTON_LOG_MAIN = (By.XPATH, ".//button[text()='Войти в аккаунт']")
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, "//*[@id='root']/div/header/nav/a/p")
    LOG_EMAIL = (By.XPATH, ".//fieldset[1]/div/div/input")
    LOG_PASSWORD = (By.NAME, "Пароль")
    BUTTON_LOGIN = (By.XPATH, ".//button[text()='Войти']")
    LABEL_COLLECT_BURGER = (By.XPATH, ".//h1[text()='Соберите бургер']")
    BUTTON_LOG_IN_REG = (By.CLASS_NAME, "Auth_link__1fOlj")
    BUTTON_LOG_IN_REC_PASSWORD = (By.CLASS_NAME, "Auth_link__1fOlj")

    # Локаторы для переходов
    LABEL_PROFILE = (By.XPATH, ".//a[text()='Профиль']")
    BUTTON_CONSTRUCTOR = (By.XPATH, ".//p[text()='Конструктор']")
    BUTTON_EXIT_ACCOUNT = (By.XPATH, ".//button[text()='Выход']")
    LABEL_BUN = (By.XPATH, ".//h2[text()='Булки']")
    LABEL_SAUCE = (By.XPATH, ".//h2[text()='Соусы']")
    LABEL_FILLING = (By.XPATH, ".//h2[text()='Начинки']")
    BUTTON_FILLING = (By.XPATH, ".//span[text()='Начинки']")
    BUTTON_SAUCE = (By.XPATH, ".//span[text()='Соусы']")
    BUTTON_BUN = (By.XPATH, ".//span[text()='Булки']")