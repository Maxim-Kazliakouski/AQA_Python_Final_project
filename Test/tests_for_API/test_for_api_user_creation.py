import requests
import Test.tests_for_API.conftest as conftest
from Test.tests_for_API.data_for_api import APIdata


# user creation
class Tests_for_user_creation:
    class Tests_positive:
        def test_create_user(self, logs_API):
            """This case checks, that there is opportunity to created user"""
            response = requests.post(APIdata.REQUEST_FOR_USER_CREATION, json=APIdata.DATA_FOR_USER_CREATION)
            json_response = response.json()
            conftest.pars_for_creation_user(json_response)
            try:
                assert response.status_code == APIdata.STATUS_CODE_200, f"User hasn't been created, status code -> {response.status_code}"
            except AssertionError as err:
                logs_API.error(f"User hasn't been created, status code -> {response.status_code}")
                raise err

        def test_create_user_without_id(self, logs_API):
            """This case checks, that there is opportunity to created user without id"""
            response = requests.post(APIdata.REQUEST_FOR_USER_CREATION, json=APIdata.DATA_FOR_USER_CREATION_WITHOUT_ID)
            json_response = response.json()
            conftest.pars_for_creation_user(json_response)
            try:
                assert response.status_code == APIdata.STATUS_CODE_200, f"User hasn't been created, status code -> {response.status_code}"
            except AssertionError as err:
                logs_API.error(f"User hasn't been created, status code -> {response.status_code}")
                raise err

        def test_create_user_without_username(self, logs_API):
            """This case checks, that there is opportunity to created user without username"""
            response = requests.post(APIdata.REQUEST_FOR_USER_CREATION,
                                     json=APIdata.DATA_FOR_USER_CREATION_WITHOUT_USERNAME)
            json_response = response.json()
            conftest.pars_for_creation_user(json_response)
            try:
                assert response.status_code == APIdata.STATUS_CODE_200, f"User hasn't been created, status code -> {response.status_code}"
            except AssertionError as err:
                logs_API.error(f"User hasn't been created, status code -> {response.status_code}")
                raise err

        def test_create_user_without_firstname(self, logs_API):
            """This case checks, that there is opportunity to created user without firstname"""
            response = requests.post(APIdata.REQUEST_FOR_USER_CREATION,
                                     json=APIdata.DATA_FOR_USER_CREATION_WITHOUT_FIRSTNAME)
            json_response = response.json()
            conftest.pars_for_creation_user(json_response)
            try:
                assert response.status_code == APIdata.STATUS_CODE_200, f"User hasn't been created, status code -> {response.status_code}"
            except AssertionError as err:
                logs_API.error(f"User hasn't been created, status code -> {response.status_code}")
                raise err

        def test_create_user_without_lastname(self, logs_API):
            """This case checks, that there is opportunity to created user without lastname"""
            response = requests.post(APIdata.REQUEST_FOR_USER_CREATION,
                                     json=APIdata.DATA_FOR_USER_CREATION_WITHOUT_LASTNAME)
            json_response = response.json()
            conftest.pars_for_creation_user(json_response)
            try:
                assert response.status_code == APIdata.STATUS_CODE_200, f"User hasn't been created, status code -> {response.status_code}"
            except AssertionError as err:
                logs_API.error(f"User hasn't been created, status code -> {response.status_code}")
                raise err

        def test_create_user_without_email(self, logs_API):
            """This case checks, that there is opportunity to created user without email"""
            response = requests.post(APIdata.REQUEST_FOR_USER_CREATION,
                                     json=APIdata.DATA_FOR_USER_CREATION_WITHOUT_EMAIL)
            json_response = response.json()
            conftest.pars_for_creation_user(json_response)
            try:
                assert response.status_code == APIdata.STATUS_CODE_200, f"User hasn't been created, status code -> {response.status_code}"
            except AssertionError as err:
                logs_API.error(f"User hasn't been created, status code -> {response.status_code}")
                raise err
                
        def test_create_user_without_password(self, logs_API):
            """This case checks, that there is opportunity to created user without password"""
            response = requests.post(APIdata.REQUEST_FOR_USER_CREATION,
                                     json=APIdata.DATA_FOR_USER_CREATION_WITHOUT_PASSWORD)
            json_response = response.json()
            conftest.pars_for_creation_user(json_response)
            try:
                assert response.status_code == APIdata.STATUS_CODE_200, f"User hasn't been created, status code -> {response.status_code}"
            except AssertionError as err:
                logs_API.error(f"User hasn't been created, status code -> {response.status_code}")
                raise err

        def test_create_user_without_phone(self, logs_API):
            """This case checks, that there is opportunity to created user without phone"""
            response = requests.post(APIdata.REQUEST_FOR_USER_CREATION,
                                     json=APIdata.DATA_FOR_USER_CREATION_WITHOUT_PHONE)
            json_response = response.json()
            conftest.pars_for_creation_user(json_response)
            try:
                assert response.status_code == APIdata.STATUS_CODE_200, f"User hasn't been created, status code -> {response.status_code}"
            except AssertionError as err:
                logs_API.error(f"User hasn't been created, status code -> {response.status_code}")
                raise err

        def test_create_user_without_userstatus(self, logs_API):
            """This case checks, that there is opportunity to created user without userstatus"""
            response = requests.post(APIdata.REQUEST_FOR_USER_CREATION,
                                     json=APIdata.DATA_FOR_USER_CREATION_WITHOUT_USER_STATUS)
            json_response = response.json()
            conftest.pars_for_creation_user(json_response)
            try:
                assert response.status_code == APIdata.STATUS_CODE_200, f"User hasn't been created, status code -> {response.status_code}"
            except AssertionError as err:
                logs_API.error(f"User hasn't been created, status code -> {response.status_code}")
                raise err
                
    class Test_negative:
        def test_create_user_without_data(self, logs_API):
            """This case checks, that there is opportunity to created user without data"""
            response = requests.post(APIdata.REQUEST_FOR_USER_CREATION)
            json_response = response.json()
            conftest.pars_for_creation_user(json_response)
            try:
                assert response.status_code == APIdata.STATUS_CODE_415, f"User has been created, status code -> {response.status_code}"
            except AssertionError as err:
                logs_API.error(f"User hasn't been created, status code -> {response.status_code}")
                raise err
            