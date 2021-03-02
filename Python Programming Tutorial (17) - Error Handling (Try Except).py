Catching Errors
I'm willing to bet all of us have seen the dreaded red error text. In python we can except certain errors and prevent our program from crashing. To do this we use a try and except statement.

A common error you could run into is trying to convert a string to an int.

print("I will add 5 to any number you give me.")
num = input("type a number:")

addedNum = int(num) + 5
print("5 +", num, "is", addedNum)
Watch what happens when we type something that is not a number:

python try except

We cannot convert the string "hello" into an integer, hence we receive an error.

To fix this error we can use a try and except statement. The program will attempt to perform any operations inside of the try statement. If for some reason an error occurs, instead of crashing the program it will leave the try statement and do whatever is inside of the except statement.

print("I will add 5 to any number you give me.")
num = input("type a number:")

try:
    addedNum = int(num) + 5
    print("5 +", num, "is", addedNum)
except:
    print("That is not a number!!")