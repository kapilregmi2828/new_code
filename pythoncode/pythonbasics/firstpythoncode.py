# external modules
import pandas
import numpy

# internal modules
import os
import sys
import datetime 

# enabling the envrironment files and variables

openai_api_key = os.environ.get("OPENAI_API_KEY")
username = os.environ.get("oracle_user")
password = os.environ.get("orcle_password")

a = 1 # integer variable
b = 2.5 # float variable
c = "Hello World" # string variable

Name = input("What is your name? ")

# function, class, loop, conditional statements, and data structures

if a == 1:
    print("a is equal to 1")

for i in range(5):
    print(i)

def fun1(name = Name):
    print("This is a function coding and My name is " + name)

# execution of the function or class
fun1()