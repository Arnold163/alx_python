"""time for square now"""
from models.rectangle import Rectangle
class Square(Rectangle):
    """
    square class, inherits from rectangle.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        initializes a square instance.

        Args:
            size (int): The size of the square.
            x (int):The x-coordinate of the square (default is 0)
            y (int): The y-coordinate of the square (default is 0).
            id (int): The id of the square (default is None).
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter for the size attribute.

        Returns:
            int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute.

        Args:
            value (int): The size to set.

        Raises:
            TypeError: If value is not an int.
            ValueError: If value is not an int greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("size must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """
        returns a string representation of the square.

        returns:
            str: [Square] (<id>) <x>/<y> - <size>
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
    