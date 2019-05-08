# Time
import time
t = time.time() # Start time

# Variables
x_1 = 1 # First value in sequence
x_2 = 2 # Second value in sequence
p = 0 # Placeholder value
n = 4000000 # Max value
s = 0 # Total

# Continue to loop until the sequence exceeds the max value
while x_2 < n:
  # Check if the value is even
  if x_2 % 2 == 0:
    # If so, add to the total
    s += x_2
  # Store the second value in the placeholder
  p = x_2
  # Update the second value by summing the first and second value
  x_2 = x_1 + x_2
  # Update the first value from the placeholder
  x_1 = p

print("Result: %s" %(s))
print("%s seconds" %(time.time() - t))