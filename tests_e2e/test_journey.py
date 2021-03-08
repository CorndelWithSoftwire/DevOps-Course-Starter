from time import sleep
from selenium.webdriver.common.by import By
import pytest 

def test_check_title(driver, test_app):
    driver.get('http://localhost:5000/')
    assert driver.title == 'To-Do App'

def test_add_todo_item(driver, test_app):
    driver.get('http://localhost:5000/')
    text = "Test 1 To Do Item"

    populateTitleInputElement(driver, text)
    submitTitleButtonElement(driver)

    newToDoItemXPath = '/html/body/div/div[2]/div[2]/div/ul[1]/div/li/ul/div/div[1]'
    newToDoItem = driver.find_elements(By.XPATH, newToDoItemXPath)
 
    assert newToDoItem[0].text == text

def test_change_todo_item_doing(driver, test_app):
    driver.get('http://localhost:5000/')
    text = "Test 2 To Do Item"
    populateTitleInputElement(driver, text)
    submitTitleButtonElement(driver)
    submitDoingButtonElement(driver)

    doingToDoItemXPath = '/html/body/div/div[2]/div[2]/div/ul[2]/div[1]/li/ul/div/div[2]'
    doingToDoItem = driver.find_elements(By.XPATH, doingToDoItemXPath)

    assert doingToDoItem[0].text == 'Doing'

def test_change_todo_item_done(driver, test_app):
    driver.get('http://localhost:5000/')
    text = "Test 3 To Do Item"
    populateTitleInputElement(driver, text)
    submitTitleButtonElement(driver)
    submitDoingButtonElement(driver)
    submitDoneButtonElement(driver)
    completedxpath = "/html/body/div/div[2]/div[2]/div/ul[3]/details[1]/summary"
    completedItems = driver.find_elements(By.XPATH, completedxpath)
    completedItems[0].click()
    doingToDoItemXPath = '/html/body/div/div[2]/div[2]/div/ul[3]/details[1]/div[1]/li/ul/div/div[2]'
    doingToDoItem = driver.find_elements(By.XPATH, doingToDoItemXPath)

    assert doingToDoItem[0].text == 'Done'

def populateTitleInputElement(driver, text):
    titleInputXPath = "//*[@id=\"title\"]"
    titleInput = driver.find_elements(By.XPATH, titleInputXPath)
    titleInput[0].send_keys(text)
    sleep(5)

def submitTitleButtonElement(driver):
    titleSubmitXPath = "/html/body/div/div[2]/div[1]/form/input[2]"
    titleSubmit = driver.find_elements(By.XPATH, titleSubmitXPath)
    titleSubmit[0].click()
    sleep(5)

def submitDoingButtonElement(driver):
    doingSubmitXPath = "/html/body/div/div[2]/div[2]/div/ul[1]/div[1]/li/ul/div/div[3]/div/form/input"
    doingSubmit = driver.find_elements(By.XPATH, doingSubmitXPath)
    doingSubmit[0].click()
    sleep(5)

def submitDoneButtonElement(driver): 
    doneSubmitXPath = "/html/body/div/div[2]/div[2]/div/ul[2]/div/li/ul/div/div[3]/div/form/input"
    doneSubmit = driver.find_elements(By.XPATH, doneSubmitXPath)
    doneSubmit[0].click()
    sleep(5)