from salary import employee_salary

def test_gross_salary():
    result = employee_salary(50000)
    assert result == 65000

def test_hra_and_da():
    result = employee_salary(10000)
    assert result == 13000

def test_zero_salary():
    result = employee_salary(0)
    assert result == 0