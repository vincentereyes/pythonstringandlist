list_one = [1,2,5,6,5]
list_two = [1,2,5,6,5,3]

li = ['celery','carrots','bread','milk']
lis = ['celery','carrots','bread','cream']

q = ['celery','carrots','bread','cream']
w = ['celery','carrots','bread','cream']

def comparelists(lone, ltwo):
	a = len(lone)
	b = len(ltwo)
	count = 0

	if a != b:
		print "List is not the same"
	else:
		for i in range(0, a):
			if lone[i] != ltwo[i]:
				count +=1
		if count == 0:
			print "List is the same"
		else:
			print "List is not the same" 			


comparelists(list_one, list_two)
comparelists(li, lis)
comparelists(q,w)
