from Pages.main_page import MainPage
from Pages.header import Header
from Pages.search_results import SearchResults
from Pages.shop import ShopPage

class Application:
    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.header = Header(self.driver)
        self.shop = ShopPage(self.driver)
        self.search_results = SearchResults(self.driver)






