"""this stuff is not easy i have less time aargh"""
class Square:
    """
    A class representing a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initializes a Square instance with a specified size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size

my_square = Square(3)
print(f"<class '{type(my_square).__module__}.{type(my_square).__name__}'>")
try:
    print(my_square.size)
except AttributeError:
    print("'Square' object has no attribute 'size'")
print(vars(my_square))

print(f"<class '{type(my_square).__module__}.{type(my_square).__name__}'>")
print(vars(my_square))

