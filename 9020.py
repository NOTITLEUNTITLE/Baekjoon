import sys
def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5)+1):
        if num % i == 0:
            return False
    return True


result = [False, False] + [True] * 10002

for i in range(2, 10001):
    if result[i]:
        for j in range(2*i, 10002, i):
            result[j] = False
            
t = int(sys.stdin.readline())

for i in range(t):
    num = int(sys.stdin.readline())
    min_num = num // 2
    max_num = min_num

    while min_num > 0:
        if result[min_num] and result[max_num]:
            print(min_num, max_num)
            break
        else :
            min_num -= 1
            max_num += 1
