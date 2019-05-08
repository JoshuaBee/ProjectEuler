# Time
import time
t = time.time() # Start time

# Variables
n = 1000 # Max integer value
s = 0 # Total

# Loop over all integers up to n
for i in range(1, n):
  # Check whether the integer is a multiple of 3 or 5
  if (i % 3 == 0) or (i % 5 == 0):
    # If so, add to the total
    s += i

print("Result: %s" %(s))
print("%s seconds" %(time.time() - t))