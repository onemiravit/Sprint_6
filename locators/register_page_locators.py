from selenium.webdriver.common.by import By

class RegisterPageLocators:
    NAME_FIELD = [By.XPATH, "//input[@name='name']"]
    EMAIL_FIELD = [By.XPATH, "//div[label[text()='Email']]/input"]
    PASSWORD_FIELD = [By.XPATH, "//input[@name='Пароль']"]
    REGISTER_BUTTON = [By.XPATH, "//button[text()='Зарегистрироваться']"]