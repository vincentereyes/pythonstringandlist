def one():
	greeting = "hello"
	name = "dojo"
	print greeting, name

def two():
	ar = ['Wish', 'Mop', 'Bleet', 'March', 'Jerk']
	for i in range(0, len(ar)):
		print ar[i]

def three(x):
	elist=[]
	for i in range(0, 25):
		elist.append(x*2)
	print elist

def four(a):
	blank=""
	for i in range(len(a)-1, -1, -1):
		blank += a[i]
	print blank

def five():
	x = 10
	x = x * 7
	y = 30
	z = y + x
	z = z * 3
	z = z - y
	z = z / 27
	x = z + y
	y = 3
	x = x + y
	if x % 10 == 0:
		print "true"
	else:
		return False
print five()