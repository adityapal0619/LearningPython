# Example of a List
example_list = [1, 2, 3, 4, 5]

# Example of a Dictionary
example_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Example of a Tuple
example_tuple = (10, 20, 30, 40, 50)

# Example of a Set
example_set = {100, 200, 300, 400, 500}

# Printing the examples
print("List:", example_list)
print("Dictionary:", example_dict)
print("Tuple:", example_tuple)
print("Set:", example_set)
# List methods
print("List Methods:")
print("append(x): Adds an item x to the end of the list.")
print("extend(iterable): Extends the list by appending elements from the iterable.")
print("insert(i, x): Inserts an item x at a given position i.")
print("remove(x): Removes the first occurrence of an item x.")
print("pop([i]): Removes and returns the item at position i (default is the last item).")
print("clear(): Removes all items from the list.")
print("index(x[, start[, end]]): Returns the index of the first occurrence of x.")
print("count(x): Returns the number of occurrences of x.")
print("sort(key=None, reverse=False): Sorts the list in ascending order.")
print("reverse(): Reverses the elements of the list in place.")
print("copy(): Returns a shallow copy of the list.")

# Dictionary methods
print("\nDictionary Methods:")
print("keys(): Returns a view object of all keys.")
print("values(): Returns a view object of all values.")
print("items(): Returns a view object of all key-value pairs.")
print("get(key[, default]): Returns the value for a key, or default if key is not found.")
print("pop(key[, default]): Removes and returns the value for a key.")
print("popitem(): Removes and returns the last inserted key-value pair.")
print("clear(): Removes all items from the dictionary.")
print("update([other]): Updates the dictionary with key-value pairs from other.")
print("setdefault(key[, default]): Returns the value of a key, or sets it to default if not present.")
print("copy(): Returns a shallow copy of the dictionary.")
print("fromkeys(iterable[, value]): Creates a new dictionary with keys from iterable and values set to value.")

# Tuple methods
print("\nTuple Methods:")
print("count(x): Returns the number of occurrences of x.")
print("index(x[, start[, end]]): Returns the index of the first occurrence of x.")

# Set methods
print("\nSet Methods:")
print("add(x): Adds an element x to the set.")
print("remove(x): Removes an element x from the set; raises KeyError if not found.")
print("discard(x): Removes an element x from the set if present.")
print("pop(): Removes and returns an arbitrary element from the set.")
print("clear(): Removes all elements from the set.")
print("union(*others): Returns the union of the set and others.")
print("intersection(*others): Returns the intersection of the set and others.")
print("difference(*others): Returns the difference of the set and others.")
print("symmetric_difference(other): Returns the symmetric difference of the set and other.")
print("issubset(other): Checks if the set is a subset of other.")
print("issuperset(other): Checks if the set is a superset of other.")
print("isdisjoint(other): Checks if the set has no elements in common with other.")
print("copy(): Returns a shallow copy of the set.")