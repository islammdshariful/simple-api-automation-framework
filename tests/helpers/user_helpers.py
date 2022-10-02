from uuid import uuid4

from faker import Faker
from jsonpath_ng import parse


def search_user_with_email(users, email):
    return [user for user in users if user['email'] == email][0]


def search_user_with_slug(users, slug):
    return [user for user in users if user['slug'] == slug][0]


def search_nodes_using_json_path(users, json_path):
    jsonpath_expr = parse(json_path)
    return [match.value for match in jsonpath_expr.find(users)]


def generate_password():
    fake = Faker()
    return fake.password(length=8)


def generate_email():
    fake = Faker()
    return fake.email()


def get_a_user_payload(email=None):
    fake = Faker()
    if email is not None:
        payload = {
            "name": fake.name(),
            "username": fake.profile()['username'],
            "slug": str(uuid4()),
            "email": email,
            "address": {
                "street": fake.street_address(),
                "suite": fake.street_name(),
                "city": fake.city(),
                "zipcode": fake.postcode(),
                "geo": {
                    "lat": f'{fake.latitude()}',
                    "lng": f'{fake.longitude()}'
                }
            },
            "phone": fake.phone_number(),
            "website": fake.url(),
            "company": {
                "name": fake.company(),
                "catchPhrase": fake.catch_phrase(),
                "bs": fake.bs()
            }
        }
    else:
        payload = {
            "name": fake.name(),
            "username": fake.profile()['username'],
            "slug": str(uuid4()),
            "email": fake.email(),
            "address": {
                "street": fake.street_address(),
                "suite": fake.street_name(),
                "city": fake.city(),
                "zipcode": fake.postcode(),
                "geo": {
                    "lat": f'{fake.latitude()}',
                    "lng": f'{fake.longitude()}'
                }
            },
            "phone": fake.phone_number(),
            "website": fake.url(),
            "company": {
                "name": fake.company(),
                "catchPhrase": fake.catch_phrase(),
                "bs": fake.bs()
            }
        }
    return payload
