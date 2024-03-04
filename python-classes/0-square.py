"""this stuff is not easy i have less time aargh"""
class Square:
    def __init__(self, size):
        self.__size = size

Square = __import__('0-square').Square

my_square = Square(3)
print(type(my_square))
#print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)


