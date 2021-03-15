n = int(input())
b = 0
c = int(10) # получаемое число
while (n >= 10) and (c >= 10):
	c = 0
	while n > 0:
		c = c + n % 10
		n = n // 10
	if c >= 10:
		n = c
		c = 0
		while n > 0:
			c = c + n % 10
			n = n // 10
		n = c
print(c)