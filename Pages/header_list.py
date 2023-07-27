from Pages.base_page import Page
from selenium.webdriver.common.by import By


class HeaderList(Page):
    TOP_LINKS = (By.XPATH, '(//nav[@class="header__inline-menu center cure_header"])[1]')

    def click_on_header_links(self):
        top_links = self.driver.find_elements(*self.TOP_LINKS)
        for i in range(len(top_links)):
            link_to_click = self.driver.find_elements(*self.TOP_LINKS)[i]
            link_text = link_to_click.text
            print(link_text)







