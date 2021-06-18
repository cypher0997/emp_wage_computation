from employee_wage_exception import EmpWageException
from employee import Employee


class Company:

    def __init__(self, company_name, company_id, company_type):
        """
        this method sets the values of company's current object
        :param company_name:describes company name
        :param company_id:describes company id
        :param company_type:describes company type
        """
        self.company_name = company_name
        self.company_id = company_id
        self.company_type = company_type

    def add_company_details(self):
        company_emp_details = {
            'company_name': self.company_name,
            'company_id': self.company_id,
            'company_type': self.company_type
        }
        return company_emp_details

    def returns_emp_details(self):
        """
        this methods takes all current objects attributes values and creates a map with the corresponding
        number of employee details
        :return: returns a map of required details
        """
        try:
            emp_details = {}
            neo_company_emp_details = self.add_company_details()
            emp_details_count = 0
            emp_id_count = 0
            number_of_emp = int(input("enter the number of employee u want to store"))
            for i in range(0, number_of_emp):
                work_type_input = int(input("enter '1' if full_time else '2' for part_time "))
                if work_type_input is None or work_type_input > 2:
                    raise EmpWageException()
                emp_name_input = input("enter the employee name")
                emp_id_count += 1
                employee = Employee(emp_name_input, emp_id_count, "IT", int(work_type_input), 1)
                emp_details = employee.returns_employee_details()
                emp_details_count += 1
                neo_company_emp_details['emp_details' + str(emp_details_count)] = emp_details
            return neo_company_emp_details
        except ValueError:
            raise EmpWageException

    def returns_final_list(self):
        """
        creates a final list of all companies with required details of its own and its employees
        :return: returns required final list
        """
        company_list = []
        final_result = self.returns_emp_details()
        company_list.append(final_result)
        return company_list

