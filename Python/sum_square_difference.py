square_of_sum = sum(i for i in range(101)) ** 2
print(square_of_sum)

sum_of_squares = sum(j**2 for j in range(101))
print(sum_of_squares)

print(square_of_sum - sum_of_squares)

# How to write the code in one line
# print((sum(i for i in range(101)) ** 2) - (sum(j**2 for j in range(101))))
