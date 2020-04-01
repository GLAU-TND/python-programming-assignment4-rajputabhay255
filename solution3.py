a = input()# input from user for substring
b =  list(map(str,input().split()))#input from user
c = len(a)#len of substr
d = []
for i in b:
	if a == i[0:c]:
		d.append(i)
print(d)
