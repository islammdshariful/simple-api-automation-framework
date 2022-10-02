from clients.base_client import BaseAuthClient


class LoginRegistration(BaseAuthClient):
    def __init__(self):
        super().__init__()

    def login(self, email, password):
        url = f'{self.base_url}/auth/login'
        payload = {
            "email": email,
            "password": password
        }
        response = self.request.post(url, payload)
        return response

    def registration(self, email, password):
        url = f'{self.base_url}/auth/register'
        payload = {
            "email": email,
            "password": password
        }
        response = self.request.post(url, payload)
        return response
