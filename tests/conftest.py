from uuid import uuid4
import pytest

from clients.base_client import BaseAuthClient
from clients.login_registration.login_registration import LoginRegistration
from clients.users.user_client import UserAuthClient
from tests.helpers.user_helpers import search_nodes_using_json_path
from utils.file_reader import read_file

# token = None
credentials = LoginRegistration()
client = BaseAuthClient()
user_client = UserAuthClient()


@pytest.fixture
def create_data():
    payload = read_file('create_user.json')

    payload['slug'] = str(uuid4())

    yield payload


@pytest.fixture(scope='module')
def token():
    response = credentials.login('bruno@email.com', 'bruno')
    auth = search_nodes_using_json_path(response.as_dict, json_path="$.[*].access_token")[0]
    token = auth

    yield token
