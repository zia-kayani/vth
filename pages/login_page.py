from playwright.sync_api import Page, expect


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.login_link = page.get_by_role("link", name="Log in")
        self.username_input = page.get_by_role(
            "textbox", name="Enter username/email/mob"
        )
        self.login_with_password_link = page.get_by_role(
            "link", name="Login with password"
        )
        self.password_input = page.get_by_role("textbox", name="Password")
        self.next_button = page.get_by_role("button", name="Next")

    def open(self):
        self.page.goto("https://lms.pr1056.streamtraining.com/")
        expect(self.login_link).to_be_visible()

    def login_with_password(self, username: str, password: str):
        self.login_link.click()

        self.username_input.fill(username)
        self.login_with_password_link.click()

        self.password_input.fill(password)
        self.next_button.click()
