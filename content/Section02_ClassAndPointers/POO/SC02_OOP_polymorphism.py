"""Python Polymorphism

Create class Vehicles
and their derivates
Truck, Car, Motorcycle.

"""


class Vehicle:
    """
    Main class
    """

    def __init__(self, number_of_wheels: int, vehicle_brand: str) -> None:
        """Constructor

        Args:
            number_of_wheels (int)
            vehicle_brand (str)
        """
        self.number_of_wheels = number_of_wheels
        self.vehicle_brand = vehicle_brand

    def __str__(self) -> str:
        return f"The vehicle has {self.number_of_wheels} \
        wheels and their mark is {self.vehicle_brand}"


class Truck(Vehicle):
    """Truck class

    Args:
        Vehicle (_type_): Main class
    """

    def __init__(self, number_of_wheels: int, vehicle_brand: str) -> None:
        super().__init__(number_of_wheels, vehicle_brand)

    def __str__(self) -> str:
        return f"The type of vehicle is Truck and it has {self.number_of_wheels} \
        wheels and their mark is {self.vehicle_brand}"


class Car(Vehicle):
    """Car class

    Args:
        Vehicle (_type_): Main class
    """

    def __init__(self, number_of_wheels: int, vehicle_brand: str) -> None:
        super().__init__(number_of_wheels, vehicle_brand)

    def __str__(self) -> str:
        return f"The type of vehicle is Car and it has {self.number_of_wheels} \
        wheels and their mark is {self.vehicle_brand}"


class Motorcycle(Vehicle):
    """Motorcycle class

    Args:
        Vehicle (_type_): Main class
    """

    def __init__(self, number_of_wheels: int, vehicle_brand: str) -> None:
        super().__init__(number_of_wheels, vehicle_brand)

    def __str__(self) -> str:
        return f"The type of vehicle is Motorcycle and it has {self.number_of_wheels} \
        wheels and their mark is {self.vehicle_brand}"


if __name__ == "__main__":
    # Create objects with polymorphism
    truck = Truck(8, "Mercedes Benz - Wagon")
    car = Car(4, "Audi - Q4")
    motorcycle = Motorcycle(2, "Yamaha - FZ")
    # Show behavior
    print(truck)
    print(car)
    print(motorcycle)
