"""Python Inheritance

Create classes Person and Bank account

"""


class Person:
    """
    Basic personal information of person
    """

    def __init__(self, tipe_id: str) -> None:
        """Constructor

        Args:
            tipe_id (str): dni, of id number person
        """
        self.__tipe_id = tipe_id
        self.first_name = None
        self.last_name = None
        self.age = None

    def set_name(self, fullname: str) -> None:
        self.first_name, self.last_name = fullname.split()

    def set_age(self, age: int) -> None:
        self.age = age

    def get_first_name(self) -> str:
        return self.first_name

    def get_last_name(self) -> str:
        return self.last_name

    def get_full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def get_age(self) -> int:
        return self.age


class BankAccount(Person):
    """ Bank Account

    Args:
        Person (_type_): inherence class Person
    """
    def __init__(self, account_number: str, tipe_id: str) -> None:
        self.__account_number = account_number
        super().__init__(tipe_id)

    def __str__(self) -> str:
        return f"Account Number: {self.__account_number}"

    def get_personal_data(self) -> None:
        print("Personal Data")
        print(f"Full Name: {self.get_full_name()}")
        print(f"Age: {self.get_age()}")
        print(f"Account Number: {self.__account_number}")


if __name__ == "__main__":
    # Create object with inherence
    person_account = BankAccount("MLP-451253489", "111")
    # Set data
    person_account.set_name("Silvia Rojas")
    person_account.set_age(21)
    # Get data
    person_account.get_personal_data()
