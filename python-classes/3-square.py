class Square:
    def __init__(self, size=0):
        self.size = size
    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size ** 2
    
#my_square_1 = Square(3)
#print("Area: {}" .format(my_square_1.area()))
#print("size: {}".format(my_square_1.size))

try:
    my_square_1 = "invalid"
except Exception as e:
        print(e)

try: 
    my_square_2 = Square(89)
    print(my_square_2.size)
    print(my_square_2.area())
except Exception as e:
    print(e)

try: 
    my_square_3 = Square(-33)
    print(my_square_3.size)
    print(my_square_3.area())
except Exception as e:
    print(e)

try: 
    my_square_4 = Square(33)
    print(my_square_4.size)
    print(my_square_4.area())
except Exception as e:
    print(e)

     