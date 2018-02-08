from random import shuffle
class Deck(object):
	"""docstring for Deck"""
	def __init__(self):
		self.deck = []
		for i in range(0, 4):
			for j in range(1,14):
				if i == 0:
					temp = "heart"
				elif i == 1:
					temp = "diamond"
				elif i == 2:
					temp = "spade"
				else:
					temp = "clover"
				self.deck.append(Card(temp, j))

	def display(self):
			for i in range(0, len(self.deck)):
				print self.deck[i].shape, self.deck[i].number

	def shuffle1(self):
		shuffle(self.deck)

	def deal(self):
		temp = []
		for i in range(0,7):
			temp.append(self.deck.pop())
		return temp

class Card(object):
	"""docstring for Card"""
	def __init__(self, shape, number):

		self.shape = shape
		self.number = number


class Playa(object):
	"""docstring for Playa"""
	def __init__(self, name):
		self.name = name
		self.status = "active"
		self.hand = []
	def play(self):
		self.status = "active"
	def notplay(self):
		self.status = "inactive"	
		
a = Deck()
p = Playa("Vince")
a.display()
a.shuffle1()
a.display()
p.hand = a.deal()
print "====="
for i in range(0, len(p.hand)):
	print p.hand[i].shape, p.hand[i].number
a.shuffle1()
# a.display()
# print p.hand[0].number, p.hand[0].shape