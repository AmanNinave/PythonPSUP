2 test cases failed

s,d = list(map(int,input().split()));

#print(s , d);
arr = list();
sum =0;

for i in range(d):
	arr.append(9);
	sum+=9;
diff = sum-s;

if s == 0 or d == 0 or d>4 or s >36:
	print(-1);
else :
	i = -1;
	while diff != 0 :
		if diff >= 9:
			arr[i] = 0;
			diff = diff - 9;
		else :
			arr[i] = arr[i]-diff;
			diff = 0;
		i=i-1;
	for i in arr:
		print(i, end="");