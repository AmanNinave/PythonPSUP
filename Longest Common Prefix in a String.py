x = input();
arr = input().split();

str = '';
check = True;
i= 0;
while check:
	for j in arr:
		if len(j) > i and arr[0][i] == j[i]:
			check = True;
		else :
			check = False;
			break;
	if check :
		str+=arr[0][i];
	i+=1;
print(str);