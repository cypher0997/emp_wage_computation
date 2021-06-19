

class EmployeeWageBuilder:
    def __int__(self):
        self.none = None

    def calculate_monthly_wage(self, emp_hrs):
        ignore = self.none
        """
        this methods performs the basic calculations for employees monthly wage
        :param emp_hrs: this describes employee working hours for a day
        :return: this method returns the total monthly wage that an employee earns
        """
        emp_wage = 0
        if emp_hrs == 0:
            i = 0
            return i
        else:
            rate_per_hrs = 20
            emp_wage += emp_hrs * rate_per_hrs
            return emp_wage
