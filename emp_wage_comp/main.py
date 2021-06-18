from employee_wage_exception import EmpWageException
from company import Company


def main():
    """
    its a main method from where the execution starts
    :return: it prints the list of companies in which each company has its own employee details
    """
    print("welcome to employee wage computation")
    try:
        cl = []
        company_id_count = 0
        number_of_companies = int(input("enter the number of companies u want to store"))
        if number_of_companies is None:
            raise EmpWageException()
        for i in range(0, number_of_companies):
            company_name_input = input("enter the company name")
            if company_name_input is company_name_input.isnumeric() or company_name_input is None:
                raise EmpWageException()
            company_id_count += 1
            company_ob = Company(company_name_input, company_id_count, "IT")
            cl.append(company_ob.returns_final_list())
        for i in cl:
            print(i)
    except ValueError:
        raise EmpWageException


if __name__ == '__main__':
    main()
