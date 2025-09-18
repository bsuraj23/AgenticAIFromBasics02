
# Python Program to Find Largest Number in a List
# Using a Loop 

a = [10, 24, 76, 23, 12]

# Assuming first element is largest.
largest = a[0]

# Iterate through list and find largest
for val in a:
    if val > largest:
      
      	# If current element is greater than largest
    	# update it
        largest = val

print(largest)

# Using max()
a = [10, 24, 76, 23, 12]

# Max() will return the largest in 'a'
largest = max(a)
print(largest)