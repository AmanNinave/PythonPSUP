def checkPrime(x):
	for i in range(2, x//2+1):
		if x%i == 0 :
			return False;
	return True;

def printPrime(x):
	y = 2;
	while x > 0:
		if checkPrime(y):
			x-=1;
		y+=1;
	return y-1;		

k = int(input());

print(printPrime(k));