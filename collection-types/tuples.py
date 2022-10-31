# Tuples are similar to lists but they are immutable.

words = ('hi', 'hello', 'hi')
print(words)
# NOTE : Duplicate values are accepted.
# words[1] = 'Cheese' # you cannot mutate a tuple
print(words[1])

tup = (1, (1,2,3), 3, 4, 5)
# Multi-dimentional tuple is available

print(tup[1][1])

# Tuple unpacking 
# ---------------

a, b, *c, d = tup
print(tup)
print(c)  # it unpacks into list not tuple !
# *c - takes all values from the collection that are left over from other variables.

a, b, *c, d = tuple(range(20))
print(len(c))


