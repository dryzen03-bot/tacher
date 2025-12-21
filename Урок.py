'''import requests
help(requests)'''

'''import requests

def first_function():
    pass

class Human:
    pass

rq=requests
ff=first_function
nick=Human

print(requests.__name__)
print(rq.__name__)
print(first_function.__name__)
print(ff.__name__)
print(Human.__name__)
print(nick.__name__)'''

'''a = [1, 2, 3]
print (dir(a))'''

'''print(type(1.2))

print(type([1, 2, 3]))

print(type((3, 'Three')))
def do_something():
    pass

print(type(do_something))
class Fruit:
    pass

print(type(Fruit))'''

'''class Fruit:
    tasty = True

fruit = Fruit()
if hasattr(fruit, 'tasty'):
    print('The fruit is tasty')
else:
    print('The fruit is not tasty')'''

'''data='string'
print(getattr(data,'reverse',None))'''

'''data='string'
def first_function():
    pass

print(callable(data))
print(callable(first_function))'''

'''class Human:
    pass

class YOU(Human):
    pass

print(issubclass(Human,YOU))
print(issubclass(YOU,Human))'''

'''class Human:
    pass

class YOU(Human):
    pass
your_smartphone=YOU()

print(isinstance(your_smartphone,Human))
print(isinstance(your_smartphone,YOU))'''

'''class YOU:
    pass
class Me:
    pass

your_smartphone=YOU()

print(isinstance(your_smartphone,Me))
print(isinstance(your_smartphone,YOU))'''

'''import inspect
import requests

print(inspect.ismodule(requests))
print(inspect.isclass(requests))
print(inspect.isfunction(requests))'''

'''import inspect
import requests
print(inspect.getmodule(requests.get))
print(inspect.get   module(list))'''

'''import inspect
class Human:
    def __init__(self, age, height, name='Nick'):
        self.age = age
        self.height = height
        self.secondname='Wild'

sig = inspect.signature(Human)
for i in sig.parameters.values():
    print(i.name,i.default)

#print(inspect.signature(Human))'''

'''import sys
print(sys.executable)
print(sys.version)'''

'''import sys
print(sys.platform)'''

'''import sys
print(sys.argv)'''

'''import sys
import requests
import math
import tkinter
print(sys.modules)
for module_name, module_path in sys.modules.items():
    print(module_name, module_path)'''

'''try:
    print("start code")
    print(error)
    print("No errors")
except:
    print("We have an error")
    print("code after capsule")'''

'''try:
    print("start code")
    print(10/0)
    print("No errors")
except NameError:
    print("We have an error")
except ZeroDivisionError:
    print("НА 0 ДЕЛИТЬ НЕЛЬЗЯ!!!")

print('code after capsule')'''

'''try:
    print("start code")
    print(10/0)
    print("No errors")
except (NameError,ZeroDivisionError):
    print("We have an error", "НА 0 ДЕЛИТЬ НЕЛЬЗЯ!!!")'''

'''try:
    print("start code")
    print(10/0)
    print("No errors")
except (NameError,ZeroDivisionError) as error:
    print(error)'''

'''try:
    try:
        print("start code")
        print(eerror)
        print("No errors")
    except SyntaxError:
        print("WRONGSyntax")
except NameError as error:
    print(error)'''
'''try:
    print("start code")
except:
    print("something is wrong")
else:
    ('net problem')
finally:
    print('end code')'''

def checker(var_1):
    if type(var_1)!= str:
        raise TypeError(f"Sorry, we can’t work with {type(var_1)}, "
                        f""f"we need class str")
    else:
        return var_1
first_var = 10
checker(first_var)

'''class BuildingEror(Exception):
    def __str__(self):
        return (f"With so much material the"
                f"house cannot be built!")
def check_material(amount_of_material,limit_value):
    if amount_of_material > limit_value:
        return "enough material"
    else:
        raise BuildingEror(amount_of_material)
materials = 123
check_material(materials, 300)'''

'''import warnings
warnings.warn('Tut Pusto', SyntaxWarning)'''

'''import warnings
warnings.simplefilter('ignore',SyntaxWarning)
warnings.simplefilter('always',ImportWarning)

warnings.warn('Tut Pusto', SyntaxWarning)
warnings.warn('Net Bibloiteki', ImportWarning)'''

'''import warnings
warnings.simplefilter('ignore',SyntaxWarning)
warnings.simplefilter('error',ImportWarning)

warnings.warn('Tut Pusto', SyntaxWarning)

try:
    warnings.warn('Net Bibloiteki', ImportWarning)
except:
    print('warning processed')'''