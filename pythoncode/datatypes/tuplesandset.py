# tuples are orders and immutable data types in python (unchageable). 
# They are defined by using parentheses () and can contain any number of elements of different data types.

# t1 = () - tuples
# f1() -- function

t1 = (1,1,1,1,2,3,4) #data of int, float, string, complex, boolean data types can be stored in tuples

user_name = ("admin", "kapil", "super") # static data can be stored in tuples
 
# with tuples we can only able to read the data

print(t1[0])
print(t1[0:3])

# Set is unordered and unindexed data type in python.
#  It is defined by using curly braces {} and can contain any number of elements of different data types.
#  Sets do not allow duplicate values.

s1 = {1,2,3,4,5,6,6,7,8,9,10} # data of int, float, string, complex, boolean data types can be stored in sets
print(s1) # duplicate values will be removed automatically

l1= [1,2,3,3,3,3,4,4,4,5,5] #data of int, float, str, complex, bool / duplicate values are allowed in list
print(l1)

l1 = set(l1) # converting list to set
print(l1) # duplicate values will be removed automatically  

l1 = list(l1) # converting set to list
print(l1) # duplicate values will be removed automatically
