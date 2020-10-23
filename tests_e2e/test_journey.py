from time import sleep
from selenium.webdriver.common.by import By

def test_task_journey(driver, test_app):
    driver.get('http://localhost:5000/')
    add_todo_item(driver)
    assert driver.title == 'To-Do App'

def add_todo_item(driver):
    titleInputXPath = "//*[@id=\"title\"]"
    titleInput = driver.find_elements(By.XPATH, titleInputXPath)
    text = "Test 1 To Do Item"
    titleInput[0].send_keys(text)
    sleep(5)

    titleSubmitXPath = "/html/body/div/div[2]/div[1]/form/input[2]"
    titleSubmit = driver.find_elements(By.XPATH, titleSubmitXPath)
    titleSubmit[0].click()
    sleep(5)

    newToDoItemXPath = '/html/body/div/div[2]/div[2]/div/ul[1]/div/li/ul/div/div[1]'
    newToDoItem = driver.find_elements(By.XPATH, newToDoItemXPath)
 
    assert newToDoItem[0].text = text
    