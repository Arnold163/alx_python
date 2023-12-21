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
          raise TypeError("height must be an integer")
       if value <= 0:
          raise ValueError("height must be > 0")
       self.__height = value

    @property
    def width(self):
        """
        Getter for the width attribute.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width
    
    @width.setter
    def width(self, value):
        """
        Setter for the width attribute.

        Args:
            value (int): The width to set.

        Raises:
            ValueError: If value is not an int greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

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
          raise TypeError("x must be an integer")
       if value < 0:
           raise ValueError("x must be >= 0")
       self.__x = value

    @property
    def y(self):
        """
        Getter for y attribute.

        Returns:
            int: The y-coordinate of the rectangle.
        """
        return self.__y
    
    @y.setter
    def y(self, value):
        """
        Setter for y attribute.

        Args:
            value (int): The y-coordinate to set.

        Raises:
            TypeError: if value is not an int.
            ValueError: If value is not an integer.
            
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
           raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        calculate and return the area of the rectangle

        Returns: 
            int: the area of the rectangle
        """
        return self.__width * self.__height
    
    def display(self):
        """
        print the rectangle instance with the character #.
        """

        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width, end="")
            print()
    
    def __str__(self):
        """
        return a string represantation of the rectangle.

        returns:
            str: [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
    

    """
    this is an update of the function below, it really needs a long comment to make it work, so that you understand the code, its good practice
    """
    def update(self, *Args):

        """
        Update the Rectangle attributes.

        Args:
            *args: Variable number of arguments in the order (id, width, height, x, y).
        """
        if len(Args) >= 1:
            self.id = Args[0]
        if len(Args) >= 2:
            self.width = Args[1]
        if len(Args) >= 3:
            self.height = Args[2]
        if len(Args) >= 4:
            self.x = Args[3]
        if len(Args) >= 5:
            self.y = Args[4]

"""example of isage  same here good manners"""
r = Rectangle(1, 2, 3, 4, 5)
print(r) #before update

r.update(10, 20, 30, 40, 50)
print(r)
"""after update and here too i hope it passes this time"""
        
            
    








       




