#n = int(input())

import time

n = 111181177 # 4 secs

start = time.time()

is_prime = True

if n <= 1:
    is_prime = False
else:
    for i in range(2, int(n/2)):
        if n % i == 0:
            is_prime = False
            print("factor ", i)
            break
        else:
            is_prime = True

print(is_prime)

end = time.time()
print("n = {}; time = {}".format(n, end-start))
