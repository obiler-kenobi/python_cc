import pytest
from employee import Employee
 
@pytest.fixture
def employee():
    """Employee details that will be available to all test functions."""
    employee = Employee('oliver john', 'arenas', 10000)
    return employee

def test_give_default_raise(employee):
    """Test giving employees default raise."""
    employee.give_raise()
    assert employee.annual_salary == 15000

def test_give_custom_raise(employee):
    """Test giving employees custom raise."""
    employee.give_raise(2000)
    assert employee.annual_salary == 12000