import sys
def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5)+1):
        if num % i == 0:
            return False
    return True


result = list()
for i in range(1,246913):
    if isPrime(i):
        result.append(i)

while True:
    num = int(sys.stdin.readline())
    if num == 0:
        break
    count = 0
    for i in result:
        if num < i <= 2*num:
            count += 1
    print(count)

#while True:
#    num = int(sys.stdin.readline())
#    count = 0
#    if num == 0:
#        break
#
#    for i in range(num+1, 2*num+1):
#        if isPrime(i):
#            count += 1
#    print(count)
