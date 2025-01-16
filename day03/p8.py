"""
built-in variables

"""

class Employee:
    """This is an Employee class containing all functionalities used in this class"""
    x = 10

    def __init__(self, y):
        self.y = y
        self.z = None

def add(a,b):
    """
    This function will add two value a and b
    """
    pass


def greet(name:str,age:int) -> str:
    return f'Hello {name}, my age is {age}'

obj = Employee(101)

print(dir())
'''
print(__name__)
print(__file__)
print(__doc__)
print(add.__doc__)
print(Employee.__doc__)
'''
'''
print(Employee.__dict__)
print(obj.__dict__)
'''

print(greet.__annotations__)

print(greet("bhima",45))

print(dir(__builtins__))

__builtins__.print = lambda x: "Custome print statement"

print("Hello World")