from selenium.webdriver.common.by import By


class MainPageLocators:

    GO_TO_ADMIN_BUTTON = By.CLASS_NAME, 'btn.btn-primary.my-2'
    USERNAME_FIELD = By.NAME, 'username'
    PASSWORD_FIELD = By.NAME, 'password'
    LOGIN_BUTTON = By.XPATH, '//*[@id="login-form"]/div[3]/input'
    POST_DATE = By.XPATH, "//small[contains(text(),'Feb. 10')]"
    NAVBAR_BUTTON = By.CLASS_NAME, "navbar-toggler-icon"
    CONTACT_LIST = By.CLASS_NAME, "list-unstyled"
    ABOUT_INFO = By.CLASS_NAME, "text-muted"
    ALBUM_BUTTON = By.CLASS_NAME, "navbar-brand.d-flex.align-items-center"
