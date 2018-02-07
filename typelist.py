l = ['magical unicorns',19,'hello',98.98,'world']
a = [2,3,1,7,4,12]
b = ['magical','unicorns']



def typ(g):
	su = 0
	newStr = ""
	for i in g:
		if isinstance(i, str):
			newStr += i + " "
		if isinstance(i, float):
			su += i
		if isinstance(i, int):
			su += i
	if su == 0:
		print "The list you entered is of string type"
		print newStr
	if newStr == "":
		print "The list you entered is of integer type"
		print su
	if su > 0 and not(newStr == ""):
		print "The list you entered is of mixed type"
		print newStr
		print su
typ(b)
typ(a)
typ(l)