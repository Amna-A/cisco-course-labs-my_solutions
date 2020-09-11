def isPrime(num):
    for j in range(2,num):
        if num%j  ==0:
            return False
    return True

for i in range(1, 20):
	if isPrime(i + 1):
			print(i + 1, end=" ")
print()