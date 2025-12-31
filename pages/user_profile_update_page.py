from playwright.sync_api import Page, expect

class UserProfileUpdatePage:
    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.user_profile_link = page.locator(".dropdown-button.head-info")
        self.profile_settings_link = page.get_by_role("link", name=" Profile Settings")
        self.profile_tab = page.get_by_role("link", name="Profile", exact=True)
        self.password_input = page.get_by_role("textbox", name="Password", exact=True)
        self.confirm_password_input = page.get_by_role("textbox", name="Confirm Password")
        self.save_button = page.get_by_role("button", name="Save")

    def open_user_profile(self):
        expect(self.user_profile_link).to_be_visible()
        self.user_profile_link.click()

    def navigate_to_profile_settings(self):
        expect(self.profile_settings_link).to_be_visible()
        self.profile_settings_link.click()
        expect(self.profile_tab).to_be_visible()
        self.profile_tab.click()

    def update_password(self, new_password: str):
        expect(self.password_input).to_be_visible()
        self.password_input.fill(new_password)
        expect(self.confirm_password_input).to_be_visible()
        self.confirm_password_input.fill(new_password)
        expect(self.save_button).to_be_visible()
        self.save_button.click()
        


