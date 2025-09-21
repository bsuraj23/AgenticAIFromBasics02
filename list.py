# creating a list with fruits
# printing the list
fruits = ["apple", "banana", "cherry"]
print(fruits)

# addeding a fruit to the list ---"append"--- method
fruits.append("orange")
print(fruits)

# removing a fruit from the list ---"remove"--- method
fruits.remove("banana")
print(fruits)

# adding a fruit at a specific position ---"insert"--- method
fruits.insert(1, "kiwi")
print(fruits)

# sorting the list in ascending order ---"sort"--- method
fruits.sort()
print(fruits)   

# sorting the list in descending order ---"sort"--- method with reverse parameter
fruits.sort(reverse=True)
print(fruits)

# finding the index of a fruit ---"index"--- method
fruits= fruits.index("cherry")
print(fruits)

# counting occurrences of a fruit ---"count"--- method
fruits= fruits.count("apple")
print(fruits)

