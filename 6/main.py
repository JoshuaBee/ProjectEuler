# Time
import time
t = time.time() # Start time

# Imports
import math

# Variables
n = 100 # Number count
x = 0 # The sum of sqaures
y = 0 # The sqaure of sums

# Loop over all numbers up to n
for i in range(n + 1):
  # Sum the squares
  x += int(math.pow(i, 2))
  
  # Sum the values
  y += i

# Square the sums
y = int(math.pow(y, 2))

# The difference between the square of sums and the sum of squares
z = y - x

print("Result: %s" %(z))
print("%s seconds" %(time.time() - t))