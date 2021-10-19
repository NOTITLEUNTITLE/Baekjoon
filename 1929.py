num1, num2 = map(int, input().split())

def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5)+1):
        if num % i == 0:
            return False
    return True


for i in range(num1, num2+1):
    if isPrime(i):
        print(i)
