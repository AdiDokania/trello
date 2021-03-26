from selenium.webdriver.common.by import By
from configurations.config import TestData
from Pages.BasePage import BasePage


class HomePage(BasePage):
    Board = (By.XPATH, "//span[text() = 'Create new board']")
    BoardTitle = (By.XPATH, "//input[@placeholder ='Add board title']")
    BoardBtn = (By.XPATH, "//button[text() ='Create board']")
    ListName = (By.NAME, "name")
    AddListBtn = (By.XPATH, "//input[@value='Add list']")
    AddCardBtn = (By.XPATH, "//span[text()='Add a card']")
    CardName = (By.XPATH, "//div[@class ='card-composer']/div/div/textarea")
    NewCardBtn = (By.XPATH, "//input[@value ='Add card']")

    def __init__(self, driver):
        super().__init__(driver)


    def goToBoards(self):
        self.do_click(self.Board)
        self.do_send_keys(self.BoardTitle, TestData.BoardTitle)
        self.do_click(self.BoardBtn)

    def createList(self):
        self.do_send_keys(self.ListName, TestData.ListName)
        self.do_click(self.AddListBtn)

    def createCard(self):
        self.do_click(self.AddCardBtn)
        self.do_send_keys(self.CardName, TestData.CardName)
        self.do_click(self.NewCardBtn)