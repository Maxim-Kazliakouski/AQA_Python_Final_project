class APIdata:
    # USER STORE
    URL = 'https://petstore.swagger.io'
    STATUS_CODE_200 = 200
    STATUS_CODE_400 = 400
    STATUS_CODE_415 = 415
    STATUS_CODE_404 = 404
    USERNAME = 'Max91'
    INCORRECT_USERNAME = 'qwery'
    REQUEST_FOR_USER_CREATION = 'https://petstore.swagger.io/v2/user'
    DATA_FOR_USER_CREATION = {
        "id": 0,
        "username": "Max91",
        "firstName": "Maxim",
        "lastName": "Kazliakouski",
        "email": "max@gmail.com",
        "password": "qwery123",
        "phone": "+375291234567",
        "userStatus": 0
    }
    DATA_FOR_USER_CREATION_WITHOUT_ID = {
        "username": "Max91",
        "firstName": "Maxim",
        "lastName": "Kazliakouski",
        "email": "max@gmail.com",
        "password": "qwery123",
        "phone": "+375291234567",
        "userStatus": 1
    }
    DATA_FOR_USER_CREATION_WITHOUT_USERNAME = {
        "id": 0,
        "firstName": "Maxim",
        "lastName": "Kazliakouski",
        "email": "max@gmail.com",
        "password": "qwery123",
        "phone": "+375291234567",
        "userStatus": 1
    }
    DATA_FOR_USER_CREATION_WITHOUT_FIRSTNAME = {
        "id": 0,
        "username": "Max91",
        "lastName": "Kazliakouski",
        "email": "max@gmail.com",
        "password": "qwery123",
        "phone": "+375291234567",
        "userStatus": 1
    }
    DATA_FOR_USER_CREATION_WITHOUT_LASTNAME = {
        "id": 0,
        "username": "Max91",
        "firstName": "Maxim",
        "email": "max@gmail.com",
        "password": "qwery123",
        "phone": "+375291234567",
        "userStatus": 1
    }
    DATA_FOR_USER_CREATION_WITHOUT_EMAIL = {
        "id": 0,
        "username": "Max91",
        "firstName": "Maxim",
        "lastName": "Kazliakouski",
        "password": "qwery123",
        "phone": "+375291234567",
        "userStatus": 1
    }
    DATA_FOR_USER_CREATION_WITHOUT_PASSWORD = {
        "id": 0,
        "username": "Max91",
        "firstName": "Maxim",
        "lastName": "Kazliakouski",
        "email": "max@gmail.com",
        "phone": "+375291234567",
        "userStatus": 1
    }
    DATA_FOR_USER_CREATION_WITHOUT_PHONE = {
        "id": 0,
        "username": "Max91",
        "firstName": "Maxim",
        "lastName": "Kazliakouski",
        "email": "max@gmail.com",
        "password": "qwery123",
        "userStatus": 1
    }
    DATA_FOR_USER_CREATION_WITHOUT_USER_STATUS = {
        "id": 0,
        "username": "Max91",
        "firstName": "Maxim",
        "lastName": "Kazliakouski",
        "email": "max@gmail.com",
        "password": "qwery123",
        "phone": "+375291234567"
    }
    REQUEST_FOR_USER_LOGIN = 'https://petstore.swagger.io/v2/user/login'
    PARAMS_FOR_USER_LOGIN = {'username': 'Max91', 'password': 'qwerty123'}
    REQUEST_FOR_GETTING_USER_INFO = f'https://petstore.swagger.io/v2/user/{USERNAME}'
    REQUEST_FOR_GETTING_INFO_INCORRECT_USER = f'https://petstore.swagger.io/v2/user/{INCORRECT_USERNAME}'
    REQUEST_FOR_USER_LOGOUT = 'https://petstore.swagger.io/v2/user/logout'
    REQUEST_FOR_DELETE_USER = f'https://petstore.swagger.io/v2/user/{USERNAME}'

    # API FOR PET STORE
    REQUEST_FOR_ADDING_PET = "https://petstore.swagger.io/v2/pet"
    RESPONSE_FOR_ADDING = {'id': 10000, 'category': {'id': 2, 'name': 'Jack'}, 'name': 'doggie', 'photoUrls': ['string'],
                           'tags': [{'id': 3, 'name': 'string'}], 'status': 'available'}
    PET_NAME_1 = 'Jack'
    DATA_FOR_ADDING_PET = {
        "id": 10000,
        "category": {
            "id": 2,
            "name": f"{PET_NAME_1}"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 3,
                "name": "string"
            }
        ],
        "status": "available"
    }
    REQUEST_FOR_FINDING_PET_BY_ID = "https://petstore.swagger.io/v2/pet/10000"
    RESPONSE_FOR_FINDING_PET_BY_ID = {'id': 10000, 'category': {'id': 2, 'name': 'Jack'}, 'name': 'doggie',
                                      'photoUrls': ['string'], 'tags': [{'id': 3, 'name': 'string'}],
                                      'status': 'available'}
    REQUEST_FOR_UPDATING_PET_NAME = "https://petstore.swagger.io/v2/pet"
    PET_NAME_2 = 'Russel'
    DATA_FOR_UPDATING_PET_NAME = {
        "id": 10000,
        "category": {
            "id": 2,
            "name": f"{PET_NAME_2}"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 3,
                "name": "string"
            }
        ],
        "status": "available"
    }
    RESPONSE_FOR_UPDATING_PET_NAME = {'id': 10000, 'category': {'id': 2, 'name': 'Russel'},
                                      'name': 'doggie',
                                      'photoUrls': ['string'],
                                      'tags': [{'id': 3, 'name': 'string'}],
                                      'status': 'available'}
    REQUEST_FOR_DELETING_PET = "https://petstore.swagger.io/v2/pet/10000"
