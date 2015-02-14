#y listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
#What is the 10 001st prime number?


primes = [2]

i =3;

def isprime(x,primes):
    
    for y in primes:
        if x%y ==0:
            return False

    return True



while len(primes)< 10001:

    if isprime(i,primes) == True:
        primes.append(i)
    i = i+2




