# List comprehensions - To create a list with set of rules 

cubes = [i**3 for i in range(3)]

print(cubes)

cubes = [i**3 for i in range(3) if i**3 <= 5 ]

print(cubes)

