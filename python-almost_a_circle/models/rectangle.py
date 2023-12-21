"""models rectangle, lets see how this code goes"""
from models.base import Base

class Rectangle(Base):

    """
    class rectangle, inherits from base
    """

    def __init__(self, width, height, x=0, y=0, id=None):

        """
        this will initialize the rectangle instance
      

        Args:
            width (int) : The width of the rectangle.
            height (int) : the height of the rectangle.
            x (int) : the x-coordinate of the rectangle (default is 0).
            y (int): the y-coordinate of the rectangle (default is 0).
            id (int) : the id of the rectangle (default is none).
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def height(self):
       """
       getter for the height attribute.

       returns:
            int: the height of the rectangle
       """
       return self.__height 
    
    @height.setter
    def height(self, value):
       """
       setter for the height attribute.

       Args:
            value (int): the height to set.
        Raises:
            valueError: if value is not an int greater than 0
       """

       if not isinstance(value, int):
          raise ValueError("height must be an integer")
       if value <= 0:
          raise ValueError("height must be > 0")
       self.__height = value

    @property
    def x(self):
       """
       getter for x attri

       returns:
            int: the x-coordinate of the rectangle
       """
       return self.__x 
    
    @x.setter
    def x(self, value):
       """
       setter for the x attri

       Args:
            valueError: if value is not an integer.
       """
       if not isinstance(value, int):
          raise ValueError("x must be an integer")
       self.__x = value

    @property
    def y(self, value):
       """
       getter for the y attri.

       return:
            int: the y-coordinate of the rectangle.

        raised:
            valueError: if value is not an integer
       """

       if not isinstance(value, int):
          raise ValueError("y must be an integer")
       self.__y = value







       




