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

    def __str__(self):
        """
        returns a string represantation of the square.

        returns:
            str: [square] (<id>) <x>/<y> - <size>
        """
        return f"[square] ({self.id}) {self.x}/{self.y} - {self.size}"

    