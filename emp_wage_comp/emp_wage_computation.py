import random


class Employee:
    def __init__(self, emp_name, emp_id, department):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.department = department

    def check_emp_present_or_absent(self):
        is_present = 1
        random_num = random.randint(0, 1)
        if random_num == is_present:
            print(self.emp_name+" "+"present")
        else:
            print(self.emp_name+" "+"absent")


def main():
    print("welcome to employee wage computation")
    employee = Employee("Andra", 1, "IT")
    employee.check_emp_present_or_absent()


if __name__ == '__main__':
    main()