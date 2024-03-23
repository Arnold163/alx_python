"""this stuff is not easy i have less time aargh"""
class Square:
    def __init__(self, size):
        self.__size = size

my_square = Square(3)
print(f"<class '{type(my_square).__module__}.{type(my_square).__name__}'>")
print(vars(my_square))




