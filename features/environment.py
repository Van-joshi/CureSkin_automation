import allure_behave
import behave
from allure_behave.formatter import AllureFormatter
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from app.application import Application
from support.logger import logger
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def browser_init(context):
    '''setup for Chrome'''
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)

    ''' MOBILE EMULATION'''
    mobile_emulation = {"deviceName": "iPhone 8"}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    context.driver = webdriver.Chrome(options=chrome_options)

    '''setup for firefox'''

    # firefox_options = webdriver.FirefoxOptions()
    # firefox_options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    # context.driver = webdriver.Firefox(executable_path='./geckodriver.exe', options=firefox_options)

    '''HEADLESS MODE FOR CHROME'''

    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # context.driver = webdriver.Chrome(chrome_options=options, service=service)

    '''HEADLESS MODE FOR FIREFOX FOR WINDOWS'''

    # firefox_options = webdriver.FirefoxOptions()
    # firefox_options.add_argument('--headless')
    # firefox_options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    # context.driver = webdriver.Firefox(executable_path='./geckodriver.exe', options=firefox_options)
    # #### BROWSERSTACK ####
    # desired_cap = {
    #     'browser': 'Firefox',
    #     'os_version': '10',
    #     'os': 'Windows',
    #     'sessionName': scenario.name
    # }
    # bs_user = 'vandanajoshi_qBgtJw'
    # bs_key = 'h7xzvq7pFSyyxkmFkyeJ'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)
    # context.driver.execute_script(
    #     'browserstack_executor:{"action":"setSessionName", "arguments":{"name": " ' + scenario.name + ' " }}')
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.driver.wait = WebDriverWait(context.driver, 12)
    context.app = Application(context.driver)

    # Allure command:

   #behave - f allure_behave.formatter: AllureFormatter -o features/
   #behave - f allure_behave.formatter: AllureFormatter -o features/tests/search_result.feature
   #behave -f allure_behave.formatter:AllureFormatter -o test_results/ ./features/tests/search_result.feature
    #behave -f allure_behave.formatter:AllureFormatter -o test_results/ ./features/
    # to generate allure report
    # allure serve test_results/




def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)
        # Mark test case as FAILED on BrowserStack:
        #context.driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {'
                                     # '"status":"failed", "reason": "Step failed"}}')


    #
def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()