from Pages.base_page import Page
from selenium.webdriver.common.by import By


class ShopPage(Page):
    SEARCH_RESULTS = (By.ID, 'ProductCount')


def verify_results_text(self):
    self.verify_results_text(*self.SEARCH_RESULTS)
