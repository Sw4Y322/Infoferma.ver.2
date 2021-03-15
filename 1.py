d = {2:9,5:(-3),3:12,7:3,4:20,1:9,6:9,11:3,13:6}

newd = dict()

for v,k in d.items():
	print(v,k)
	if v < 6 and k >= 0:
		newd[v] = k
print(newd)