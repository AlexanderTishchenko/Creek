class TextField:
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator

    def enter_text(self, text):
        self.driver.find_element_by_flutter(*self.locator).clear()
        self.driver.find_element_by_flutter(*self.locator).send_keys(text)