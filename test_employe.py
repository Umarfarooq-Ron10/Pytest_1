from employee import employee_details

def test_employee_details():
    expected_output = (
        "Employee Name: Alice\n"
        "Employee ID: E101\n"
        "Department: IT\n"
        "Salary: 55000"
    )
    assert employee_details("Alice", "E101", "IT", 55000) == expected_output