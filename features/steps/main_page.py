from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import wait
from selenium.common.exceptions import TimeoutException


@given('Open CureSkin url')
def open_url(context):
    # context.driver.get("https://cureskin.com/")
    context.app.main_page.open_main_page()



@when('CureSkin url is open')
def main_page_loads(context):
    context.driver.wait.until(EC.url_contains('cureskin.com'))



