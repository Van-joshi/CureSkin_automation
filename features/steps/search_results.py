from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


SEARCH_RESULTS = (By.ID,'ProductCount')
CLICK_SEARCH = (By.CSS_SELECTOR, "div[class='template-search__search'] button[aria-label='Search our site']")
TEXT_BOX = (By.ID,"Search-In-Template")


@given('Cureskin Search page is open')
def open_main_page(context):
    #context.driver.get('https://shop.cureskin.com/search')
    context.app.search_results.open_shop_page()


@when('{search_word} is entered in textbox')
def enter_search_word(context, search_word):
    #context.driver.find_element(*TEXT_BOX).send_keys('cure')
    context.app.search_results.enter_search_word(search_word)


@when('search is clicked')
def click_on_search(context):
    #context.driver.find_element(*CLICK_SEARCH).click()
    context.app.search_results.click_on_search()


@then('User gets {search_results}')
def Product_count_displayed(context, search_results):
    context.app.search_results.Product_count_displayed()
    #expected_result = f'{search_results} results found for “cure”'
    #actual_result = context.driver.find_element(*SEARCH_RESULTS).text
    #assert actual_result == expected_result,f'expected{expected_result} but got{actual_result}'

