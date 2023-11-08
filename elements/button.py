class Button:
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator

    def click(self):
        self.driver.find_element_by_flutter(*self.locator).click()