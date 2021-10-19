#num = int(input())
#
#while num != 1:
#    for i in range(2, num+1):
#        if num % i == 0:
#            print(i)
#            num = num // i
#            break



n = int(input())

while n % 2 == 0:
	n //= 2
	print(2)

index = 3

while index * index <= n and n > 1:

	while n % index == 0:
		n //= index
		print(index)

	index += 2

if n != 1:
	print(n)

