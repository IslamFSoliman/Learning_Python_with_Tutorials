Global vs Local Variables
Now that we've learned about functions it's time to understand an important topic, the difference between global and local variables. When we create a variable within a function is it said to be local to that function. This means that we cannot access variables that we've created within that function outside of it.

def myFunc():
    y = 7
    print(y)

myFunc()
print(y)  # -> This will cause an error!
# We cannot access the variable y as it is defined within a function
When we create variables in the main-line (not within a function) they are said to be global. This means that all of our functions can access these variables so long as they are defined after the variable is created.

x = 7

def myFunc():
    print(x)  # This will print 7
Global Keyword
Many times we would like to change a global variable from within a function. However, have a look at what happens when we try this below.

x = 7

def myFunc():
    x = 5
    
myFunc()
print(x)

# OUTPUT:
7
When we try to change the value of x from within the function what we actually end up doing is creating a new variable local to myFunc. To avoid this problem we can use the "global" keyword.

x = 7

def myFunc():
    global x
    x = 5
    
myFunc()
print(x)

# OUTPUT
5
Warning
It is typically not good practice to use global variables. This is because we usually design functions that are meant to be reused in future programs. So avoid using global variables if possible.
One case where a global variable is acceptable is when creating project/program specific functions that will not be re-used.