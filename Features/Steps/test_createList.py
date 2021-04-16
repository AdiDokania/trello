import time
from behave import *
from selenium import webdriver

from Pages.HomePage import HomePage
from Utilities.CustomLogger import LogGen
from configurations.config import TestData
from Pages.LoginPage import LoginPage

global lpage
global hpage
mylogger = LogGen.logger()


@given('Launch the Browser')
def launch_browser(context):
    context.driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)
    mylogger.info("**** Driver Initialized ****")
    time.sleep(10)
    context.driver.maximize_window()
    context.driver.get(TestData.BASEURL)
    time.sleep(10)
    mylogger.info("** URL Launched **")

@when('Login to Application')
def login_to_application(context):
    lpage = LoginPage(context.driver)
    lpage.loginToApplication()


@when('Create New Board')
def create_new_board(context):
    hpage = HomePage(context.driver)
    time.sleep(10)
    hpage.goToBoards()


@when('Add New List')
def create_new_list(context):
    hpage = HomePage(context.driver)
    time.sleep(2)
    hpage.createList()
    time.sleep(2)

@then('Validate Title')
def assert_title(context):
    hpage = HomePage(context.driver)
    HTitle = hpage.getTitle()
    if HTitle == TestData.BoardTitle:
        assert True
        mylogger.info(" Title Verified")

    else:
        mylogger.info(" Title Not Verified ")
        assert False