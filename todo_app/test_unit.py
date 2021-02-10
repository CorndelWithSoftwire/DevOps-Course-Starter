import pytest
from todo_app.todo import Newviewmodel    



def test_from_trello_card():
	# Given 
	test_array=[1,2,3,4]
	test_Newviewmodel=Newviewmodel(test_array)
	# When
	result=test_Newviewmodel.items
	# Then
	assert result == test_array





