from Pages.BasePage import Page
from selenium.webdriver.common.by import By

SHOP_LINK = (By.XPATH,"(//a[@class='elementor-item'][normalize-space()='Shop'])[1]")
SEARCH_RESULTS = (By.XPATH, "(//p[@id='ProductCount'])[1]")


class Header(Page):
    SHOP_LINK = (By.XPATH, "(//a[@class='elementor-item'][normalize-space()='Shop'])[1]")
    SEARCH_RESULTS = (By.XPATH, "(//p[@id='ProductCount'])[1]")


def click_on_shop(self):
    self.click_on_shop(*self.SHOP_LINK)


def verify_results_text(self):
    self.verify_result_text(self.Search_Results)



