import pytest
import logging as logger

from dodocs.src.utilities.generic_utility import generate_unique_email_password

@pytest.mark.test29
def test_create_customer_only_email_password():

    logger.info("TEST: Create customer's only email and password")
    # email should be unique for every call

    rand_info = generate_unique_email_password()
    email = rand_info['email']
    password = rand_info['password']

    # create payload
    payload = {'email': email, 'password': password}

    # make the api call

    # verify status code of the call

    # verify email in the response

    # verify customer is created in the database
