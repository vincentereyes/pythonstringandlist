
a = [2,4,10,16]

def oddoreven():
	for i in range(1, 2001):
		if i % 2 == 0:
			print "Number is " + str(i) + ". This is an even number"
		else:
			print "Number is " + str(i) + ". This is an odd number"


def multiply(arr,num):
    for x in range(len(arr)):
        arr[x] *= num
    return arr

oddoreven()
print multiply(a,5)
