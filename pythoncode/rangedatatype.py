# range is a built-in function in Python that generates a sequence of numbers. It can take one, two, or three arguments:
# range(start, stop, step)

range(10) #default start is 0, stop is 10, step is 1
for i in range(10):
    print(i)

for i in range(10,100,10): # start is 10, stop is 100, step is 10
    print(i)

for i in range(100,-100,-10): # start is 100, stop is 10, step is -10
    print(i)
