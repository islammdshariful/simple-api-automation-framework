from json import dumps
from clients.base_client import BaseClient, BaseAuthClient
from tests.helpers.user_helpers import get_a_user_payload


class UserClient(BaseClient):
    def __init__(self):
        super().__init__()

    def __get_user_url(self, user_id=None):
        if user_id is None:
            return f'{self.base_url}/users/'
        else:
            return f'{self.base_url}/users/{user_id}'

    def read_all_user(self):
        return self.request.get(self.__get_user_url(), self.headers)

    def read_one_user_by_id(self, user_id):
        return self.request.get(self.__get_user_url(user_id))

    def create_user(self, body=None):
        slug, response = self.__create_user(body)
        return slug, response

    def __create_user(self, body=None):
        if body is None:
            user = get_a_user_payload()
            slug = user['slug']
            payload = dumps(user)
        else:
            slug = body['slug']
            payload = dumps(body)

        response = self.request.post(self.__get_user_url(), payload, self.headers)
        return slug, response

    def update_user(self, user_id, payload):
        return self.request.put(self.__get_user_url(user_id), payload, self.headers)

    def delete_user(self, user_id):
        return self.request.delete(self.__get_user_url(user_id))


class UserAuthClient(BaseAuthClient):
    def __init__(self):
        super().__init__()

    def __get_user_url(self, user_id=None):
        if user_id is None:
            return f'{self.base_url}/users/'
        else:
            return f'{self.base_url}/users/{user_id}'

    def read_all_user(self, token=None):
        if token is not None:
            self.headers["Authorization"] = f'Bearer {token}'
            return self.request.get(self.__get_user_url(), self.headers)
        else:
            print('NO TOKEN IS PASSED WITH THE HEADERS')

    def read_one_user_by_id(self, user_id, token=None):
        if token is not None:
            self.headers["Authorization"] = f'Bearer {token}'
            return self.request.get(self.__get_user_url(user_id), self.headers)
        else:
            print('NO TOKEN IS PASSED WITH THE HEADERS')

    def create_user(self, body=None, email=None, token=None):
        email, slug, response = self.__create_user(body=body, email=email, token=token)
        return email, slug, response

    def __create_user(self, body=None, email=None, token=None):
        if body is None:
            user = get_a_user_payload(email)
            slug = user['slug']
            payload = dumps(user)
        else:
            slug = body['slug']
            payload = dumps(body)

        if token is not None:
            self.headers["Authorization"] = f'Bearer {token}'
        response = self.request.post(self.__get_user_url(), payload, self.headers)
        return email, slug, response

    def update_user(self, user_id, payload, token):
        if token is not None:
            self.headers["Authorization"] = f'Bearer {token}'
            return self.request.put(self.__get_user_url(user_id), payload, self.headers)
        else:
            print('NO TOKEN IS PASSED WITH THE HEADERS')

    def delete_user(self, user_id, token):
        if token is not None:
            print(token)
            self.headers["Authorization"] = f'Bearer {token}'
            return self.request.delete(self.__get_user_url(user_id), self.headers)
        else:
            print('NO TOKEN IS PASSED WITH THE HEADERS')
