from Pages.MainPage import MainPage
from Pages.Header import Header


class Application:
    def __init__(self, driver):
        self.driver = driver
        self.MainPage = MainPage(self.driver)
        self.Header = Header(self.driver)





