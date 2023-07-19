from Pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Header(Page):
    SHOP_LINK = (By.XPATH, "(//a[@class='elementor-item'][normalize-space()='Shop'])[1]")
    SEARCH_RESULTS = (By.XPATH, "(//p[@id='ProductCount'])[1]")
    HOME_LINK = (By.CSS_SELECTOR, "ul[id='menu-1-5bfd1d9'] a[class='elementor-item elementor-item-active']")
    CURESKIN_APP = (By.XPATH, "(//a[@class='elementor-item'][normalize-space()='Cureskin App'])[1]")
    ABOUT_US = (By.XPATH, "(//a[@class='elementor-item'][normalize-space()='About Us'])[1]")
    OUR_EXPERTISE = (By.XPATH, "(//a[@class='elementor-item'][normalize-space()='Our Expertise'])[1]")
    TESTIMONIALS = (By.XPATH, "(//a[@class='elementor-item'][normalize-space()='Testimonials'])[1]")
    SKIN_HAIR = (By.XPATH, "(//a[@class='elementor-item'][normalize-space()='Skin & Hair 101'])[1]")
    FAQ = (By.XPATH, "(//a[@class='elementor-item'][normalize-space()='FAQs'])[1]")
    CONTACT_US = (By.XPATH, "(//a[@class='elementor-item'][normalize-space()='Contact Us'])[1]")


    def shop_link(self):
        self.driver.find_element(*self.SHOP_LINK)


    def home_link(self):
        self.driver.find_element(*self.HOME_LINK)


    def cureskin_app_link(self):
        self.driver.find_element(*self.CURESKIN_APP)


    def about_us_link(self):
        self.driver.find_element(*self.ABOUT_US)


    def expertise_link(self):
        self.driver.find_element(*self.OUR_EXPERTISE)


    def testimonials_link(self):
        self.click_on_testimonials(*self.TESTIMONIALS)


    def skinAndHair_link(self):
        self.driver.find_element(*self.SKIN_HAIR)


    def FAQ_link(self):
        self.driver.find_element(*self.FAQ)


    def Contact_us_link(self):
        self.driver.find_element(*self.CONTACT_US)


    def verify_results_text(self):
        self.verify_result_text(self.Search_Results)


    def abtUs_page_loads(self,*locator):
        return self.wait.until(EC.url_contains('https://cureskin.com/about-cureskin/'))

