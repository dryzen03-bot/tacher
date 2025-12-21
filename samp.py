'''class Human:
    height = 170

class Student(Human):
    pass

class Worker(Human):
    pass'''


'''nick = Student()
print(nick.height)'''

'''class Hello:
    def __init__(self):
        print("Hello")

class HelloWorld(Hello):
    def __init__(self):
        super().__init__()
        print("World")'''

'''class Computer:
    def calculate(self):
        print("Calculating")

class Display:
    def display(self):
        print("Showing image")

class SmartPhone(Display, Computer):
    pass'''

class Computer:
    def __init__(self):
        super().__init__()
        self.memory = 128

class Display:
    def __init__(self):
        super().__init__()
        self.resolution = "4k"




