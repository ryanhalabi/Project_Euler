#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
good = []

n = 100000000

for i in range(1,n):
    if (20*i)%19==0:
        if (20*i)%18==0:
            if (20*i)%17==0:
                if (20*i)%16==0:
                    if (20*i)%15==0:
                        if (20*i)%14==0:
                            if (20*i)%13==0:
                                if (20*i)%12==0:
                                    if (20*i)%11==0:
                                        good.append(20*i)


print(good)
