# Example of a set in Python

# Creating a set
fruits = {"apple", "banana", "cherry", "apple"}  # Duplicate "apple" will be ignored

# Display the set
print("Fruits set:", fruits)

# Adding an element to the set
fruits.add("orange")
print("After adding 'orange':", fruits)

# Removing an element from the set
fruits.remove("banana")
print("After removing 'banana':", fruits)

# Checking membership
print("Is 'apple' in the set?", "apple" in fruits)

# Iterating through the set
print("Iterating through the set:")
for fruit in fruits:
    print(fruit)

# Set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union
print("Union of set_a and set_b:", set_a | set_b)

# Intersection
print("Intersection of set_a and set_b:", set_a & set_b)

# Difference
print("Difference of set_a and set_b:", set_a - set_b)

# Symmetric Difference
print("Symmetric Difference of set_a and set_b:", set_a ^ set_b)