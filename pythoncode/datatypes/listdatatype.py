a = [1, 2,3,10.5, "Kapil", 3j, True]
b = [1,1,1,2,2,2,3,3,3]

# list data types can be ordered, changed and allow duplicate values
# list data types is mutable data type - (we can modify the list after creation)

c = [10,20,30,40,50] # index = 0,1,2,3,4 or -5,-4,-3,-2,-1
print(c)
print(c[0]) # 10
print(c[-1]) # 50
print(c[0:3]) # 10,20,30 # access the element using index

# adding date to the list : append, insert, extend
c.append(60) # append() method is used to add an element at the end of the list
print(c)

c.insert(2,25) # insert() method is used to add an element at the specified index
print(c)

b.extend(a)
print(b) # extend() method is used to add multiple elements to the end of the list

b.extend(c)
print(b) # extend() method is used to add multiple elements to the end of the list

# deleting data from the list : remove, pop, del, clear

c.remove(30)
print(c) # remove() method is used to remove the first occurrence of the specified element from the list

c.pop(2) 
print(c) # pop() method is used to remove the element at the specified index and return it

c.pop() # pop() method is used to remove the last element from the list and return it
print(c)

c.clear() # clear() method is used to remove all elements from the list
print(c)

del c #del is used to delete the list completely


d = [10,20,40,30,50]
print(d)
d.sort() # sort() method is used to sort the list in ascending order
print(d)

d.sort(reverse=True) # sort() method is used to sort the list in descending order
print(d)

