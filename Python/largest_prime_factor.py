num = 600851475143
largest_prime = 0

# The divisor starts at 2 because starting at one will cause
# an infinite loop 
divisor = 2

# In this loop, it will divide the number by a divisor until
# it can no longer be divided by that divisor.
# When that happens, it will change the divisor by increasing it by 1.
while divisor <= num:

  # If there is a remainder, increase the divisor by 1
  if num % divisor:
    divisor += 1

  # If it divides cleanly, divide it and make it the "largest_prime"
  else:
    num /= divisor
    largest_prime = divisor

print(largest_prime)      # The correct answer is 6857
