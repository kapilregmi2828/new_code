# in built module: os, sys, datetime, re, json, csv, random, subprocess, argparse, logging, http.

# OS module is used to perform operating system related operations like file handling, directory handling, process handling, etc.

import os
# get current working directory
print(os.getcwd())   
print(os.listdir()) # list all files and directories in the current working directory

#print(os.mkdir("test_dir")) # create a new directory
#print(os.rmdir("test_dir")) # remove a directory

# if os.path.exists("test_dir"):
#     print("Directory exists and deleted")
#     os.rmdir("test_dir") # remove a directory
# else:
#     print("Directory does not exist and created")
#     os.mkdir("test_dir") # create a new directory

os.system("dir") # execute a command in the command prompt and return the output

user_name = os.getlogin() # get the current logged in user name
print(user_name)

if os.path.exists("test.txt"):
    file_size = os.path.getsize("test.txt") # get the size of the file in bytes
    print(f"filename: test.txt")
    print(f"File size: {file_size} bytes")

else:
    print("File does not exist")

os.environ["default_name"] = "admin" # set an environment variable
print(os.environ["default_name"]) # get the value of an environment variable    


