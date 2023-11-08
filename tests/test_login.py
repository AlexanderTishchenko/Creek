import unittest
from pages.login_page import LoginPage
from utils.driver_factory import DriverFactory


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = DriverFactory.get_driver()
        self.login_page = LoginPage(self.driver)

    def test_login_success(self):
        self.login_page.open()
        self.login_page.enter_username('user')
        self.login_page.enter_password('pass')
        self.login_page.click_login()

        # Add assertions here

    def tearDown(self):
        self.driver.quit()