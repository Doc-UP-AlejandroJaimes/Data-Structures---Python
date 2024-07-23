"""Class Cookie

Containts the basic components of a class.

"""


class Cookie:
    def __init__(self, color: str) -> None:
        self.color = color

    def get_color(self) -> str:
        return self.color


if __name__ == "__main__":
    # Create two objects
    cookie_blue = Cookie("Blue")
    cookie_brown = Cookie("Brown")

    print(f"The Cookie 1, has color: {cookie_blue.get_color()}")
    print(f"The Cookie 1, has color: {cookie_brown.get_color()}")

    print(f"The Cookie 1, stored in: {id(cookie_blue)}")
    print(f"The Cookie 1, has color: {id(cookie_brown)}")
