#A tuple consists of a number of values separated by commas, for instance:
t = 12345, 54321, 'hello!'
t[0]

t

# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
u

# Tuples are immutable:
t[0] = 88888


# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
v

#Ugly, but effective. For example:
empty = ()
singleton = 'hello',    # <-- note trailing comma
len(empty)

len(singleton)

singleton

#The statement t = 12345, 54321, 'hello!' is an example of tuple packing: the values 12345, 54321 and 'hello!' are packed together in a tuple. The reverse operation is also possible:
x, y, z = t