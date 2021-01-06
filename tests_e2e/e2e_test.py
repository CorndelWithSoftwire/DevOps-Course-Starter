
def test_task_journey(driver, test_app): 
  driver.get('http://localhost:5000/')
  assert driver.title == 'To-Do App'