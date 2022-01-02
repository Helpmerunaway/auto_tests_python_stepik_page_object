from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_EMAIL_INPUT = (By.ID, "id_login-username")
    LOGIN_PASSWORD_INPUT = (By.ID, "id_login-password")
    REGISTER_EMAIL_INPUT = (By.ID, "id_registration-email")
    REGISTER_PASSWORD_INPUT = (By.ID, "id_registration-password1")
    REGISTER_PASSWORD_INPUT2 = (By.ID, "id_registration - password2")