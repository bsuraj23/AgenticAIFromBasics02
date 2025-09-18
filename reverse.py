
# Reverse a String in Python Without Using Slicing or Built-in Functions
# Using a LOOP

def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str  # Prepend each character
    return reversed_str
input_string = "SINDHU"
output_string = reverse_string(input_string)
print("Reversed String:", output_string)


# Using a List

def reverse_string(s):
    char_list = list(s)  # Convert string to list
    reversed_str = ""
    
    for i in range(len(char_list) - 1, -1, -1):  # Iterate backwards
        reversed_str += char_list[i]
    
    return reversed_str

input_string = "Hello"
output_string = reverse_string(input_string)
print("Reversed String:", output_string)

