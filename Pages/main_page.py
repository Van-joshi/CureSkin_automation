from Pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC


class MainPage(Page):
    def open_main_page(self):
        self.open_url("https://cureskin.com/")



    def main_page_loads(self,*locator):
        return self.wait.until(EC.url_contains('cureskin.com'))

