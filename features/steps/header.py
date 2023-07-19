from selenium.webdriver.common.by import By
from behave import given, when, then


SHOP_LINK = (By.XPATH,"(//a[@class='elementor-item'][normalize-space()='Shop'])[1]")
SEARCH_RESULTS = (By.XPATH, "(//p[@id='ProductCount'])[1]")
HOME_LINK = (By.CSS_SELECTOR, "ul[id='menu-1-5bfd1d9'] a[class='elementor-item elementor-item-active']")
CURESKIN_APP = (By.XPATH,"(//a[@class='elementor-item'][normalize-space()='Cureskin App'])[1]")
ABOUT_US = (By.XPATH, "(//a[@class='elementor-item'][normalize-space()='About Us'])[1]")
OUR_EXPERTISE  = (By.XPATH,"(//a[@class='elementor-item'][normalize-space()='Our Expertise'])[1]")
TESTIMONIALS =(By.XPATH, "(//a[@class='elementor-item'][normalize-space()='Testimonials'])[1]")
SKIN_HAIR =(By.XPATH,"(//a[@class='elementor-item'][normalize-space()='Skin & Hair 101'])[1]")
FAQ = (By.XPATH,"(//a[@class='elementor-item'][normalize-space()='FAQs'])[1]")
CONTACT_US = (By.XPATH,"(//a[@class='elementor-item'][normalize-space()='Contact Us'])[1]")


@when('locate home tab')
def home_link(context):
    context.driver.find_element(*HOME_LINK)
    #context.app.header.home_link()


@when('locate shop tab')
def shop_link(context):
    context.driver.find_element(*SHOP_LINK)
    #context.app.header.shop_link()


@when('locate CureSkin app tab')
def cureskin_app_link(context):
    context.driver.find_element(*CURESKIN_APP)
    #context.app.header.cureskin_app_link()


@when('locate About Us tab')
def about_us_link(context):
    context.driver.find_element(*ABOUT_US)
    #context.app.header.about_us_link()


@when('locate our expertise tab')
def expertise_link(context):
    context.driver.find_element(*OUR_EXPERTISE)
    #context.app.header.expertise_link()


@when('locate our Testimonials tab')
def testimonials_link(context):
    context.driver.find_element(*TESTIMONIALS)
    #context.app.header.testimonials_link()


@when('locate Skin&Hair tab')
def skinAndHair_link(context):
    context.driver.find_element(*SKIN_HAIR)
    #context.app.header.skinAndHair_link()


@when('locate FAQ')
def FAQ_link(context):
    context.driver.find_element(*FAQ)
    #context.app.header.FAQ_link()


@when('locate Contact us tab')
def Contact_us_link(context):
    context.driver.find_element(*CONTACT_US)
    #context.app.header.Contact_us_link()





