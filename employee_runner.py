import employee

def main():
    employee1 = employee.Employee("Susan Meyers", "47899", "Accounting", "Vice President")
    employee2 = employee.Employee("Mark Jones", "39119", "IT", "Programmer")
    employee3 = employee.Employee("Joy Rogers", "81774", "Manufacturing", "Engineer")

    print(employee1.get_name(), employee1.get_ID_number(), employee1.get_department(), employee1.get_job_title() )
    print(employee2.get_name(), employee2.get_ID_number(), employee2.get_department(), employee2.get_job_title() )
    print(employee3.get_name(), employee3.get_ID_number(), employee3.get_department(), employee3.get_job_title() )


if __name__ == "__main__":
    main()
