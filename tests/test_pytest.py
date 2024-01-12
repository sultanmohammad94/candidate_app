import pytest


def test_is_lower():
    s = 'abcd'
    assert s.islower() == 'abcd' #Check if the string is lower

def test_even_number():
    n = 2
    assert n %2 == 0 #Check if the number is even

def test_odd_number():
    n = 3
    assert n %2 != 0 #Check if n is odd number

if __name__ == '__main__':
    pytest.main()