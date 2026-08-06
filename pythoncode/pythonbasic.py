# input variables

name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
a = 10
# Output parameters
# print("Hello", name, "you are", age, "years old.")
# print("Hello " + name + ", you are " + age + " years old.")
print(f"Hello {name}, you are {age} years old.")
print("Hello {}, you are {} years old.".format(name, age))
print("Hello %s you are %s years old." % (name, age))

print(name)

if age < 18:
    print(f"Hello {name}, you are {age} years old. You are a minor.")
else:
    print(f"Hello {name}, you are {age} years old. You are an adult.")

def f1():
    a = 0 # Local variable
    print(f"The value of a is {a}")
    print(f"Hello {name}, you are {age} years old.")

f1()

print(f"The value of a is {a}")




