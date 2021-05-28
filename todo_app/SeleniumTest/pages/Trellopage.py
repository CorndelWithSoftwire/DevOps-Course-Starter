from todo_app.SeleniumTest.config import TestData
from selenium.webdriver.common.by import By
from todo_app.SeleniumTest.pages.Basepage import BasePage

class TrelloHomePage(BasePage):
    TrelloBoard = (By.CLASS_NAME, "RtLvvlOZklu-NO _3ZNHfNcj3Tqnuu")

    """Constructor"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.Base_url)

    def get_trello_Page_title(self, title):
        return self.get_title(title)

    def is_trello_board_exists(self):
        return self.is_visible(self.TrelloBoard)

