
# Check Prime Number in Python
# Using Math Module

import math

n = 11
if n <= 1:
    print(False)
else:
    is_prime = True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            is_prime = False
            break
    print(is_prime)

# Using Recursion

from math import sqrt

def Prime(n, i):  
    if i == 1 or i == 2:  
        return True
    if n % i == 0:  
        return False
    if Prime(n, i - 1) == False:  
        return False

    return True

n = 13
i = int(sqrt(n) + 1)

print(Prime(n, i))