import math
import random

n = random.randint(1, 100)

if n%2 != 0:
    print("Weird")
elif (n%2 ==0) and (2 <= n <= 5):
    print("Not Weird")
else:
    print(n)