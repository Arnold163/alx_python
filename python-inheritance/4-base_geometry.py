"""base geo"""
class BaseGeometry:
    def area(self):
        """raising an exception"""
        raise Exception("area() is not implemented")
    
    """the code below"""
BaseGeometry = __import__('4-base_geometry').BaseGeometry

bg = BaseGeometry()

"""try:
    print(bg.area())
except Exception as e:
    print("[{}] {}" .format(e.__class__.__name__, e))"""
