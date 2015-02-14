#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
#Find the largest palindrome made from the product of two 3-digit numbers.

import math as m
import numpy as np



def palin(i):
    i = int(i)
    if (  (str(i))[::-1]  == str(i) ) :
        return True
    return False

list =[0]

for i in range(-(999), -(100)):
    for j in range(-(999), i-1):
        print(m.fabs(i),' and ', m.fabs(j))
        if (i*j< max(list)):
            break
        if palin( m.fabs(i)* m.fabs(j)) == True:
            list.append( i*j)

print(max(list))