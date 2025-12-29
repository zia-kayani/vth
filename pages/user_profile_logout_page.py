from pages.user_profile_update_page import UserProfileUpdatePage
from playwright.sync_api import Page, expect

class UserProfileLogoutPage:
    def __init__(self, page: Page):
        self.page =  Page
        self.logout_link = page.get_by_role("link", name=" Logout")
    
    def logout_user(self):
        expect(self.logout_link).to_be_visible()
        self.logout_link.click()
        




        