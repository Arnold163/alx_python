""" wi this make it an enough comment slash documantation"""
class Base:
    """
    Class Base: the class for managing id attribute in other
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initializes thr Base instance.

        Args:
            id (int) : The public instance. If None, it is auto-incremented.
        

        Attributes:
            id (int): The public instance attribute representing the id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

        """thia is where it will output tye output"""

if __name__ == "__main__":
    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)
    