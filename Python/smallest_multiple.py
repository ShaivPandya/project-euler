import math
divisors = list(range(1,21))

lcm = divisors[0]
for i in range(1,len(divisors)):
  lcm = lcm*divisors[i]//math.gcd(lcm, divisors[i])
print(lcm)
