# Time
import time
t = time.time() # Start time

# Imports
import math

# Variables
n = 600851475143 # Value to factorise
i = 2

# Loop over all integers until all factor have been found
while n != 1:
  # Check whether the integer is a factor of n
  if n % i == 0:
    # If so, divide by the factor and check again
    n = n / i
  else:
    # Else move on to the next integer
    i += 1

print("Result: %s" %(i))
print("%s seconds" %(time.time() - t))