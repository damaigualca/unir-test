import app
import math

class InvalidPermissions(Exception):
    pass


class Calculator:
    def add(self, x, y):
        self.check_types(x, y)
        return x + y

    def substract(self, x, y):
        self.check_types(x, y)
        return x - y

    def multiply(self, x, y):
        if not app.util.validate_permissions(f"{x} * {y}", "user1"):
            raise InvalidPermissions('User has no permissions')

        self.check_types(x, y)
        return x * y

    def divide(self, x, y):
        self.check_types(x, y)
        if y == 0:
            raise TypeError("Division by zero is not possible")

        return x / y

    def power(self, x, y):
        self.check_types(x, y)
        return x ** y
    
    # changes 16.05.2023
    def square_root(self, x):
        self.check_types(x, 0)
        if x < 0:
            raise TypeError("Square root of negative number is not possible")
        return x ** 0.5
    
    def log10(self, x):
        self.check_types(x, y)
        # only positive numbers
        if x < 0:
            raise TypeError("Logarithm of negative number is not possible")
        return math.log10(x)

    def check_types(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Parameters must be numbers")


if __name__ == "__main__":  # pragma: no cover
    calc = Calculator()
    result = calc.add(2, 2)
    print(result)

    result = calc.substract(2, 2)
    print(result)

    result = calc.multiply(2, 2)
    print(result)

    result = calc.divide(2, 2)
    print(result)

    result = calc.power(2, 2)
    print(result)

    result = calc.square_root(4)
    print(result)

    result = calc.log10(4, 2)
    print(result)
