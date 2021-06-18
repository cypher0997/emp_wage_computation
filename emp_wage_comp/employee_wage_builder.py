

class EmployeeWageBuilder:

    def calculate_monthly_wage(self, emp_hrs):
        emp_wage = 0
        if emp_hrs == 0:
            i = 0
            return i
        else:
            rate_per_hrs = 20
            emp_wage += emp_hrs * rate_per_hrs
            return emp_wage
