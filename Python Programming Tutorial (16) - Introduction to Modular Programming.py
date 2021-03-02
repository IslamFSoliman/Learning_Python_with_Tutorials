
Modular Programming
Modular programming is the practice of splitting our code up into different files (modules) and then importing that code so that we can use it for many different projects. Typically code that you will be reusing goes into its own module so you can simply import that module rather than copying and pasting. This makes our programs more readable, easier to scale and nicer to work with.

A module is typically any python file that contains only functions and classes. A good example of module you may have used before is the math module. We can create and import our own modules.

Below is the code contained in two separate python files.

# File name: myModule.py

def func(x):
    return x + 2

def func2(y):
    return y * 78
# File name: main.py

import myModule

value = myModule.func(5)  # this will call the func function from myModule

print(value)  # this prints 7
We can use the import keyword to import modules that are built into python or that we've created.
Note: To import our own modules they must be in the same directory as the file we are importing from.

To avoid the use of "myModule" we can import specific functions from our modules using a combination of keywords "import" and "from".

# File name: main.py

from myModule import func

value = func(5)  # now we can just use func like a regular function

print(value)  # this prints 7