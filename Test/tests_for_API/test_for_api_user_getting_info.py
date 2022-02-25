import requests
import Test.tests_for_API.conftest as conftest
from Test.tests_for_API.data_for_api import APIdata


# user getting info
class Tests_for_user_login:
    class Tests_positive:
        def test_login_user(self, logs_API):
            """This case checks, that there is opportunity for user to login"""
            response = requests.get(APIdata.REQUEST_FOR_GETTING_USER_INFO)
            json_response = response.json()
            conftest.pars_for_creation_user(json_response)
            try:
                assert response.status_code == APIdata.STATUS_CODE_200, f"There is no info by request user, status code -> {response.status_code}"
            except AssertionError as err:
                logs_API.error(f"There is no info by request user, status code -> {response.status_code}")
                raise err

    class Tests_negative:
        def test_login_incorrect_user(self, logs_API):
            """This case checks, that there is no opportunity to login user with incorrect username"""
            response = requests.get(APIdata.REQUEST_FOR_GETTING_INFO_INCORRECT_USER)
            json_response = response.json()
            conftest.pars_for_creation_user(json_response)
            try:
                assert response.status_code == APIdata.STATUS_CODE_404, f"There is info by request user, status code -> {response.status_code}"
            except AssertionError as err:
                logs_API.error(f"There is no info by request user, status code -> {response.status_code}")
                raise err
