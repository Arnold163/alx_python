"""implemantation of the class"""
def is_kind_of_class(obj, a_class):
    """checks obj is an instance of a_class or subclass"""
    return isinstance(obj, a_class)

is_kind_of_class = __import__('1-is_kind_of_class').is_kind_of_class

"""a = 1
if is_kind_of_class(a, int):
    print("{} comes from {}" .format(a, int.__name__))
if is_kind_of_class(a, float):
    print("{} comes from {}" .format(a, float.__name__))
if is_kind_of_class(a, object):
    print("{} comes from {}" .format(a, object.__name__))"""
