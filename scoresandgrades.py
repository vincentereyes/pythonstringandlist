def scores():
	print "Scores and Grades"
	import random
	for x in range(10):
		i = random.randint(60,101)
  		if i > 59 and i <70:
  			print "Score: " + str(i) + "; Your Grade is D"
  		if i > 69 and i <80:
  			print "Score: " + str(i) + "; Your Grade is C"
  		if i > 79 and i <90:
  			print "Score: " + str(i) + "; Your Grade is B"
  		if i > 89 and i <101:
  			print "Score: " + str(i) + "; Your Grade is A"
scores()