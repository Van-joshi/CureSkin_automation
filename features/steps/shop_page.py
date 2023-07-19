from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import wait
from selenium.common.exceptions import TimeoutException

SEARCH_RESULTS = (By.ID,'ProductCount')
SHOP_LINK = (By.XPATH,"(//a[@class='elementor-item'][normalize-space()='Shop'])[1]")


@when ('Click on shop')
def click_on_shop(context):
    context.driver.find_element(*SHOP_LINK).click()


@then('All products are displayed')
def verify_results_text(context):
    product_count_text = context.driver.find_element(*SEARCH_RESULTS).text
    #product_count_test = int(product_count_text)
    print(product_count_text)
    expected_result = '19 products'
    assert product_count_text == expected_result, f'Error!,expected{expected_result} but got{product_count_text}'
