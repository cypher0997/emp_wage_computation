import random
from employee_wage_builder import EmployeeWageBuilder


class Employee:
    def __init__(self, emp_name, emp_id, department, form, check):
        """
        sets the attributes for current employee object
        :param emp_name: describes employee name
        :param emp_id: describes employee id
        :param department: describes employee department
        :param form: describes type of employee
        :param check: checks if present or absent
        """
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.department = department
        self.work_type = form
        self.is_present = check

    def check_emp_present_or_absent(self):
        """
        checks if employee present or absent
        :return: gives true if present else gives false
        """
        random_num = random.randint(0, 1)
        if random_num == self.is_present:
            return 1
        else:
            return 2

    def returns_work_hrs(self):
        """
        calculates the monthly wage for employee
        :return: returns the total amount employee earned at months end and returns a map of corresponding details
        """
        count = 0
        emp_hrs = 0
        status = self.check_emp_present_or_absent()
        if status:
            wage_hrs = {
                '1': 8,
                '2': 4,
            }
            emp_hrs = wage_hrs.get(str(status))
            return emp_hrs
        else:
            i = 0
            return i

    def returns_employee_details(self):
        """
        this methods creates dictionary that holds employee details
        :return: it returns the employee detail dictionary
        """
        count = 0
        emp_wage = 0
        emp_details = {
            'name': self.emp_name,
            'emp_id': self.emp_id,
            'department': self.department,
            }
        emp_monthly_wage = EmployeeWageBuilder()
        while True:
            count += 1
            if count == 20:
                break
            emp_wage += emp_monthly_wage.calculate_monthly_wage(self.returns_work_hrs())
        emp_details['wage'] = emp_wage
        return emp_details
