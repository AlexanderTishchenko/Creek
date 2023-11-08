from selenium import webdriver

class DriverFactory:
    @staticmethod
    def get_driver():
        # You can add logic here to select different drivers based on input/environment
        return webdriver.Chrome('/path/to/chromedriver')