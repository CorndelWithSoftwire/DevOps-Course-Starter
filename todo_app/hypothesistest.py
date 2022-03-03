import pytest 
from hypothesis import given 
from hypothesis.strategies import integers 

 
@pytest.mark.parametrize('number', [-10, 0, 
1, 5, 1000000]) 
def test_division(number): 
 assert number / 1 == number 
 
@given(number=integers()) 
def test_division_with_hypothesis(number): 
 assert number / 1 == number