class TestDataAdminPage:
    ADMIN_PAGE_LOGIN_URL = 'http://localhost:8000/admin/login/?next=/admin/login'
    USER_NAME_FOR_ADMIN = 'admin'
    PASSWORD_FOR_ADMIN = 'password'
    USERNAME = 'Test'
    PASSWORD = 'maxim05091991'
    ERROR_MESSAGE_DURING_REG_WITHOUT_NAME = 'Please correct the error below.'
    ERROR_MESSAGE_DURING_REG_WITHOUT_PASSWORDS_AT_ALL = 'Please correct the errors below.'
    ERROR_MESSAGE_DURING_REG_WITHOUT_CONFIRMED_PASSWORD = 'Please correct the error below.'
    FORBIDDEN_SYMBOLS_FOR_USERNAME = ['!', '#', '$', '%', '^', '&', '*', '(',
                                      ')', '~', ',', "'", '<', '>', '/',
                                      '=', '?', '|', '{', '}', '[', ']', '±', '§',
                                      ';', '"', ':']
    ERROR_MESSAGE_FORBIDDEN_SYMBOLS_FOR_USERNAME = "Enter a valid username. This value may contain only letters, numbers, and @/./+/-/_ characters."
    