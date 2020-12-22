largest_palindrome = 0
num1 = num2 = 0

for i in range(100, 1000):
  for j in range(100, 1000):
    if str(i*j) == str(i*j)[::-1]:
      if i*j > largest_palindrome:
        largest_palindrome = i*j
        num1, num2 = i, j

print(largest_palindrome)
print(num1, num2)
