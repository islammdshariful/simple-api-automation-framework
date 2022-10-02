import requests
from json import dumps

from clients.users.user_client import UserClient
from tests.assertions.user_assertions import *
from tests.helpers.user_helpers import get_a_user_payload, search_nodes_using_json_path, \
    search_user_with_slug, search_user_with_email

from utils.config import pretty_print

user_client = UserClient()


def test_view_all_users():
    response = user_client.read_all_user()
    pretty_print(response.as_dict)
    assert_status_code(actual_code=response.status_code, expected_code=requests.codes.ok,
                       description='No User Found')


def test_search_one_user():
    user_id = 1
    response = user_client.read_one_user_by_id(str(user_id))
    pretty_print(response.as_dict)
    assert_status_code(actual_code=response.status_code, expected_code=requests.codes.ok,
                       description=f'User with ID: {user_id} not Found')


def test_search_a_user_with_email():
    email = 'kelleymichele@example.com'
    response = user_client.read_all_user()
    assert_status_code(actual_code=response.status_code, expected_code=requests.codes.ok)
    assert_user_have_in_users_with_email(response=response, email=email,
                                         description=f'User with EMAIL: {email} not Found')
    is_new_user_exists = search_user_with_email(response.as_dict, email)
    if assert_that(is_new_user_exists).is_not_empty():
        pretty_print(is_new_user_exists)


def test_register_new_user():
    slug, response = user_client.create_user()
    assert_status_code(actual_code=response.status_code, expected_code=201, description='User not created')

    users = user_client.read_all_user().as_dict
    is_new_user_created = search_user_with_slug(users, slug)
    assert_user_is_present(is_new_user_created)


def test_register_a_new_user_with_a_json_template(create_data):
    user_client.create_user(create_data)

    response = user_client.read_all_user()
    users = response.as_dict

    result = search_nodes_using_json_path(users, json_path="$.[*].slug")

    expected_slug = create_data['slug']
    assert_that(result).contains(expected_slug)


def test_update_a_user():
    user_id = 7
    user = get_a_user_payload()
    payload = dumps(user)
    response = user_client.update_user(user_id, payload)
    assert_status_code(actual_code=response.status_code, expected_code=200, description='User not updated')


def test_delete_a_user():
    user_id = 8
    response = user_client.delete_user(user_id)
    assert_status_code(actual_code=response.status_code, expected_code=200, description='User not deleted')


def test_newly_register_user_can_be_deleted():
    slug, response = user_client.create_user()
    assert_status_code(actual_code=response.status_code, expected_code=201, description='User not created')

    users = user_client.read_all_user().as_dict
    user_id = search_user_with_slug(users, slug)['id']

    response = user_client.delete_user(user_id)
    assert_status_code(actual_code=response.status_code, expected_code=200, description='User not deleted')
