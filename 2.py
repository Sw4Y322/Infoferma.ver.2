a = [2,4,6,-3,9,-4,3,9,4]
i = 0
b = a[1]+a[0]
for i in range ((len(a))-1):
	if a[i]+a[i+1]>b:
		b = a[i]+a[i+1]
	i = i + 1
print(b)