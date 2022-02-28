import logging
import pytest
import requests
from Test.tests_for_API.data_for_api import APIdata


def pars_for_creation_user(json_response):
    print()
    for i, j in json_response.items():
        print(f'{i}: {j}')


@pytest.fixture(scope='session')
def deleting_pet():
    print('\nPreparing for deleting pet before testing...')
    try:
        requests.delete(APIdata.REQUEST_FOR_DELETING_PET)
        return print('Deleting pet was successful')
    except:
        print("Pet hasn't been deleted")


@pytest.fixture(scope='function')
def logs_API():
    # to get the name of the test case file name at runtime
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    # FileHandler class to set the location of log file
    fileHandler = logging.FileHandler('./logfile.log', mode='a', delay=False)
    # Formatter class to set the format of log file
    formatter = logging.Formatter("[%(asctime)s] -- [%(levelname)s][%(lineno)d]--[%(name)s->tests_for_API]: \n%(message)s")
    # object of FileHandler gets formatting info from setFormatter #method
    fileHandler.setFormatter(formatter)
    # logger object gets formatting, path of log file info with addHandler #method
    if logger.hasHandlers():
        logger.handlers.clear()
    logger.addHandler(fileHandler)
    # setting logging level to INFO
    return logger
