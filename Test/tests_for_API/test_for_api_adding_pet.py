import requests
import Test.tests_for_API.conftest as conftest
from Test.tests_for_API.data_for_api import APIdata


# adding pet to the store
class Tests_for_pet_adding:
    class Tests_positive:
        def test_pet_adding(self, deleting_pet, logs_API):
            response = requests.post(APIdata.REQUEST_FOR_ADDING_PET, json=APIdata.DATA_FOR_ADDING_PET)
            json_response = response.json()
            conftest.pars_for_creation_user(json_response)
            try:
                assert response.status_code == APIdata.STATUS_CODE_200, f"Pet hasn't been added, status code -> {response.status_code}"
                # assert json_response == APIdata.RESPONSE_FOR_ADDING, "The response body not as expected"
            except AssertionError as err:
                logs_API.error(f"Pet hasn't been added, status code -> {response.status_code}")
                raise err

        def test_finding_pet_by_id(self, logs_API):
            response = requests.get(APIdata.REQUEST_FOR_FINDING_PET_BY_ID)
            json_response = response.json()
            print(json_response)
            conftest.pars_for_creation_user(json_response)
            try:
                assert response.status_code == APIdata.STATUS_CODE_200, f"Pet hasn't been found by ID, status code -> {response.status_code}"
                assert json_response == APIdata.RESPONSE_FOR_FINDING_PET_BY_ID, "The response body not as expected"
            except AssertionError as err:
                logs_API.error(f"Pet hasn't been found by ID, status code -> {response.status_code}")
                raise err

        def test_updating_pet_name(self, logs_API):
            response = requests.put(APIdata.REQUEST_FOR_UPDATING_PET_NAME, json=APIdata.DATA_FOR_UPDATING_PET_NAME)
            json_response = response.json()
            conftest.pars_for_creation_user(json_response)
            try:
                assert response.status_code == APIdata.STATUS_CODE_200, f"Pet name hasn't been updated, status code -> {response.status_code}"
                assert json_response['category'][
                       'name'] == APIdata.PET_NAME_2, f"The pet name doesn't change on {APIdata.PET_NAME_2}"
            except AssertionError as err:
                logs_API.error(f"The pet name doesn't change on {APIdata.PET_NAME_2}")
                raise err
