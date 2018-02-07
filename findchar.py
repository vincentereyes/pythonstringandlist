
a = ['hello','world','my','name','is','Anna','okay']
new_list = []

for i in a:
	if i.count('o') > 0:
		new_list.append(i)
print new_list