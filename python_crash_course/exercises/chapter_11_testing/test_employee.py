from Employee_11_3 import Employee
import pytest



# Test using fixture
@pytest.fixture

def employee_1():
        # This fixture creates an instance of Employee to use in the tests
    return Employee("oscar", "perez", 85000)


def test_current_salary(employee_1):
        # This method tests the __init__ method of the Employee class
    assert employee_1.annual_salary == 85000
    assert employee_1.first_name == "oscar"
    assert employee_1.last_name == "perez"



