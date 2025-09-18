
# Count vowels in a string.

# Using Regular Expressions

import re

s = "Python is fun!"
p = r'[aeiouAEIOU]'
vowel = re.findall(p, s)
print(f"Count: {len(vowel)}, Vowels: {vowel}")

# Using a Manual Loop

s = "Python is fun!"
vowels = "aeiouAEIOU"
counts = {}
for char in s:
    if char in vowels:
        counts[char] = counts.get(char, 0) + 1
print(counts)