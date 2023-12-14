#!/usr/bin/env python3
"""pow = __import__('1-power').pow

print(pow(2, 2))
print(pow(98, 2))
print(pow(98, 0))
print(pow(100, -2))
print(pow(-4, 5))"""



class Base():
    """ My base class """

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances

class User(Base):
    """ My User class """
    pass

b = Base()
u = User()
print(u.id)

