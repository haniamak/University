## pytest z1.py --random-order
## https://pypi.org/project/pytest-random-order/
import pytest

# def func(x):
#     return x + 1

# def test_answer1():
#     assert func(3) == 5

# def test_answer2():
#     assert func(3) == 4

# def test_answer3():
#     assert func(3) == 3


## pytest z1.py --reruns 3
## https://pytest-rerunfailures.readthedocs.io/stable/quickstart.html#basic-usage

import random

def toss():
    x = random.randint(0, 1)
    return x

#@pytest.mark.repeat(3)
def test_toss():
    assert toss() == 0


## pip install pytest-repeat
## https://pypi.org/project/pytest-repeat/
## pytest --count=10 z1.py if we don't use decorator

