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


@given('Launch Browser')
def launch_browser(context):
    context.driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)
    mylogger.info("**** Driver Initialized ****")
    time.sleep(10)
    context.driver.maximize_window()
    context.driver.get(TestData.BASEURL)
    time.sleep(10)
    mylogger.info("** URL Launched **")

@when('Login Application')
def login_to_application(context):
    lpage = LoginPage(context.driver)
    lpage.loginToApplication()
    context.driver.save_screenshot(".//Screenshots//trello.png")


@then('Create A New Board')
def create_new_board(context):
    hpage = HomePage(context.driver)
    time.sleep(20)
    hpage.goToBoards()


@then('Add A New List')
def create_new_list(context):
    hpage = HomePage(context.driver)
    time.sleep(5)
    hpage.createList()
    time.sleep(5)

@then('Add new Card')
def create_new_card(context):
    hpage = HomePage(context.driver)
    hpage.createCard()
    time.sleep(5)