def toStrInBase(n, base):
	convert = '0123456789abcdef'
	if n < base:
		return convert[n]
	else:
		return toStrInBase(n // base,base)+convert[n%base]

num = input("Enter a number: ")
max = -1

for c in str(num):
	if (c == 'a'):
		c = 10
	if (c == 'b'):
		c = 11
	if (c == 'c'):
		c = 12
	if (c == 'd'):
		c = 13
	if (c == 'e'):
		c = 14
	if (c == 'f'):
		c = 15
		
	if (int(c) > int(max)):
		max = c
		
min_base = int(max) + 1
print('base', min_base, '=>', toStrInBase(int(num, min_base), 10))