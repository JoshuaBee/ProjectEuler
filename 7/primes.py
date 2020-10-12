import math

# Generate primes up to n
def primesByValue(n):
  # Add the first prime 2 to the array
  primes = [2]
  
  # Loop over all odd numbers up to n
  for i in range(3, n + 1, 2):
    
    s = math.floor(math.sqrt(i))
    isPrime = True
    
    # Loop over the current prime list
    for prime in primes:
      # Check if the divisor is less then the square of i
      if prime <= s:
        # Check if i has any prime factors
        if i % prime == 0:
          # If so then i is not prime
          isPrime = False
          break
      # If so then prime cannot be a factor, so move on to the next number
      else:
        break
    
    # Check if the value i is prime
    if isPrime:
      # If so, add to the array
      primes.append(i)
  
  return primes

# Generate the first n primes
def primesByCount(n):
  # Add the first prime 2 to the array
  primes = [2]
  primeCount = 1
  
  # For some reason the while loop doesn't work, but the for loop does
  #i = 1
  #while primeCount < n:
    #i += 2
  # Loop over all odd numbers
  for i in range(3, 999999, 2):
    if primeCount == n:
      break
    
    s = math.floor(math.sqrt(i))
    isPrime = True
    
    # Loop over the current prime list
    for prime in primes:
      # Check if the divisor is less then the square of i
      if prime <= s:
        # Check if i has any prime factors
        if i % prime == 0:
          # If so then i is not prime
          isPrime = False
          break
      # If so then prime cannot be a factor, so move on to the next number
      else:
        break
    
    # Check if the value i is prime
    if isPrime:
      # If so, add to the array
      primes.append(i)
      primeCount += 1
      #print(i)
  
  return primes