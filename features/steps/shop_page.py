from selenium.webdriver.common.by import By
from behave import given, when, then


@when ('Click on shop')
def click_on_shop(context):
    context.app.shop.click_on_shop()


@then('{search_results} products are displayed')
def verify_results_text(context,search_results ):
    context.app.shop.verify_results_text()

