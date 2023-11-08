from elements.text_field import TextField
from elements.button import Button
from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = 'http://example.com/login'

    def __init__(self, driver):
        self.username_field = TextField(driver, ('ID', 'username'))
        self.password_field = TextField(driver, ('ID', 'password'))
        self.login_button = Button(driver, ('ID', 'login'))

    def open(self):
        super().open(self.URL)

    def enter_username(self, username):
        self.username_field.enter_text(username)

    def enter_password(self, password):
        self.password_field.enter_text(password)

    def click_login(self):
        self.login_button.click()