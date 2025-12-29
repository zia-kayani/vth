from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.user_profile_update_page import UserProfileUpdatePage
from pages.user_profile_logout_page import UserProfileLogoutPage
from config.env_credentials import LOGINCREDENTIALS

def test_example(page: Page) -> None:
    login_page = LoginPage(page)

    user_profile_page = UserProfileUpdatePage(page)
    user_logout_page = UserProfileLogoutPage(page)

    login_page.open()
    login_page.login_with_password(username=LOGINCREDENTIALS['USERNAME'], password=LOGINCREDENTIALS['PASSWORD'])

    page.wait_for_timeout(5000)
    
    user_profile_page.open_user_profile()

    user_logout_page.logout_user()
    
    