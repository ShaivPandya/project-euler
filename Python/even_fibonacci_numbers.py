num1 = 0
num2 = 1
result = 0
sum_even = 0

def fibonacci_numbers():
  global num1, num2, result

  result = num1 + num2
  print('Fibonacci number is ', result)

  num1 = num2
  num2 = result

def check_even():
  global result, sum_even

  if result % 2 == 0:
    sum_even += result
  
  print('The sum is ', sum_even)

while num1+num2<4000000:
  fibonacci_numbers()
  check_even()

"""
num1 = 0
num2 = 1
total = 0

while num1 < 4000000:
  num1, num2 = num2, num1+num2
  if num1 % 2 == 0:
    total += num1

print(total)
"""