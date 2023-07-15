from Pages.BasePage import Page
from selenium.webdriver.support import expected_conditions as EC


class MainPage(Page):
    def open_url(self):
        self.driver.get('https://cureskin.com/')

    def main_page_loads(self,*locator):
        return self.wait.until(EC.url_contains('cureskin.com'))