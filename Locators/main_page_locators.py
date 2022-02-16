from selenium.webdriver.common.by import By


class MainPageLocators:

    GO_TO_ADMIN_BUTTON = By.CLASS_NAME, 'btn.btn-primary.my-2'
    USERNAME_FIELD = By.NAME, 'username'
    PASSWORD_FIELD = By.NAME, 'password'
    LOGIN_BUTTON = By.XPATH, '//*[@id="login-form"]/div[3]/input'
    POST_DATE = By.XPATH, "//small[contains(text(),'Feb. 10')]"