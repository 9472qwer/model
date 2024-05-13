class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def foo(self):
        print(f"my name is {self.name}, my age is {self.age}")