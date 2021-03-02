Writing to a File
Reading from a file is great but sometimes we also want to write information that we can access later. Writing to a file is extremely similar to reading. The only difference is the mode in which we open the file. There are two writing modes that we can use, append and write.

Appending to a file will add to the end of it. If we are opening in a file in "a" mode we must ensure it is in the same directory as our python script.

f = open("file.txt", "a")
Opening a file in "w" or write mode will clear the entire file if it exists. If it does not exist it will create a new one for us.

f = open("file.txt", "w")
Once we've opened our file we can write things to it. If we would like to write to a newline each time we must make sure we include a "\n" at the end of our write statement.

f = open("file.txt", "w")

lines = ["line 1", "line 2", "line 3"]
for line in lines:
    f.write(line + "\n")

f.close()  # Once we are done writing we must close the file to save the changes.
