# Time
import time
t = time.time() # Start time

# Imports
from primes import *

# Variables
n = 10001 # Number count

p = primesByCount(n)

print("Result: %s" %(p[-1]))
print("%s seconds" %(time.time() - t))