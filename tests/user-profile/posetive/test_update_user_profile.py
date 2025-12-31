from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.user_profile_update_page import UserProfileUpdatePage
from config.env_credentials import LOGINCREDENTIALS
import pytest

@pytest.mark.video
def test_example(page: Page) -> None:
    login_page = LoginPage(page)
    user_profile_page = UserProfileUpdatePage(page)

    login_page.open()
    login_page.login_with_password(username=LOGINCREDENTIALS["USERNAME"], password=LOGINCREDENTIALS["PASSWORD"])

    page.wait_for_timeout(5000)

    user_profile_page.open_user_profile()
    user_profile_page.navigate_to_profile_settings()
    user_profile_page.update_password(new_password=LOGINCREDENTIALS["NEW_PASSWORD"])
    