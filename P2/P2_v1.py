### Find sum of all the prime numbers under 1000 ###

max_n = 1000
prime_list = [2]

def is_prime(n):
    global prime_list
    flag = 1
    for i in prime_list:
        if i > (n/2):
            break
        k = n % i
        if k == 0 :
            flag = 0
            break
    return flag

## test
sum = 2
for a in range (3,max_n+1):
    r = is_prime(a)
    if r == 1:
        sum = sum + a
        prime_list.append(a)

print("Answer:", sum)