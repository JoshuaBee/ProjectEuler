# Time
import time
t = time.time() # Start time

# Imports
import math
from primes import *

# Variables
n = 20 # Max divisor
r = 1 # Result
m = 0 # Local factor count
max = 0 # Global factor count

p = primes(n) # Generate primes up to n

# Loop over all the primes up to n
for i in p:
  max = 0
  # Loop over values up to n
  for j in range(2, n + 1):
    m = 0
    
    # Check the prime factors of j
    while j % i == 0:
      j /=  i
      m += 1
    
    # Record the highest factor count
    if m > max:
      max = m
  
  # Multiply the prime factors together
  r *= int(math.pow(i, max))

print("Result: %s" %(r))
print("%s seconds" %(time.time() - t))