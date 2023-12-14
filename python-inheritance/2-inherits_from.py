"""inheritance on its way"""
def inherits_from(obj, a_class):
    """obj instance of subclass"""
    return issubclass(type(obj), a_class)

inherits_from = __import__('2-inherits_from').inherits_from

"""a = True
if inherits_from(a, int):
    print("{} inherited from class {}" .format(a, int.__name__))"""