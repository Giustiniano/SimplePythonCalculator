import pytest

from simple_python_calulator.simple_python_calculator import simple_python_calculator

@pytest.mark.parametrize("expression, exp_result", [("1+1", 2), ("1 + 1", 2), ("10+1", 11), ("10+10", 20), ("-1--1", 0)])
def test_simple_python_calculator(expression, exp_result):
    assert simple_python_calculator(expression) == exp_result