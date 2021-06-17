import random


class Employee:
    def __init__(self, emp_name, emp_id, department,is_fulltime):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.department = department
        self.work_type = is_fulltime

    def check_emp_present_or_absent(self):
        is_present = 1
        random_num = random.randint(0, 1)
        if random_num == is_present:
            return True
        else:
            return False

    def calculate_daily_wage(self):
        status = self.check_emp_present_or_absent()
        if status:
            emp_hrs = 0
            emp_wage = 0
            rate_per_hrs = 20
            if self.work_type == 1:
                emp_hrs = 8
            else:
                emp_hrs = 0
            emp_wage = emp_hrs * rate_per_hrs
            print("daily Wage"+" "+str(emp_wage))
        else:
            print("employee is absent")


def main():
    print("welcome to employee wage computation")
    employee = Employee("Andra", 1, "IT",1)
    employee.calculate_daily_wage()


if __name__ == '__main__':
    main()