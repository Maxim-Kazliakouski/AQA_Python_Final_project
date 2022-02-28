import requests
import Test.tests_for_API.conftest as conftest
from Test.tests_for_API.data_for_api import APIdata


# user login/logout
class Tests_for_user_login_logout:
    class Tests_positive:
        def test_login_user(self, logs_API):
            """This case checks, that there is opportunity to login user"""
            response = requests.get(APIdata.REQUEST_FOR_USER_LOGIN, params=APIdata.PARAMS_FOR_USER_LOGIN)
            json_response = response.json()
            conftest.pars_for_creation_user(json_response)
            try:
                assert response.status_code == APIdata.STATUS_CODE_200, f"User hasn't been login, status code -> {response.status_code}"
            except AssertionError as err:
                logs_API.error(f"User hasn't been login, status code -> {response.status_code}")
                raise err

        def test_logout_user(self, logs_API):
            """This case checks, that there is opportunity to logout user"""
            response = requests.get(APIdata.REQUEST_FOR_USER_LOGOUT)
            json_response = response.json()
            conftest.pars_for_creation_user(json_response)
            try:
                assert response.status_code == APIdata.STATUS_CODE_200, f"User hasn't been logout, status code -> {response.status_code}"
            except AssertionError as err:
                logs_API.error(f"User hasn't been login, status code -> {response.status_code}")
                raise err

        def test_delete_user(self, logs_API):
            """This case checks, that there is opportunity to delete user"""
            response = requests.delete(APIdata.REQUEST_FOR_DELETE_USER)
            try:
                assert response.status_code == APIdata.STATUS_CODE_200, f"User has already deleted and not found, status code -> {response.status_code}"
            except AssertionError as err:
                logs_API.error(f"User hasn't been login, status code -> {response.status_code}")
                raise err
