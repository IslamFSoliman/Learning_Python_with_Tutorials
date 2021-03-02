# Functions
# Now it's time to talk about functions! In math functions simply apply operations to a given input and return some output. Now in computing not all functions require input and not all functions give output. The basic idea is that a function is a block of code that does something. Typically we use functions when we repeat the same or a similar task. One of the most basic examples of a function is seen below:

def addTwo(x):
    return x + 2

print(addTwo(3))  # This will print 5

    #___________________________________________________________#

# Before we can dive further into functions there are a few definitions we need to understand:

# - Parameters: These are the input for the function, they appear in the brackets of the function definition. In the example above our only parameter is x (you can have as many parameters as you want).

# - Arguments: These are what us (the programmer) passes to the function as input. The appear in the function call. In the example above the only argument is 3.

# Breaking Down The Syntax: when we create a function we first type the keyword "def" followed by a function name and brackets. Inside the brackets we can list all of our parameters. All of the lines underneath the function that are indented are apart of the function and will be executed when we call the function.

# Calling The Function: to call the function we must type the function name followed by brackets. Inside the brackets we must list all of the arguments that the function requires. For example, if the function has two parameters we need 2 arguments.

# Returning Values
# As you may have noticed in the above example our function addTwo uses the keyword "return". This indicates that at this line the function will terminate and return a certain value to wherever it was called from. However, not all functions need to return values. Some functions may manipulate a list or print something to the screen rather than returning a value. Some examples of different functions can be seen below:

    #___________________________________________________________#
# This function checks to see if every element in a list is a zero
# It returns to us a True or False value depending on the list it's given
def isZeros(li):    
    for element in li:
        if element != 0:
            return False
    return True

print(isZeros([0,0,0,1]))  # This will print False


# This function checks to see if every element in a list is a zero
# It displays to the screen True or False
# It does NOT return a value
def isZeros(li):
    check = True    
    for element in li:
        if element != 0:
            check = False
            break
    if check:
        print("True")
    else:
        print("False")

isZeros([0,0,0,0])  # Calling this will result in True being printed to the screen
    #___________________________________________________________#

# Some More Examples
# Note: Functions are meant to be re-used and thus can be used as many times as you would like. If you ever find yourself repeating code think about putting it into a function and calling that function in place of the repeated code.

# Problem: we want to ask a set of questions 5 times.

# Below I will show you three ways of solving this problem and then we will compare their efficiency and elegance.
    #___________________________________________________________#
# Solution 1:

name = input("Please type your name: ")
age = input("Please type your age: ")
country = input("Please type where you are from: ")
print("Your name is", name, "you are", years, "old and you are from", country + '.')

name = input("Please type your name: ")
age = input("Please type your age: ")
country = input("Please type where you are from: ")
print("Your name is", name, "you are", years, "old and you are from", country + '.')

name = input("Please type your name: ")
age = input("Please type your age: ")
country = input("Please type where you are from: ")
print("Your name is", name, "you are", years, "old and you are from", country + '.')

name = input("Please type your name: ")
age = input("Please type your age: ")
country = input("Please type where you are from: ")
print("Your name is", name, "you are", years, "old and you are from", country + '.')

name = input("Please type your name: ")
age = input("Please type your age: ")
country = input("Please type where you are from: ")
print("Your name is", name, "you are", years, "old and you are from", country + '.')
    #___________________________________________________________#

# Solution 2:

def askQuestions():
    name = input("Please type your name: ")
    age = input("Please type your age: ")
    country = input("Please type where you are from: ")
    print("Your name is", name, "you are", age, "old and you are from", country + '.')

askQuestions() #1
askQuestions() #2
askQuestions() #3
askQuestions() #4
askQuestions() #5
    #___________________________________________________________#

# Solution 3:

def askQuestions():
    name = input("Please type your name: ")
    age = input("Please type your age: ")
    country = input("Please type where you are from: ")
    print("Your name is", name, "you are", age, "old and you are from", country + '.')

for i in range(5):
    askQuestions()  # This will call the function 5 times
As we can see solution 2 and 3 are much more efficient and elegant. Not only do they use less lines of code but they are easier to read and make our program look cleaner.