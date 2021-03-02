Reading From A File
In many cases we may wish to use information stored in files. Python makes it very easy for us to open and read text files and to parse them into a list for further processing.

*IMPORTANT* Before attempting to open an existing text file be ensure that it is in the same directory as your python script. This simply means wherever your python file is stored on your computer your text file must be there with it! For example if your python file is stored on your Desktop in the folder Python (Desktop > Python) then your text file must be in that Python folder as well.

This is the basic syntax for opening a file:

f = open("file.txt", "r")
The open function takes two arguments. The first is the file name ("file.txt") and the second is the mode ("r"). The mode will tell python if it is reading, writing or appending to the document. In our case we use "r" standing for read.

Once we've opened the file and have stored it in a variable (in our case f) we can use the .readlines() method to convert each line into an element in a list.

f = open("file.txt", "r")

lines = f.readlines()

# lines looks like ["line 1 \n", "line 2 \n", "line 3"]
Now you may notice that each element in the list (excluding the last in some cases) has a trailing "\n". This "\n" is known as an escape character and it is how programs know to go to a newline. Typically this character is not visible to us but since we are reading in all of the content of the file we see it. To remove this character we can utilize the .strip() method.

f = open("file.txt", "r")

lines = f.strip().readlines()

# lines now looks like ["line 1", "line 2", "line 3"]