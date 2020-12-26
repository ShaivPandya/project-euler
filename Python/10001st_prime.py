
prime = 0
num = 2

while prime < 10001:
    for i in range(2, num+1//2):
        if num%i == 0:
            break
    else:
        prime +=1
    num +=1
print(num-1)

# Convert the following Python 2 code into Python 3
"""
def primes(n):
    '''
    Generate primes using the sieve algorithm
    '''
    if n == 2:
        return [2]
    elif n < 2:
        return []
    s = range (3, n+1, 2)
    mroot = n ** 0.5
    half = ((n + 1) / 2) - 1
    i = 0
    m = 3
    while m <= mroot:
        if s[i]:
            j = (m * m - 3) / 2
            s[j] = 0
            while j < half:
                s[j] = 0
                j += m
        i = i+1
        m = 2 * i + 3
    return [2] + [x for x in s if x]

list = primes(200000) # generate a list of all primes below 2,00,000

print list[10000]
"""