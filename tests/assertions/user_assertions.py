from assertpy import assert_that


def assert_status_code(actual_code, expected_code, description=None):
    assert_that(actual_code, description=description).is_equal_to(expected_code)


def assert_user_have_in_users_with_email(response, email, description=None):
    assert_that(response.as_dict, description=description).extracting('email').is_not_empty().contains(email)


def assert_user_is_present(is_new_user_created):
    assert_that(is_new_user_created).is_not_empty()

