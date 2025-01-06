import os

# fileObject = open("created_file.txt", "x")
# print("File Created !!!")

if os.path.exists("created_file.txt"):
    os.remove("created_file.txt")
else:
    print("Specified file does not exist")