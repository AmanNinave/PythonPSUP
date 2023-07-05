x = int(input())
check = True;
i=1;
if x >=0 and x<=10:
	while i<10:
		y = str(i**x);
		if len(y) == x:
			print(y);
		elif len(y) >x :
			check = False;
			break;
		i+=1;

#n = int(input())
sum = 0
if(n>0 and n<=10):
	for i in range(1,n+1):
		sum = str(i**n)
		if(len(sum)==n):
			print(sum)
		elif len(sum) > n:
			break;