from clients.base_client import BaseAuthClient
from json import dumps
from clients.login_registration.login_registration import LoginRegistration
from clients.users.user_client import UserAuthClient
from tests.assertions.user_assertions import assert_status_code
from tests.helpers.user_helpers import get_a_user_payload, search_nodes_using_json_path, generate_email, \
    generate_password

from utils.config import pretty_print

credentials = LoginRegistration()
client = BaseAuthClient()
user_client = UserAuthClient()


def test_login():
    email = 'bruno@email.com'
    password = 'bruno'
    response = credentials.login(email=email, password=password)
    pretty_print(response.as_dict)
    auth_token = search_nodes_using_json_path(response.as_dict, json_path="$.[*].access_token")[0]
    print(auth_token)


def test_register_user():
    email = generate_email()
    password = generate_password()
    response = credentials.registration(email=email, password=password)
    assert_status_code(actual_code=response.status_code, expected_code=200, description='User not created')
    auth_token = search_nodes_using_json_path(response.as_dict, json_path="$.[*].access_token")[0]

    _, slug, response = user_client.create_user(email=email, token=auth_token)
    pretty_print(response.as_dict)
    assert_status_code(actual_code=response.status_code, expected_code=201, description='User not saved to database')


def test_view_all_users(token):
    response = user_client.read_all_user(token=token)
    assert_status_code(actual_code=response.status_code, expected_code=200,
                       description='No User Found')
    pretty_print(response.as_dict)


def test_search_one_user(token):
    user_id = 3
    response = user_client.read_one_user_by_id(user_id=str(user_id), token=token)
    pretty_print(response.as_dict)
    assert_status_code(actual_code=response.status_code, expected_code=200,
                       description=f'User with ID: {user_id} not Found')


def test_update_a_user(token):
    user_id = 3
    user = get_a_user_payload()
    payload = dumps(user)
    response = user_client.update_user(user_id=user_id, payload=payload, token=token)
    pretty_print(response.as_dict)
    assert_status_code(actual_code=response.status_code, expected_code=200, description='User not updated')


def test_delete_a_user(token):
    user_id = 4
    response = user_client.delete_user(user_id=user_id, token=token)
    pretty_print(response.as_dict)
    assert_status_code(actual_code=response.status_code, expected_code=200, description='User not deleted')
