from Pages.base_page import Page
from selenium.webdriver.common.by import By


class SearchResults(Page):
    SEARCH_RESULTS = (By.ID, 'ProductCount')
    SEARCH_ICON = (By.CSS_SELECTOR, "div[class='template-search__search'] button[aria-label='Search our site']")
    TEXT_BOX = (By.ID, "Search-In-Template")

    def open_main_page(self):
        self.driver.get('https://shop.cureskin.com/search')

    def enter_search_word(self, text):
        self.driver.find_element(*self.TEXT_BOX).send_keys(text)

    def click_on_search(self):
        self.driver.find_element(*self.SEARCH_ICON).click()

    def Product_count_displayed(self):
        expected_result = '19 results found for “cure”'
        actual_result = self.driver.find_element(*self.SEARCH_RESULTS).text
        assert actual_result == expected_result,f'expected{expected_result} but got{actual_result}'




