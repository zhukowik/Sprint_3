from selenium.webdriver.common.by import By


class Locators:
    # Локаторы для регистрации
    NAME = (By.XPATH, ".//label[text()='Имя']/following-sibling::input")
    REG_EMAIL = (By.XPATH, ".//label[text()='Email']/following-sibling::input")
    REG_PASSWORD = (By.NAME, "Пароль")
    BUTTON_REG = (By.XPATH, ".//button[text()='Зарегистрироваться']")
    LABEL_LOGIN = (By.XPATH, ".//h2[text()='Вход']")
    ERROR_PASSWORD = (By.XPATH, ".//p[text()='Некорректный пароль']")

    #Локаторы для авторизации пользователя
    BUTTON_LOG_MAIN = (By.XPATH, ".//button[text()='Войти в аккаунт']")
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, ".//p[text()='Личный Кабинет']")
    LOG_EMAIL = (By.XPATH, ".//label[text()='Email']/following-sibling::input")
    LOG_PASSWORD = (By.NAME, "Пароль")
    BUTTON_LOGIN = (By.XPATH, ".//button[text()='Войти']")
    LABEL_COLLECT_BURGER = (By.XPATH, ".//h1[text()='Соберите бургер']")
    BUTTON_LOG_IN_REG = (By.CLASS_NAME, "Auth_link__1fOlj")
    BUTTON_LOG_IN_REC_PASSWORD = (By.CLASS_NAME, "Auth_link__1fOlj")

    # Локаторы для переходов
    LABEL_PROFILE = (By.XPATH, ".//a[text()='Профиль']")
    BUTTON_CONSTRUCTOR = (By.XPATH, ".//p[text()='Конструктор']")
    BUTTON_EXIT_ACCOUNT = (By.XPATH, ".//button[text()='Выход']")
    BUTTON_FILLING = (By.XPATH, ".//div[span[text() = 'Начинки']]")
    BUTTON_SAUCE = (By.XPATH, ".//div[span[text() = 'Соусы']]")
    BUTTON_BUN = (By.XPATH, ".//div[span[text() = 'Булки']]")
    FIRST_SAUCE_IN_LIST = (By.XPATH, './/p[text()="Соус Spicy-X"]')
    FIRST_BUN_IN_LIST = (By.XPATH, ".//p[text()='Флюоресцентная булка R2-D3']")
    FIRST_FILLING_IN_LIST = (By.XPATH,'.//p[text()="Мясо бессмертных моллюсков Protostomia"]')
