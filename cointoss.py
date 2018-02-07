def cointoss():
	headcount = 0
	tailcount = 0
	import random
	for i in range(1, 5001):
		x = round(random.random())
		if x == 1.0:
			headcount +=1
			print "Attempt #" + str(i) + ": Throwing a coin... It's a head! ... Got " + str(headcount) + " head(s) so far and " + str(tailcount) + " tail(s) so far"
		else:
			tailcount +=1
			print "Attempt #" + str(i) + ": Throwing a coin... It's a tail! ... Got " + str(headcount) + " head(s) so far and " + str(tailcount) + " tail(s) so far"

	print "Ending the program. thank you!"
cointoss()