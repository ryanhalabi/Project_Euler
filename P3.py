#generate primes from 0 to n
import math

primes = [3]

n =600851475143

#n = 131950







def smallest(n):
    check = 0

    i = 1
    while (check ==0):
        i = i+1
        if ((n/i)%1 == 0):
            divisor = i
            check = 1

    return n/divisor

    print(i)




x = n

while ( smallest(x) != 1):
    x= smallest(x)

print(x)