"""Python Encapsulation

Create class Employee

"""


class Employee:
    """
    Employee information
    """

    def __init__(self, job_title:str) -> None:
        """ Constructor

        Args:
            job_title (str)
        """
        self.__employee_id = None
        self.full_name = None
        self.salary = None
        self.job_title = job_title
    
    def set_employee_id(self, employee_id: str) -> None:
        self.__employee_id = employee_id

    def set_name(self, full_name: str) -> None:
        self.full_name = full_name

    def set_salary(self, salary:float) -> None:
        self.salary = salary

    def set_job_title(self, job_title:str) -> None:
        self.job_title = job_title

    def get_name(self) -> str:
        return self.full_name
    
    def get_employee_id(self) -> str:
        return self.__employee_id
    
    def get_salary(self) -> float:
        return self.salary
    
    def get_job_title(self) -> str:
        return self.job_title


if __name__ == "__main__":
    # Create object with encapsulation
    employee = Employee("Data Enginner")
    # Set data
    employee.set_name("Clareth Chinchilla")
    employee.set_salary(4_750_500.28)
    employee.set_employee_id(f'{employee.get_name()[0]}{id(employee)}')
    # Get employee_id
    print(f'Employee_id: {employee.get_employee_id()}')
    # Change employee_id
    employee.__employee_id = "testPolyform123"
    print(f'Employee_id: {employee.get_employee_id()}')
    # using setter function
    employee.set_employee_id(f'{employee.get_name()[:2:1].upper()}{id(employee)}')
    print(f'Employee_id: {employee.get_employee_id()}')
    
