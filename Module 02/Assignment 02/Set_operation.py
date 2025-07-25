'''Writing a Python program that takes two sets from the user and computes their union, intersection, and difference.

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}'''

# take input from the user
input_1 = input("Enter the first set:\n")
input_2 = input("Enter the Second set:\n")

# split the input, convert into integer and create list
list_1 = list(map(int, input_1.split()))
list_2 = list(map(int, input_2.split()))

# converting the list to set
set1 = set(list_1)
set2 = set(list_2)

# print the set 
print("First set:", set1)
print("Second set:", set2)

# perform operations
union = set1.union(set2)
intersection = set1.intersection(set2)
difference = set1 - set2

#print the result
print("Union of two sets:", union)
print("Intersection of two sets:", intersection)
print("Difference of two sets:", difference)
