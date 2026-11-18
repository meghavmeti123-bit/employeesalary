from salary import employee_salary

def test_gross_salary():
    result = employee_salary(50000)
    assert result == 65000

def test_hra_and_da():
    result = calculate_salary(10000)
    assert result == 13000

def test_zero_salary():
    result = calculate_salary(0)
    assert result == 0