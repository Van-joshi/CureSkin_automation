from selenium.webdriver.common.by import By
from behave import given, when, then


@when('locate home tab')
def home_link(context):
    context.app.header.home_link()


@when('locate shop tab')
def shop_link(context):
    context.app.header.shop_link()


@when('locate CureSkin app tab')
def cureskin_app_link(context):
    context.app.header.cureskin_app_link()


@when('locate About Us tab')
def about_us_link(context):
    context.app.header.about_us_link()


@when('locate our expertise tab')
def expertise_link(context):
    context.app.header.expertise_link()


@when('locate our Testimonials tab')
def testimonials_link(context):
    context.app.header.testimonials_link()


@when('locate Skin&Hair tab')
def skinAndHair_link(context):
    context.app.header.skinAndHair_link()


@when('locate FAQ')
def FAQ_link(context):
    context.app.header.FAQ_link()


@when('locate Contact us tab')
def Contact_us_link(context):
    context.app.header.Contact_us_link()





