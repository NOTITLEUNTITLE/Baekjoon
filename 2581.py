m=int(input())
n=int(input())

primenumber = list()

def isPrime(a):
  if(a<2):
    return False
  for i in range(2,a):
    if(a%i==0):
      return False
  return True

for i in range(m, n+1):
  if(isPrime(i)):
    primenumber.append(i)

if len(primenumber):
  print(sum(primenumber))
  print(primenumber[0])
else :
  print(-1)



