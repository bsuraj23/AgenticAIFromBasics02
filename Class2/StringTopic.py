# Important Programs regarding String Concept

# Reverse a string
s = "Python"
print(s[::-1])  # nohtyP

# Palindrome check
word = "madam"
print(word == word[::-1])  # True

# Count vowels
s = "Hello World"
vowels = "aeiouAEIOU"
count = sum(1 for char in s if char in vowels)
print(count)  # 3# Formatting the Strings
name = "Alice"
age = 30
print("My name is {} and age is {}".format(name, age))
print(f"My name is {name} and age is {age}")# Counting substring in the given String
s = "banana"
print(s.count("a"))   # 3# Replacing a String with another String
s = "I like Java"
print(s.replace("Java", "Python"))  # I like Python# Splitting of Strings
s = "apple,banana,cherry"
print(s.split(","))   # ['apple', 'banana', 'cherry']# Joining of Strings
fruits = ["apple", "banana", "cherry"]
print(", ".join(fruits))  # apple, banana, cherry# Changing Case of a String
s = "Python Programming"
print(s.upper())   # PYTHON PROGRAMMING
print(s.lower())   # python programming
print(s.title())   # Python Programming
print(s.swapcase())# pYTHON pROGRAMMING# Strings are Data Types in Python
# str4= "\n \t \s"
str1 = "Rahul "
str2 = "mohan"

print(str1 + "" + str2)



# print("Have you observed syntax for str3\t" + str3)
str3 = """otherName\tajdhgfdajhg \t gahfgahgf 
 I am other line """

# STRING DATA TYPE
s = "Hello, World!"
print(type(s))  # <class 'str'>


# What is String?
s = "Python is fun"
print(s)

# How to define multi-line String Literals?
multi_line = """This is
a multi-line
string."""
print(multi_line)

# How to Access Characters of a String?
s = "Python"
print(s[0])    # P
print(s[-1])   # n


# How to Access Characters of a String?
s = "Python"
print(s[0])    # P
print(s[-1])   # n


# Behaviour of Slice Operator
s = "Python"
print(s[1:4])  # yth
print(s[:2])   # Py
print(s[2:])   # thon


# Slice Operator Case Study# Important Programs regarding String Concept

# Reverse a string
s = "Python"
print(s[::-1])  # nohtyP

# Palindrome check
word = "madam"
print(word == word[::-1])  # True

# Count vowels
s = "Hello World"
vowels = "aeiouAEIOU"
count = sum(1 for char in s if char in vowels)
print(count)  # 3
s = "Programming"
print(s[3:8])    # rammi
print(s[::-1])   # gnimmargorP

# Mathematical Operators for String
a = "Hello"
b = "World"
print(a + " " + b)   # Hello World
print(a * 3)         # HelloHelloHello

# len() in-built Function
s = "Python"
print(len(s))  # 6

# Checking Membership
s = "Python"
print("th" in s)     # True
print("abc" not in s) # True

# Comparison of Strings
a = "apple"
b = "banana"
print(a == b)   # False
print(a < b)    # True (lexicographical)


# Removing Spaces from the String
s = "  Hello World  "
print(s.strip())      # Hello World
print(s.lstrip())     # Hello World  
print(s.rstrip())     #   Hello World


# Finding Substrings
s = "Python programming"
print(s.find("gram"))   # 10
print(s.find("xyz"))    # -1