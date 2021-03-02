List Methods
Similarly to strings pythons list data type has many useful methods that we can implement. The two that I am going to show you here are .count() & .find(). These methods also work on strings!

- .count(): will count how many times a certain element appears.
- .find(): will find the first occurrence of an item and return its index.

myList = ["a", "b", "b", "a", "c", "d"]

myList.count("a")  # -> 2
myList.find("a")   # -> 0
myList.count("b")  # -> 2
myList.find("hello")  # -> -1
# If the element is not found .find() will return -1
Example
Problem: we would like to check the validity of an email address. For our purposes it is valid if it contains one "@", has length >= 5 and ends with a ".com"

email = input("Email Address: ")

if email.count("@") == 1 and len(email) >= 5:
    if email.find(".com") == len(email) - 4:
        print("Valid Email")
    else:
        print("Invalid Email, must end with .com")
else:
    print("Invalid Email, must contain one @ and be longer than 5 characters")