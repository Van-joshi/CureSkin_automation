from Pages.base_page import Page
from selenium.webdriver.common.by import By


class ShopPage(Page):
    SEARCH_RESULTS = (By.ID, 'ProductCount')
    SHOP_LINK = (By.XPATH, "(//a[@class='elementor-item'][normalize-space()='Shop'])[1]")

    def click_on_shop(self):
        self.driver.find_element(*self.SHOP_LINK).click()

    def verify_results_text(self):
        product_count_text = self.driver.find_element(*self.SEARCH_RESULTS).text
        print(product_count_text)
        expected_result = '19 products'
        assert product_count_text == expected_result, f'Error!,expected{expected_result} but got{product_count_text}'