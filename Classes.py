def Example1():
    class MyClass:
        x = 5

    p1 = MyClass()
    print(p1.x)

def Example2():
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
        def myfunc(self):
            print("Hello my name is " + self.name)

    p1 = Person("Bob", 21)
    p1.myfunc()

Example2()
