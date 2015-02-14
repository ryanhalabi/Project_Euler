#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
#Find the sum of all the primes below two million.



import time
import math as m








n = 2000001

num =[]
for i in range(0,n+1):
    num.append(i)
num[1]=0

sum =0

t0 = time.time()

for i in range(0,n+1):
    if (num[i] != 0):
        sum = sum+num[i]
        k=1
        print(num[i])
        while (i*k<=n):
            num[i*k] = 0
            k = k+1

t1 = time.time()

print(t1-t0)

print(sum)





















