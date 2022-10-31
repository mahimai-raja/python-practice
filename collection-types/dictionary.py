car = {"BMW":"blue", 
        "Volvo":"red",
        2 : [1,2],
        }   

# NOTE : you cannot have a iterable as key in dictionary

print(car.get(2)[1])

nums = {
    1 : "one",
    2 : "two",
    3 : "three",
}

print(2 in nums)   # in operator checks only the key in dict
print("one" in nums)   # meanwhile values are not iterated
print(nums.get(7,42))  # if nums don't have 7 it prints 42
print(nums.get(4, "Not found")) 