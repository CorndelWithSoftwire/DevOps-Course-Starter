import  pytest
from selenium import webdriver

from todo_app.SeleniumTest.config import TestData

@pytest.fixture(params=["chrome", "firefox", "edge"], scope ='class')
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(executable_path=TestData.Chrome_Executable_Path)
    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=TestData.Firefox_Executable_Path)
    if request.param == "Edge":
        web_driver = webdriver.Edge(executable_path=TestData.Edge_Executable_Path)
    request.cls.driver = webdriver
    yield
    web_driver.close()