import sys

def employee_salary(basic_salary):
    hra = basic_salary * 0.20
    da = basic_salary * 0.10

    gross_salary = basic_salary + hra + da

    print("Employee Salary Details")
    print("----------------------")
    print("Basic Salary:", basic_salary)
    print("HRA:", hra)
    print("DA:", da)
    print("Gross Salary:", gross_salary)

    return gross_salary

basic_salary = int(sys.argv[1])
employee_salary(basic_salary)