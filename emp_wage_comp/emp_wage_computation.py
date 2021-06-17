import random


class Employee:
    def __init__(self, emp_name, emp_id, department, form, check):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.department = department
        self.work_type = form
        self.is_present = check

    def check_emp_present_or_absent(self):
        random_num = random.randint(0, 1)
        if random_num == self.is_present:
            return True
        else:
            return False

    def calculate_monthly_wage(self):
        emp_details ={}
        emp_wage = 0
        count = 0
        while True:
            count += 1
            if count == 20:
                break
            status = self.check_emp_present_or_absent()
            if status:
                emp_hrs = 0
                rate_per_hrs = 20
                if self.work_type == 1:
                    emp_hrs = 8
                elif self.work_type == 2:
                    emp_hrs = 4
                else:
                    emp_hrs = 0
                emp_wage += emp_hrs * rate_per_hrs
            else:
                print("employee is absent at day:"+str(count))
        emp_details['name'] = self.emp_name
        emp_details['emp_id'] = self.emp_id
        emp_details['department'] = self.department
        emp_details['wage'] = emp_wage
        return emp_details


class Company:
    def __init__(self, company_name, company_id, company_type):
        self.company_name = company_name
        self.company_id = company_id
        self.company_type = company_type

    def returns_emp_details(self):
        emp_details_count = 0
        emp_id_count = 0
        company_emp_details = {}
        number_of_emp = int(input("enter the number of employee u want to store"))
        company_emp_details['company_name'] = self.company_name
        company_emp_details['company_id'] = self.company_id
        company_emp_details['company_type'] = self.company_type
        for i in range(0, number_of_emp):
            work_type_input = input("enter '1' if full_time else '2' for part_time ")
            emp_name_input = input("enter the employee name")
            emp_id_count += 1
            employee = Employee(emp_name_input, emp_id_count, "IT", int(work_type_input), 1)
            emp_details = employee.calculate_monthly_wage()
            emp_details_count += 1
            company_emp_details['emp_details'+str(emp_details_count)] = emp_details
        return company_emp_details


def main():
    company_list = []
    company_id_count = 0
    final_result = {}
    print("welcome to employee wage computation")
    number_of_companies = int(input("enter the number of companies u want to store"))
    for i in range(0,number_of_companies):
        company_name_input = input("enter the company name")
        company_id_count += 1
        company_ob = Company(company_name_input, company_id_count, "IT")
        final_result = company_ob.returns_emp_details()
        company_list.append(final_result)
    for i in company_list:
        print(i)


if __name__ == '__main__':
    main()