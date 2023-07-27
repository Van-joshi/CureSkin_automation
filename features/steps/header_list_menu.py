from behave import given, when, then
from selenium.webdriver.common.by import By


@then('User can click through all elements and verify correct page is open')
def click_on_header_links(context):
    context.app.header_list.click_on_header_links()



