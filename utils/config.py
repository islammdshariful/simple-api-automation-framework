from pprint import pprint
BASE_URI = "http://localhost:3000"
BASE_AUTH_URI = "http://localhost:8000"


def pretty_print(msg):
    print()
    pprint(msg, indent=2, sort_dicts=False)
