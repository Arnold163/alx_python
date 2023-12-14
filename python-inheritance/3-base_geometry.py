"""base geometry"""
class BaseGeometry:
    pass

"""import base"""
BaseGeometry = __import__('3-base_geometry').BaseGeometry
bg = BaseGeometry()

print(bg)
print(dir(bg))
print(dir(BaseGeometry))
