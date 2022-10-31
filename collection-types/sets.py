words = {'hi', 'hello', 'hi'} 
words2 = {'hi', 'nothello'}
print('hi' in words)
print(words)
# NOTE : Duplicate values are avoided

# print(words[1]) - Set are not indexed

a, b = words   # Unpacking of sets 
print(type(a))  # Gives prinmitive datatypes only 

words.add('new')
print(words)

words.remove('new')
print(words)

print(words | words2)  # Union
print(words & words2)  # Intersection
print(words - words2)  # Difference
print(words ^ words2)  # symmetric difference