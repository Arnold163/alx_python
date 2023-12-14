"""
Module 8-square
"""
Rectangle = __import__('7-rectangle').Rectangle


class Square(Rectangle):
    """
    Class Square, inherits from Rectangle
    """
    def __init__(self, size):
        """
        Initializes the Square instance.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Returns the string representation of the square.

        Returns:
            str: The string representation of the square.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)


if __name__ == "__main__":
    s = Square(13)
    print(s)
    print(s.area())