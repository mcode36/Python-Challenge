### Find sum of all the prime numbers under 1000 ###

import math

#max_n = 2000000
max_n = 1000

prime_list = []

def is_prime(n):
    global prime_list
    flag = 1
    for i in prime_list:
        if i > math.sqrt(n):
            break
        k = n % i
        if k == 0 :
            flag = 0
            break
    return flag


sum = 0
for a in range (2,max_n+1):
    r = is_prime(a)
    if r == 1:
        sum = sum + a
        #print("%d is prime" % a)
        prime_list.append(a)

print("Answer:", sum)

# when max_n = 1000, sum = 76127
# when max_n = 2000000, sum = 142913828922

