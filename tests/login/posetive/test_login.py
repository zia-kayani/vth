import pytest
from pages.login_page import LoginPage
from config.env_credentials import LOGINCREDENTIALS

@pytest.fixture
def user_credentials():
    return {
        "username": LOGINCREDENTIALS['USERNAME'],
        "password": LOGINCREDENTIALS['PASSWORD'],
    }
def test_user_can_login_with_valid_credentials(page, user_credentials):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login_with_password(
        username=user_credentials["username"],
        password=user_credentials["password"]
    )
