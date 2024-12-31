from employee import Employee

def test_give_default_raise():
    """Test giving employees default raise."""
    employee = Employee('oliver', 'arenas', 20000)
    employee.give_raise()
    assert employee.annual_salary == 25000

def test_give_custom_raise():
    """Test giving employees custom raise."""
    employee = Employee('oliver', 'arenas', 20000)
    employee.give_raise(2000)
    assert employee.annual_salary == 22000