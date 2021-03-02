Objects
Up until this point you may have have heard me reference objects but never explain what they are. In python almost everything is an object! When we create variables and set them equal to certain data types what we are doing is creating a new object of that data type. When we create objects we say they are of different classes. Each class has attributes and properties associated with it. For example when we create a variable and set it = 1 we are creating a new object of class integer. Integers can be added, divided, multiplied etc. We can use the “type()” function to determine what class objects belong to.

type("hello")  # -> <class 'str'>
type(1)        # -> <class 'int'>
type([1,3])    # -> <class 'list'>
Classes
The built in data types in python are really just classes! That means that we can create our own data types by creating our own classes. Below is the basic syntax for creating our own class and adding our own methods.

class Number:
    def __init__(self):
        self.var = 24
    
    def display(self):
        print(self.var)

newNum = Number()
newNum.display()
The __init__() is whats known as a constructor method. It is automatically called when we create a new instance of the class.
The display() is whats known as a method. We can use it on instances of the class.

This tutorial is not meant for you to understand and be able to create your own classes. I simply want to introduce you to the concept so you are aware that it exists and have some familiarity with