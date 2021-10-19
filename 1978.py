N = int(input())
data= list(map(int, input().split()))
primenumber = list()
n=1000

def isPrime(a):
  if(a<2):
    return False
  for i in range(2,a):
    if(a%i==0):
      return False
  return True

for i in range(n+1):
  if(isPrime(i)):
    primenumber.append(i)
count = 0
# print(primenumber)
for i in range(N):
    if data[i] in primenumber:
        count += 1
print(count)
