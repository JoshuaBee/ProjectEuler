# Time
import time
t = time.time() # Start time

# Variables
n = 3 # Number of digits
n_max = int('9' * n) # Largest n-digit number
n_min = int('1' + '0' * (n - 1)) # Smallest n-digit number
r = 0

# Reverse loop over all n-digit numbers
for i in range(n_max, n_min - 1, -1):
  # Reverse loop over all n-digit numbers <= i
  for j in range(i, n_min - 1, -1):
    
    # Create the number string, and its reverse
    k = i * j
    p = str(k)
    q = p[::-1]
    
    # Compare the strings to see if they match
    if p == q:
      # If so, keep the largest value
      if k > r:
        r = k

print("Result: %s" %(r))
print("%s seconds" %(time.time() - t))